email=input("Hey Please enter your email: ")
index=email.index("@");

print(f"Your username is: {email[:index]} and the domain is: {email[index+1:]}")