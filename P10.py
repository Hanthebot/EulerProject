def main(n):
    f=0
    prime=0
    primes=[]
    for z in range(2, n+1):
        for z1 in primes:
            if z%z1==0:
                f+=1
        if f==0:
            prime+=z
            primes.append(z)
        f=0
    primes=[str(g) for g in primes]
    return prime

def main10(n):
    f=0
    prime=0
    primes=[]
    for z in range(2, n+1):
        for z1 in primes:
            if z%z1==0:
                f+=1
        if f==0:
            prime+=z
            primes.append(z)
        f=0
    return prime

if __name__=="__main__":
    print(main(2000000))
    print("end!")