import time

#revised on 2022/07/24 22:53

def fo2(a):
    return "{0:.2f}".format(a)

def inTime(t):
    return f"{int(t / 3600)}:{int(t % 3600 / 60)}:{fo2(t % 60)}s"

def main(n, t = time.time()):
    print(f"n: {n}, Consumed time: {inTime(time.time() - t)}", end = "\r")
    if n == 1:
        return 2
    else:
        return main(n - 1) * 2 + 2

if __name__=="__main__":
    time_i = time.time()
    print("\n", main(20))
    print(f"Done, took: {inTime(time.time() - time_i)}")