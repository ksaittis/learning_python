import multiprocessing
import threading
import concurrent.futures
import os


def do_heavy_work():
    print(f'Executing method in thread {threading.get_ident()} on process {os.getpid()}')


def one_process():
    for _ in range(50):
        t = threading.Thread(target=do_heavy_work(), args=())
        t.start()


def use_threads():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(25):
            executor.submit(do_heavy_work)


def use_processes():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(25):
            executor.submit(do_heavy_work)


def use_processes_and_threads():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for _ in range(2):
            executor.submit(use_threads)


if __name__ == '__main__':
    use_processes_and_threads()
    # use_threads()
    # use_processes()
