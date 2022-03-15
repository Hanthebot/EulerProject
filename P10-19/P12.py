def getfac(n):
    fac=[]
    for a in range(1,n+1):
        if n%a==0:
            fac.append(a)
    return fac

def tri(n):
    return int((n*n+n)/2)

def main(h):
    d=[]
    z=1
    while len(getfac(tri(z)))<h:
        z+=1
        d.append(len(getfac(tri(z))))
        print(max(d), end="\r")
    return tri(z)

if __name__=="__main__":
    print(main(500))