import time
import random
def delay(x):
    time.sleep(x)
win = False
right_colours = 0
wrong_position = 0
while win==False:
    # Intoruction 🔽
    print("Welcome to Master Mind Game !")
    delay(1.2)
    print("Let me think")
    delay(1.3)
    print("Hmmmm")
    colours = ["red", "blue", "green", "yellow", "white", "black"]
    guess = []
    for i in range ( 1 , 5 ):
        guess.append(random.choice(colours))
    display = ["X" , "X" , "X" , "X"]
    delay(1.5)
    print("Ok I'm ready , btw my guess is composed of 4 colours")
    delay(1)
    print("What's your first guess?")
    # Playing phase 🔽
    while win == False :
        print("")
        answer = str(input()).lower().split()
        for i in range(4):
            for j in range(4):
                if answer[i] == guess[j] and i == j :
                    right_colours += 1
                elif answer[i] == guess[j] and i != j :
                    wrong_position +=1
        if answer == guess :
            print(f"\nYou Won , my chosen colours were {" ".join(guess)} ")
            win = True
            right_colours , wrong_position = 0,0
        elif right_colours >0 and wrong_position>0 :
            print(f"\n{right_colours} colours in the right position")
            print(f"{wrong_position} correct colour but in the wrong position")
            right_colours , wrong_position = 0,0
        elif right_colours >0 :
            print(f"\n{right_colours} colours in the right position")
            right_colours = 0
        elif wrong_position>0:
            print(f"\n{wrong_position} correct colour but in the wrong position")
            wrong_position = 0