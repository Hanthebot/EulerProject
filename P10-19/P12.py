import time
import math

#revised on 2022/07/24 22:53

def fo2(a):
    return "{0:.2f}".format(a)

def inTime(t):
    return f"{int(t / 3600)}:{int(t % 3600 / 60)}:{fo2(t % 60)}s"

def evenDivide(n):
    if n % 2:
        return int(n / 2)
    else:
        return int((n - 1) / 2)

def getFactors(n):
    fac = [num for num in range(1, int(math.sqrt(n)) + 1) if n % num == 0]
    if fac[-1] == math.sqrt(n):
        return 2 * len(fac) -1
    else:
        return 2 * len(fac)

def triangleNumber(n):
    return int((n * (n + 1)) / 2)

def main(target, t = time.time()):
    divisors = [0]
    i = 0
    number = 0
    while max(divisors) < target:
        i += 1
        number += i
        divisors.append(getFactors(number))
        print(f"i: {i}, Target: {target}, Latest: {max(divisors)}, Consumed time: {inTime(time.time() - t)}     ", end="\r")
    return number

if __name__=="__main__":
    time_i = time.time()
    print("\n", main(500, time_i))
    print(f"Done, took: {inTime(time.time() - time_i)}      ")