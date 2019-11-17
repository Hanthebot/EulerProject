def nums(n):
    l=[]
    l.append(int(n/1000))
    l.append(int(n%1000/100))
    l.append(int(n%100/10))
    l.append(int(n%10))
    return l

lis=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] 
lis2=['ten','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'] 
lis3=['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'] 
def repl(l):
    s=""
    if l[0]!=0:
        s+=" "+lis[l[0]-1]+" thousand"
    if l[1]!=0:
        s+=" "+lis[l[1]-1]+" hundred"
    if l[2]!=0:
        if l[0]>0 or l[1]>0:
            s+=" and"
        if l[2]==1:
            if l[3]!=0:
                s+=" "+lis3[l[3]-1]
            else:
                s+=" "+"ten"
        else:
            s+=" "+lis2[l[2]-1]
    if l[3]!=0 and l[2]!=1:
        if l[2]==0:
            if l[0]!=0 or l[1]!=0:
                s+=' and'
        else:
            if l[0]!=0 or l[1]!=0:
                if s.replace("and",'')==s:
                    s+=' and'
        s+=" "+lis[l[3]-1]
    print(len(s.replace(" ","")),s)
    return len(s.replace(" ",'')) 

def main(n):
    s=0
    for f in range(1,1+n):
        s+=repl(nums(f))
        #print(s) 
    return s
print(main(1000))