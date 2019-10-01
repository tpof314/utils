import time

class Timer:
    def __init__(self):
        self.start = time.time()

    def tick(self):
        t = time.time()
        return t - self.start

    def reset(self):
        self.start = time.time()

    def print_time(self):
        t = self.tick()
        print('time: {:.2f} s'.format(t))


class Counter:
    def __init__(self, amount=1000):
        self.counts = 0
        self.amount_print = amount
        self.timer = Timer()

    def set_print_amount(self, amount):
        self.amount_print = amount

    def count(self):
        self.counts += 1

    def print_time(self):
        if self.counts % self.amount_print == 0:
            t = self.timer.tick()
            print("time: {:.2f} s, amount: {}".format(t, self.counts))

    def get_counts(self):
        return self.counts

    def reset(self):
        self.counts = 0
        self.timer.reset()
