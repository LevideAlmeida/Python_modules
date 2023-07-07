from time import sleep
from threading import Thread
from threading import Lock


class Tickeds:
    def __init__(self, stock):
        self.stock = stock
        self.lock = Lock()

    def buy(self, quantity):
        self.lock.acquire()

        if self.stock < quantity:
            print('Not enough tickets')
            self.lock.release()
            return

        sleep(1)

        self.stock -= quantity
        print(
            f'you bought {quantity} tickts. '
            f'There are {self.stock} tickets in stock')

        self.lock.release()


if __name__ == '__main__':
    tickets = Tickeds(10)

    for i in range(1, 10):
        thread = Thread(target=tickets.buy, args=(i,))
        thread.start()

    print(tickets.stock)
