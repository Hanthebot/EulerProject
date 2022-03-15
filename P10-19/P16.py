def plus(l):
    s=0
    for d in str(l):
        s+=int(d)
    return s

def get2n(n):
    s=1
    for r in range(n):
        s*=2
    return s

def main(n):
    return plus(get2n(n))

print(main(1000))