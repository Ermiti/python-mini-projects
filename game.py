import random
modes = ["rock", "paper", "scissors"]
aiWin = 0
userWin = 0
isPlay = True
while isPlay==True :
    userAction = input("Enter a choice (rock, paper, scissors): ")
    camputerAction = random.choice(modes)
    print(f"\nYou chose {userAction}, computer chose {camputerAction}.\n")

    if userAction == camputerAction:
        print(f"Both players selected {userAction}. It's a tie!")
    elif userAction == "rock":
        if camputerAction == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif userAction == "paper":
        if camputerAction == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif userAction == "scissors":
        if camputerAction == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    
    keepGoing = input('you wanna end? (y or n)')
    if keepGoing == 'y':
        isPlay= False
        break


print("game is over")