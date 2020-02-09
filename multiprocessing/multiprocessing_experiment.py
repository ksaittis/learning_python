import concurrent.futures
import time
import multiprocessing


def do_something(seconds: int) -> str:
    print(f'Sleeping for {seconds}')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'


def main():
    start = time.perf_counter()

    use_concurrent_module()
    # use_multiprocessing_module()

    finish = time.perf_counter()

    print(f'Time taken to run is {round(finish - start, 2)}')


def use_concurrent_module() -> None:
    secs = [5, 4, 3, 2, 1]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(do_something, secs)
        for result in results:
            print(result)
        # futures = [executor.submit(do_something, second) for second in secs]

        # for f in concurrent.futures.as_completed(futures):
        #     print(f.result())


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
