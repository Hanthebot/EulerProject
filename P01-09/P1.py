def main(a):
    s=0
    for z in range(1, a):
        if z%3==0 or z%5==0:
            s+=z
    return s

def main1(a):
    s=0
    for z in range(1, a):
        if z%3==0 or z%5==0:
            s+=z
    return s

if __name__=="__main__":
    print(main(1000))
