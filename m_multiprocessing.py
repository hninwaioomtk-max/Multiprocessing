import time
from multiprocessing import Process

def addition():
    a = 10
    b = 5
    print("Addition start")
    time.sleep(2)
    print("Addition result:", a + b)
    print("Addition finished")


def subtraction():
    a = 10
    b = 5
    print("Subtraction start")
    time.sleep(2)
    print("Subtraction result:", a - b)
    print("Subtraction finished")


def multiplication():
    a = 10
    b = 5
    print("Multiplication start")
    time.sleep(2)
    print("Multiplication result:", a * b)
    print("Multiplication finished")


if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=addition)
    p2 = Process(target=subtraction)
    p3 = Process(target=multiplication)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    end = time.time()

    print("Total time:", end - start)

