def main(n):
    f=0
    primes=[]
    z=2
    while len(primes)<n+1:
        for z1 in range(2, z):
            if z%z1==0:
                f+=1
        if f==0:
            primes.append(z)
        f=0
        z+=1
    return primes[n-1]

def main7(n):
    f=0
    primes=[]
    z=2
    while len(primes)<n+1:
        for z1 in range(2, z):
            if z%z1==0:
                f+=1
        if f==0:
            primes.append(z)
        f=0
        z+=1
    return primes[n-1]

if __name__=="__main__":
    print(main(10001))