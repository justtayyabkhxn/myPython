def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def product(x,y):
    return x*y

def division(x,y):
    return x/y

def remainder(x,y):
    return x%y



print("----CALCULATOR----")
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))

choice=int(input("Choose: \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Find Remainder"))
if choice==1:
    print(addition(x,y))
elif choice==2:
    print(subtraction(x,y))
elif choice==3:
    print(product(x,y))
elif choice==4:
    print(division(x,y))
elif choice==5:
    print(remainder(x,y))



