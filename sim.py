from random import randrange, seed, randint
seed(103)
one=list()
trial=list()
n=500000
for i in range(n):
    for j in range(4):
        o=0
        trial.append(randint(1,6))
        if trial[j]==1:
            o+=1
    one.append(o)
    trial=[]
One=list(set(one))
print(One)
count={One[i]:0 for i in range(len(One))}
for m in one:
    count[m]+=1
c=1
s=0
while c<max(One)+1:
    s+=count[c]
    c+=1
p=s/n
P=str(p)
print(" The probability of rolling a 1 on a die at least 1 time if I roll a die 4 times is about "+P)
