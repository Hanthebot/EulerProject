def getfac(n):
    factors=[]
    for LL in range(2):
        for z in reversed(range(100, 1000)):
            if n%z==0:
                factors.append(int(z))
                n=n/z
            if int(n)==1:
                return factors
    if len(factors)<2:
        return False
    if int(n)!=1:
        factors[factors.index(min(factors))]=min(factors)*n
    if len(str(factors[0]))!=3 or len(str(factors[1]))!=3:
        return False
    return factors


def isitrec(l):
    l=str(l)
    k=0
    for L in range(len(l)):
        if l[L]==l[-L-1]:
            k+=1
    if k==len(l):
        return True
    else:
        return False

def main(n):
    for h in reversed(range(1, n+1)):
        if isitrec(h):
            f=getfac(h)
            if f:
                print(h)

def main4(n):
    for h in reversed(range(1, n+1)):
        if isitrec(h):
            f=getfac(h)
            if f:
                print(h)

if __name__=="__main__":
    print(main(998001))