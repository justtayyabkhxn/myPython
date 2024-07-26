import os
import authentication as loginuser
user = loginuser.userid
os.system('cls')



Tayyab = {
    "full name": "Tayyab Khan",
    "father name": "Tajuddin",
    "mother name": "Shazia Khan",
    "qualification": "Physics Graduate",
    "age": 21,
    "weight": 73.25,
    "relationship status": "Soon to be married",
    "dob": "27/05/2002",
    "nationality": "Indian"
}
Zoya = {
    "full name": "Zoya Khan",
    "father name": "Saad Khan",
    "mother name": "Firdous Asrar",
    "qualification": "Psychology Undergrad",
    "age": 21,
    "weight": 58.25,
    "relationship status": "Soon to be married",
    "dob": "01/04/2003",
    "nationality": "Indian"
}
Anas = {
    "full name": "Anas Abrar",
    "father name": "Abrar Hasan",
    "mother name": "Ruzda",
    "qualification": "CS Graduate",
    "age": 22,
    "weight": 95.25,
    "relationship status": "Divorced",
    "dob": "17/01/2002",
    "nationality": "Indian"
}
Rayyan = {
    "full name": "Syed Rayyan Ali",
    "father name": "Rayyan ke papa",
    "mother name": "Rayyan ke muma",
    "qualification": "Physics Graduate",
    "age": 22,
    "weight": 85.25,
    "relationship status": "Randwa",
    "dob": "31/03/2001",
    "nationality": "Indian"
}

while True:
    print("<--- LOGIN SUCCESSFUL --->")
    print(f"Welcome {user}")
    opt = input("\nChoose the detail you want to access: \nFull Name\nFather Name\nMother Name\nQualification\nAge\nWeight\nRelationship Status\nDOB\nNationality\n or Enter quit to quit: ").lower()
    chosen = opt.capitalize()
    if opt == "quit":
        break
    user_data = globals().get(user)  # Get the dictionary associated with the user
    if user_data:
        os.system('cls')
        
        print(f"\n--->{user}'s {chosen} is : {user_data.get(opt)}\n")
    else:
        print("\nInvalid option. Please try again.")

print("<----- THANKS FOR THE VISIT ----->")
