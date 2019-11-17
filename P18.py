A="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
A=A.split("\n")
A=[a.split(" ") for a in A]
A=[[int(b) for b in a] for a in A]
N=[]
def main():
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            for g in range(2):
                                for h in range(2):
                                    for i in range(2):
                                        for j in range(2):
                                            for k in range(2):
                                                for l in range(2):
                                                    for m in range(2):
                                                        for n in range(2):
                                                            for o in range(2):
                                                                P=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
                                                                N.append(sum([A[p][sum(P[0:p])] for p in range(len(P))]))
    return N
print(max(main()))