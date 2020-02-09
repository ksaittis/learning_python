import concurrent.futures
import time
import multiprocessing


def do_something(seconds: int) -> str:
    print(f'Sleeping for {seconds}')
    time.sleep(seconds)
    return 'Done sleeping...'


def main():
    start = time.perf_counter()

    use_concurrent_module(10)
    # use_multiprocessing_module()

    finish = time.perf_counter()

    print(f'Time taken to run is {round(finish - start, 2)}')


def use_concurrent_module(num_processes: int) -> None:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(do_something, 1) for _ in range(num_processes)]
        for f in concurrent.futures.as_completed(futures):
            print(f.result())


def use_multiprocessing_module():
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1])
        p.start()
        processes.append(p)
    for p in processes:
        p.join()


if __name__ == '__main__':
    main()
