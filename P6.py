def foreach(n):
    s=0
    for f in range(1, n+1):
        s+=f*f
    return s
    
def atall(n):
    s=0
    for f in range(1, n+1):
        s+=f
    s=s*s
    return s
    
def main(n):
    return abs(foreach(n)-atall(n))

def main6(n):
    return abs(foreach(n)-atall(n))

if __name__=="__main__":
    print(main(100))