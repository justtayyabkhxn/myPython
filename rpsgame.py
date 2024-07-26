import random

print("-----ROCK PAPER SCISSORS-----")
score=0
hand=("Rock","Paper","Scissor")
for i in range(0,5):
    player=int(input("Choose\n1.Rock\n2.Paper\n3.Scissor\n(0 to end game)\n"))
    if player==0 :
        break
    bot=random.choices(hand)
    print(f"\nPlayer Has Choosen: {hand[player-1]}\nComputer has choosen :{bot[0]}")
    if player==1: #player has choosen rock
        if bot[0]=="Rock":
            score+=1
            print("\nIts a Draw\n")
        elif bot[0]=="Paper":
            score-=2
            print("\nBot Wins\n")
        elif bot[0]=="Scissor" :
            score+=2
            print("\nPlayer Wins\n")
    elif player==2: #player has choosen Paper
        if bot[0]=="Rock" :
            score+=2
            print("\nPlayer Wins\n")
        elif bot[0]=="Paper" :
            score+=1
            print("\nIts a Draw\n")
        elif bot[0]=="Scissor" :
            score-=2
            print("\Bot Wins\n")
    elif player==3: #player has choosen rock
        if bot[0]=="Rock" :
            score-=2
            print("\nBot Wins\n")
        elif bot[0]=="Paper":
            score+=2
            print("\nBot Wins\n")
        elif bot[0]=="Scissor":
            score+=1
            print("\nIts a Draw\n")
            

print(f"Player Score is: {score}")

        
