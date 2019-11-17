def main(n):
    b=2
    while True:
        for a in range(1, b):
            c=(a*a+b*b)**(0.5)
            if a+b+c==n:
                print(a,b,c)
                return a*b*c
        b+=1

def main9(n):
    b=2
    while True:
        for a in range(1, b):
            c=(a*a+b*b)**(0.5)
            if a+b+c==n:
                print(a,b,c)
                return a*b*c
        b+=1

if __name__=="__main__":
    print(main(1000))