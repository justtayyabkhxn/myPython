from datetime import datetime

menu={"BURGER":129,
      "PIZZA":279,
      "BROWNIE":199,
      "ICE TEA":179,
      "COLD COFFEE":229,
      "HAPPY MEAL":499,
      "WHITE SAUCE PASTA":349
      }
name=input("Enter your name please:")
phno=input("Enter your phone number please:")
cart=[]
billamt=0
while True:
    print("-------|  M E N U  |-------")

    for key,value in menu.items():
        print(f"{key.center(25)} : ₹ {value}")
    print()
    print("\t** Enter q  bill amount **")
    newitem=(input("Choose: ")).upper()
    if(newitem=="Q"):
        break
    elif menu.get(newitem) is not None:
        cart.append(newitem)
        print()
        print(f"{newitem} has been added to your cart!!!!!")
        print()
        print()
        billamt+=menu[newitem]
        
print(f"Customer Name: {name}\t Customer Ph.no: {phno}\nOrder time: {str(datetime.now())}")
print()
print("---CART-->")
count=1
for cartitem in cart:
    print(f"{count}. {cartitem}")
    count+=1
print()
print(f"Total Bill Amount: ₹ {billamt}")
        

        