
word=[]
n=int(input("how many words you want to enter"))
for i in range(n):
    a=input("enter the word of index[(i)]: ")
    word.append(a)

    
def length(word):
    l=0
    
    for i in word:
            if len(i) > l:
                
                b=i
                l=len(i)
                
    print(l)
    print(b)
    



length(word)
