a=input("enter a file with extension(.jpg)")
b=a[::-1]
c=b.index(".")
a=b[:c]
print("the file type is: ", a[::-1])
