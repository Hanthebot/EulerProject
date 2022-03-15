A = eval(open("./data/P22.txt","r").read())
A = sorted(A)
b = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b = [B.upper() for B in b]
s=0
for a in A:
    n=0
    for B in a:
        n+=b.index(B)+1
    n=n*(A.index(a)+1)
    s+=n
    
print(s)