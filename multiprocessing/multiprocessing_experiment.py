import time
import multiprocessing

start = time.perf_counter()


def do_something(seconds: int) -> None:
    print(f'Sleeping for {seconds}')
    time.sleep(seconds)
    print(f'Finished sleep')


def main():
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1])
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    finish = time.perf_counter()

    print(f'Time taken to run is {round(finish - start, 2)}')


if __name__ == '__main__':
    main()
