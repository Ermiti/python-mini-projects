import random
import re
isPlay = True
guessedNum = "hi"

def gettingEnd():
    print("ended")
    isPlay = False 

def justNumber(Value):
        if re.search(r"\d{1,2}", Value) == None: 
            guessedNum = input("enter NUMBER (just number is acceptable): ")

tryingTimes = 0
    
while isPlay:
    selectedNum = random.randint(1, 100)

    guessedNum = input("please enter your guess number amung 1 to 100 : (enter exit to end)")
    if guessedNum == 'exit':
        gettingEnd()
        break

    justNumber(guessedNum)
    while int(guessedNum) != int(selectedNum):
            tryingTimes = tryingTimes + 1    
            if int(guessedNum) < int(selectedNum):
                guessedNum = input("selected number is bigger. please choose another number: ")
            else:
                guessedNum = input("selected number is smaller. please choose another number: ")
         

    if int(guessedNum) == int(selectedNum): 
        print(f"you have tried for {tryingTimes} times and the number was {selectedNum}")
        isContinue = input("you win! wanna play again? (y/n)")
        if isContinue == 'n':
            gettingEnd()
            break
                 

     
