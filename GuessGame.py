#A number guessing game in python
import random
import time


#Introduction
print ("Welcome to the grand number guessing game in python!")
name = input ("NAME: "). title ()

print (f"Hello {name}! Gotcha challenge me? Let's jump straight into the game then. Remember you have 10 chances to guess the right answer only!")
time.sleep (0.5)
for x in reversed (range (0, 4)):
    print (x)
    time.sleep (1)

#Selecting Difficulty level
print ("Select a difficulty level")
print ("A. Easy (1-50)")
print ("B. Hard (1-100)")
diff_level = input ("Just type in A or B: "). upper ()
#making sure user type valid input
while not diff_level == "A" and not diff_level == "B":
    print("Please type only 'A' or 'B'!")
    diff_level = input("Type Again: ").upper()
if diff_level == "A":
    lowest = 1
    highest = 50
elif diff_level == "B":
    lowest = 1
    highest = 100

computer = random.randint (lowest, highest)
special_num = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
specials = []
guesses = 0
score = 0
total = 0
attempts = 10
is_running = True

#defining the hint function
def hint ():
    if computer % 2 == 0:
        print ("I thought of an even number!")
    elif computer % 2 == 1:
        print ("I thought of an odd number!")
#defining the time function
def t_sleep ():
    for x in range(1, 2):
        print("******")
        time.sleep(1)

for x in range (1, 2):
    print ("***We are almost all set***")
    time.sleep (2)

#Starting the game
while is_running:
    guess = (input ("Guess what did i thought: "))
    while not guess.isdigit ():
        print (f"Only Digits in the range {lowest} - {highest} are acceptable")
        guess = (input("Guess what did i thought: "))
    else:
        guess = int (guess)
        guesses += 1
        attempts -= 1
        time.sleep (1)

        if attempts == 0:
            print("SORRY. Game Over! You are out of attempts")
            is_running = False
        else:
            #Checking if the user collects special items
            if guess in special_num:
                    special_items = random.choice(["golden egg", "key", "map", "potion", "med", "tools"])
                    specials.append(special_items)
                    print(f"You've got a: {special_items}")
                    time.sleep (1)
                    attempts += 2
                    print (f"You've got two extra attempts.")
                    time.sleep(1)
                    print (f"Current inventory: {specials}")

            #If user's and computer's answer doesnt match
            if guess != computer:
                 if guess < lowest or guess > highest:
                     print ("Not in range")
                 elif (guess < computer):
                      print ("That was lesser")
                 elif guess > computer:
                      print ("That was higher")
                 #Giving the user the option to get a hint after 8 wrong guesses
                 if guesses > 8:
                     t_sleep()
                     hints = input("Want a hint?(Yes/No): ")
                     if hints == "yes":
                          hint()
                     else:
                          pass

        #If user's answer is correct
            elif guess == computer:
                print ("Exactly!")
                score += 1
                time.sleep (1)
        #the play again code
                repeat = input ("Wanna play Again? (Yes/No): ")
                if not repeat == "yes":
                    time.sleep (2)
                    print ("okayyy then ba bye!")
                    total += score
                    t_sleep ()
                    print (f"Your total score is {total}")
                    t_sleep ()
                    print (f"You guessed {guesses} times")
                    t_sleep ()
                    print (f"The unique items you collected were: {specials}")
                    t_sleep ()
                    is_running = False
                else:
                    computer = random.randint (lowest, highest)
                    guesses = 0
                    specials = []
                    attempts = 10
            else:
                print ("May be u typed something invalid!!")
#the loop exits forever
print ("Thankew for playing with us !")


