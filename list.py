li=[1,2,3,4,5]
l=[6,5,4,7,2]


p=len(li)
q=len(l)
print(li)
print(l)
if (p==q):
    print("both lists are of same size",p)
else:
    print("the size of list are",+p,"and",q)

sum1=0
sum2=0

for i in li:
    sum1=sum(li)
for j in l:
    sum2=sum(l)

if(sum1==sum2):
    print("the two list has the same sizeof: ",sum1)
else:
    print("the sum of the list are: ",+sum1, "  and:  ",sum2)

for i in li:
    for j in l:
        if(i==j):
            print("list has the same elements",i)
            


