from time import sleep
from threading import Thread


# My thread
class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time

        super().__init__()

    # run method
    def run(self):
        sleep(self.time)
        print(self.text)


thread_1 = MyThread('Thread 1', 2)
thread_1.start()

thread_2 = MyThread('Thread 2', 5)
thread_2.start()

thread_3 = MyThread('Thread 3', 1)
thread_3.start()

for i in range(10):
    print(i)
    sleep(1)
