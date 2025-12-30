#This is my project # 2

import time
def AI_assistant (moods):
    match moods:
        case 1:
            return "Study Mood On!"
        case 2:
            return "Health Mood On!"
        case 3:
            return "Tech Mood On!"
        case 4:
            return "Chill Mood On!"
def study_mood (study):
    match study:
        case "phy":
            return "It's mostly memorizing than understanding. Make one-pager sheets for each chapter for better retaining"
        case "chem":
            return "Target the orgo first. Almost 75% of the paper comes from the orgo portion."
        case "bio":
            return "Ohh this is the loved one! Make sure to read the book actively."
        case _:
            return "Not a subject"
def health_mood (sleep):
    match sleep:
        case _ if sleep < 6:
            return "Not sleeping enough"
        case _ if sleep > 8:
            return "Sleeping too much"
        case _ if 6 <= sleep <= 8:
            return "Yeah. That's the right number of hours to sleep"
        case _:
            return "Invalid"
def tech_mood (tech):
    match tech:
        case 1:
          return "Bro Code's 12 hour YT course on Python is the best place to start!"
        case 2:
            return "Go for Codecademy. You'll definitely master it if you are determined"
        case 3:
            return "FreeCodeCamp is all you need to excel"
        case _:
            return "Not a valid language"
def chill_mood (chill):
    match chill:
        case "quote":
            return "It is not a cage if you've built it"
        case "analogy":
            return "If you wanna do something, stick to it like a lizard sticks to ceiling"
        case _:
            return "Type something valid!"

print ("Wanna talk to AI Assistant?")
print ("Select a mood")
print ("1. Study")
print ("2. Health")
print ("3. Tech")
print ("4. Chill")

time.sleep (2)

user_mood = int(input ("Enter 1/2/3/4: "))
print (AI_assistant(user_mood))

time.sleep (1.5)

if user_mood == 1:
    subject = input ("Enter a subject: ")
    print (study_mood(subject))
elif user_mood == 2:
    sleep_hours = int (input ("Enter the number of whole hours u sleep: "))
    print (health_mood(sleep_hours))
elif user_mood == 3:
    print ("Enter a langauge u wanna learn.")
    print ("1. Python")
    print ("2. Cpp")
    print ("3. HTML")
    time.sleep(1)
    languages = int (input ("Enter a number 1/2/3: "))
    print (tech_mood(languages))
elif user_mood == 4:
    print ("Enter the fun thing u wanna hear.")
    print ("Quote")
    print ("Analogy")
    time.sleep(1)
    fun = input ("Enter: "). lower()
    print (chill_mood(fun))


