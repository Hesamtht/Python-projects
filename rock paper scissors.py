import random

print("Hi welcome to this game !")
choosen_list = ["r" , "p" , "s"]
computer = random.choice(choosen_list)
user = input("Enter your option 'r or p or s' :")

if user not in choosen_list:
    print("Please inter your option correctly !")
if  computer == user:
    print("Tie !")

elif user == "r":
    if computer == "p":
        print("paper covers rock so user LOST")
    else:
        print("rock break scissors so you WIN !")

elif user == "s":
    if computer == "r":
        print("rock break scissors so user LOST")
    else:
        print("scissor cut the paper so you WIN !")

elif user == "p":
    if computer == "s":
        print("scissor cut the paper so you LOST")
    else:
        print("paper covers rock so you WIN !")