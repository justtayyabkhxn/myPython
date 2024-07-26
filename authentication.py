users={
    "Tayyab":7267,
    "Zoya":1234,
    "Anas":2580,
    "Rayyan":0000
}
flag=False
print("----WELCOME TO LOGIN PAGE----")
while True:
    userid=input("\nEnter your userID(First Name)👤: ")
    userid=userid.capitalize()
    if(users.get(userid)):
        print("\nUser details found!! Now Enter your password 🔑")
        break
    else: print("\nInvalid user!! Enter username again")
while True:
    passwrd=int(input(f"\nHey {userid} enter your 4 digit password: "))
    if(users[userid]==passwrd):
        print("\nCorrect Password!! Now you can access your details")
        break
    else: print("\nIncorrect Password! Please try again")


    
