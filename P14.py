def step(n):
    s=0
    while True:
        if n==1:
            return s
        elif n%2==0:
            n=n/2
            s+=1
        elif n%2==1:
            n=3*n+1
            s+=1

lis=[]
for k in range(1, 1000000):
    lis.append(step(k))
print(lis.index(max(lis))+1,"-",max(lis))