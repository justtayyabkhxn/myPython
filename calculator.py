import math
print("-------- CALCULATOR --------")
option=1
while option!=0 :
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Check Even Odd\n6.Power\n0.Exit\n")
    option=int(input("\nChoose: "))
    if option<8:
        if option==0:
            print("Exiting.....")
        if option==1:
            a=int(input("Enter first Number "))
            b=int(input("Enter second Number "))
            add=a+b
            print(f"The sum is : {add}")
        elif option==2:
            a=int(input("Enter first Number "))
            b=int(input("Enter second Number "))
            diff=a-b
            print(f"The difference is : {diff}")
        elif option==3:
            a=int(input("Enter first Number "))
            b=int(input("Enter second Number "))
            prd=a*b
            print(f"The product is : {prd}")
        elif option==4:
            a=int(input("Enter first Number "))
            b=int(input("Enter second Number "))
            div=a/b
            print(f"The division is : {div}")
        elif option==5:
            a=int(input("Enter Number "))
            print("Even" if a%2==0 else "Odd")
        elif option==6:
            a=int(input("Enter first Number "))
            b=int(input("Enter power "))
            po=math.pow(a, b)
            print(f"The power is : {po}")
    else :
        print("Enter valid choice")

