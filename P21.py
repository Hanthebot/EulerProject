def factor(n):
    l=[]
    for a in range(1, n):
        if n%a==0:
            l.append(a)
    return sum(l)

def main(n):
    l=[]
    for a in range(1, n):
        if a == factor(factor(a)) and a != factor(a):
            l.append(a)
            print(a)
    return sum(l)
if __name__ == '__main__':
    print(main(10000))