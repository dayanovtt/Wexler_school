import time


def count():
    end_time = time.time() + 50
    number = 0

    while time.time() < end_time:
        print(number)
        number += 1
        time.sleep(0.1)


count()