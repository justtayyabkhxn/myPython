opt=int(input("Choose \n1.Print odd Numbers\n2.Print Even Numbers \n"))
if opt==1:
    start=int(input("Enter Starting point: "))
    if start%2==0:
        start+=1
    end=int(input("Enter ending point: "))
    for x in range(start,end,2):
        print(x);
elif opt==2:
    start=int(input("Enter Starting point: "))
    if start%2==0:
        start+=1
    end=int(input("Enter ending point: "))
    for x in range(start,end,2):
        print(x);
    