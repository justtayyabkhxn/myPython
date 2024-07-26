import random

score=0
print("-----WELCOME TO GAME-----")
while True:
    num=int(input("Guess a number between 1-10 or Enter 0 to exit"))
    ans=random.randint(1,10)
    if num==0:
        print(f"The score is: {score}")
        break
    elif num==ans :
        print(f"Right Answer!! The number is {ans}")
        score+=1
    else:
        print(f"Wrong Answer!! The number is {ans}")
        score-=1
