# factorial

def factorial(x):
    factorial = i = 1
    while i <= x:
        factorial = factorial * i
        i = i + 1
    print factorial

def factorial1(x):
    if x==1:
        return 1
    else: 
        return x * factorial(x-1)    
print factorial(10)

factorial(10)
factorial1(10)
