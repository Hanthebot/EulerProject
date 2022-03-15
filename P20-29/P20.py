def fac(n):
    s=1
    for a in range(1, n+1):
        s*=a
    return s

def disum(n):
    s=0
    for a in str(n):
        s+=int(a)
    return s

def main(n):
    return disum(fac(n))

if __name__=="__main__":
    print(main(100))