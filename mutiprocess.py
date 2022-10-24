import multiprocessing as mp
import time
import math
from unicodedata import numeric
from connection import connection
from integrated import GenerateUI
a  =[]

b = []

c = []

def calc1(numbers):
        for numer in numbers:
            a.append(math.sqrt(numer**3))


def calc2(numbers):
        for numer in numbers:
            a.append(math.sqrt(numer**4))


def calc3(numbers):
        for numer in numbers:
            a.append(math.sqrt(numer**5))

if __name__ == '__main__':
    number_list = list(range(500))

    start = time.time()
    end = time.time()
    print("CPU Cores: ", mp.cpu_count())
    p1 = mp.Process(target=calc1, args=(number_list,))
    p4 = mp.Process(target=GenerateUI, args=())
    p5 = mp.Process(target=connection, args=())
    
    p1.start()
    p4.start()
    p5.start()


    end = time.time()
    print("mutiprocessing time: ", end-start)
    
    start = time.time()
    calc1(number_list)

    end = time.time()

    print(end-start)