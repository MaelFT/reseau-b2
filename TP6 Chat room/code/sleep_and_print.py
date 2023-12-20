import time

def sleep_and_print():
    for i in range(10):
        print(i)
        time.sleep(0.5)

if __name__ == '__main__':
    start = time.perf_counter()
    sleep_and_print()
    sleep_and_print()
    stop = time.perf_counter()
    print('Done in {} seconds'.format(stop - start))
