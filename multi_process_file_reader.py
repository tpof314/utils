# Read file using multiprocess
from multiprocessing import Process
from multiprocessing import Pool
import itertools

# Single Process
class FileReader:
    
    def __init__(self, filename):
        self.my_list = []
        self.load_file(filename)

    def load_file(self, filename):
        fp = open(filename, "r")
        for line in fp:
            line = line.strip()
            self.my_list.append(line)

# Multi Process
class FileReaderMultiProcess:

    def __init__(self, filename, num_workers=8):
        self.my_list = []
        self.lines   = self._get_num_lines(filename)
        self.block_size = self.lines // num_workers

        self.args = []
        for worker_id in range(num_workers):
            first = worker_id * self.block_size
            last  = first + self.block_size
            if worker_id == num_workers - 1:
                last = self.lines

            self.args.append({
                "first": first,
                "last":  last,
                "worker_id": worker_id,
                "filename":  filename
            })
        
        pool = Pool(processes = num_workers)
        worker_results = pool.map(self.worker_fn, self.args)

        for result in worker_results:
            self.my_list.extend(result)

        for item in worker_results:
            del item

    def _get_num_lines(self, filename):
        # Get total number of lines of a text file
        num_lines = sum(1 for line in open(filename))
        return num_lines

    def worker_fn(self, args):
        filename  = args['filename']
        worker_id = args['worker_id']
        first     = args['first']
        last      = args['last']

        fp = open(filename, "r")
        count = first
        results = []
        for line in itertools.islice(fp, first, None):
            line = line.strip()
            results.append(line)
            count += 1
            if count >= last:
                break
        fp.close()
        return results

from timer import Timer

my_timer = Timer()

my_timer.reset()
reader = FileReaderMultiProcess('./data/train.src', num_workers=8)
result = reader.my_list
tick_t = my_timer.tick()
print("data size: {}, time: {:.2f}".format(len(result), tick_t))

my_timer.reset()
reader = FileReader('./data/train.src')
result = reader.my_list
tick_t = my_timer.tick()
print("data size: {}, time: {:.2f}".format(len(result), tick_t))