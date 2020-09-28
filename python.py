import time

num_runs = int(input('Сколько раз будем запускать цикл? '))

class TimeThis:

    def __init__(self, num_rums = 5):
        self.num_rums = num_rums 

    def __call__(self, func):
        def time_counter():
            avg_time = 0
            for i in range(self.num_rums):
                t0 = time.time()
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
                print('Проход {}: выполнение функции заняло {} секунд'.format((i + 1), (t1 - t0)))
            avg_time /= self.num_rums
            print('В среднем выполнение функции заняло {} секунд'.format(avg_time))
        return time_counter 

    def __enter__(self):
        self.t0 = time.time()

    def __exit__(self, *args):
        t1 = time.time()
        avg_time = (t1 - self.t0)
        print('Время выполнения - {} секунд'.format(avg_time))

time_this = TimeThis(num_runs)

@time_this
def f():
    for j in range(1000000):
        a = 1
        b = 2
        while (a + b) < 400000:
          c = a + b
          a = b
          b = c

f()