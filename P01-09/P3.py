def Punder(n):
    f=0
    primes=[]
    for z in range(2, n+1):
        for z1 in range(2, z):
            if z%z1==0:
                f+=1
        if f==0:
            primes.append(z)
        f=0
    return primes
       
       
       
def getPfactors(n):
    factors=[]
    while int(n)!=1:
        for z in range(2, int(n/2)+2):
            if n%z==0:
                factors.append(int(z))
                n=n/z
                print(z)
            if int(n)==1:
                return factors
            
    return factors

def getfactors(n):
    k=int(n/2)
    f=0
    for z in range(2, k+1):
        for z1 in range(2, z):
            if z%z1==0:
                f+=1
        if f==0:
            
            factors=[]
            if n%z==0:
                factors.append(int(z))
                n=n/z
                factors=[str(factor) for factor in factors]
                if eval("*".join(factors))==n:
                    return sorted(factors)
        f=0

def main(n):
    return getfactors(n)[-1]

def main3(n):
    return getfactors(n)[-1]

if __name__=="__main__":
    print(main(600851475143))