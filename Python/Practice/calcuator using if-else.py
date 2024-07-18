print("Hello, please enter numbers now:")

a = int(input())

print("a is",a)

b = int(input())

print("b is",b)

print("The numbers are: ",a,",",b)

print("Select an operation: add (1), minus (2), multiply (3), divide (4)")

do = int(input())

if do == 1:
    print(a+b)
    
elif do == 2:
    print(b-a)
    
elif do == 3:
    print(a*b)
    
elif do == 4:
    print(a/b)
    
else :
    print("wrong choice, restart program")
    