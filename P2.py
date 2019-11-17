def isiteven(n):
    if n%2==0:
        return True
    else:
        return False


lis=[0, 'a','b']
def fibonacci(n):
    a=1
    b=1
    l=-1
    num=a
    for z in range(1, n+1):
        if z%2==1:
            b+=a
            l=l*-1
        if z%2==0:
            a+=b
            l=l*-1
    return eval(lis[l])

def isfiboeven(n):
    return(isiteven(fibonacci(n)))

def under(n):
    z=1
    while True:
        if fibonacci(z)>n:
            return z
        z+=1

def main(n):
    ss=0
    for d in range(1,under(n)):
        if isfiboeven(d):
            ss+=fibonacci(d)
    return ss

def main2(n):
    ss=0
    for d in range(1,under(n)):
        if isfiboeven(d):
            ss+=fibonacci(d)
    return ss

if __name__=="__main__":
    print(main(10))