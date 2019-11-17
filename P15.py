def main(n):
    if n==1:
        return 2
    else:
        return main(n-1)*2+2

for r in range(1, 21):
    print(main(r))

if __name__=="__main__":
    print(main(20))