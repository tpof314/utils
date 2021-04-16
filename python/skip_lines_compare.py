# Speed Test
from timer import Timer
import itertools

my_timer = Timer()
SKIP = 400000       # Lines to skip

# Much faster
my_file = open('./data/large_file.txt')
my_list = []
my_timer.reset()
for line in itertools.islice(my_file, SKIP, None):
    line = line.strip()
    my_list.append(line)
tick_t = my_timer.tick()
print('Time = {:.2} s'.format(tick_t))
my_file.close()


# Slower
my_file  = open('./data/large_file.txt')
my_list  = []
my_timer.reset()
for _ in range(SKIP):
    next(my_file)
for line in my_file:
    line = line.strip()
    my_list.append(line)
tick_t = my_timer.tick()
print('Time = {:.2} s'.format(tick_t))
my_file.close()

