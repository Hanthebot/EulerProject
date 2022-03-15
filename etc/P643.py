def isit2n(n):
    while True:
        if n==1:
            return True
        elif n>1:
            n=n/2
        else:
            return False

def getgcd(a, b):
    for z in range(1,min(a, b)+1):
        if a % z==0 and b%z==0:
            c=z
    return(c)

def check(a,b):
    if getgcd(a,b)>1:
        return isit2n(getgcd(a,b))
    
def main(n):
    s=0
    for x in range(1,n):
        for y in range(x+1, n+1):
            if check(x, y):
                s+=1
    return s

def main643(n):
    s=0
    for x in range(1,n):
        for y in range(x+1, n+1):
            if check(x, y):
                s+=1
    return s

if __name__=="__main__":
    print(main(100000000000)%1000000007)