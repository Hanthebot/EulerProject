def main(n):
    s=1
    while True:
        l=[]
        for r in range(1,n+1):
            if s%r!=0:
                s+=1
                break
            l.append(r)
        if len(l)==n:
            return s

def main5(n):
    s=1
    while True:
        l=[]
        for r in range(1,n+1):
            if s%r!=0:
                s+=1
                break
            l.append(r)
        if len(l)==n:
            return s

if __name__=="__main__":
    print(main(20))