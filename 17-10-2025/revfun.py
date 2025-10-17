



def read():
    a = int(input("Enter a number at least 4 digits: "))
    if len(str(a)) < 4:
        print("Invalid input! Please enter at least 4 digits.")
        return read()   
    return a

def reverse(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10
    return rev

a = read()    
r = reverse(a)
print("Original number =", a)
print("Reversed number =", r)
