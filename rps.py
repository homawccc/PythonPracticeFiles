from random import *

#comment - create 3 string variables
rock  = "rock"
paper = "paper"
scis = "scissors"
choices = [rock, paper, scis] # a list consisting of the 3 variables

upick = input("Choose: rock, paper, or scissors\n>>")
ran_num  = randint(0,2)

print(f"You chose '{upick}'.")
print("You chose '" + upick + "'.")

print(f"Computer chose '{choices[ran_num]}'.")
print(ran_num)

if upick == "rock" or upick == "Rock":
    if ran_num == 0:
        print("Tie: Rock-Rock")
    elif ran_num == 1:
        print("You Lose: Paper Covers Rock") 
    else:
        print("You Win: Rock Crushes Scissors")
       
elif upick == "paper" or upick == "Paper":
    if ran_num == 0:
        print("You Win: Paper Covers Rock")
    elif ran_num == 1:
        print("Tie: Paper-Paper") 
    else:
        print("You Lose: Scissors Cuts Paper")

elif upick == "scissors" or upick == "Scissors":
    if ran_num == 0:
        print("You Lose: Rock Crushes Scissors")
    elif ran_num == 1:
        print("You Win: Scissors Cuts Paper") 
    else:
        print("Tie: Scissors-Scissors")

else:
    print("Please choose: rock, paper or scissors!")