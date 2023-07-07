from time import sleep
from threading import Thread


def wait(text, time):
    sleep(time)
    print(text)


thread = Thread(target=wait, args=("hello world!", 5))
thread.start()

while thread.is_alive():
    print('waiting the thread...')
    sleep(1)

print('\n \nTHREAD END!!!')
