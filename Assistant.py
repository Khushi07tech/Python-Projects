#This is my project # 2
import time

def AI_assistant (moods):
    match moods:
        case 1:
            return "Study Mood On!📚"
        case 2:
            return "Health Mood On!👩🏻‍⚕️"
        case 3:
            return "Tech Mood On!👨🏻‍💻"
        case 4:
            return "Chill Mood On!😁"
def study_mood (study):
    match study:
        case "phy":
            return "It's mostly memorizing than understanding. Make one-pager sheets for each chapter for better retaining"
        case "chem":
            return "Target the orgo first. Almost 75% of the paper comes from the orgo portion."
        case "bio":
            return "Ohh this is the loved one! Make sure to read the book actively."
        case _:
            return "Not Found"
def health_mood (sleep):
    match sleep:
        case _ if sleep < 6:
            return "You are not sleeping enough😤"
        case _ if sleep > 8:
            return "You are sleeping too much🙄"
        case _ if 6 <= sleep <= 8:
            return "Yeah. That's the right number of hours to sleep💤"
        case _:
            return "Invalid"
def tech_mood (tech):
    match tech:
        case 1:
          return "Bro Code's 12 hour YT video on Python is the best place to start!😌"
        case 2:
            return "🧠Go for Codecademy. You'll definitely master cpp, if you are determined"
        case 3:
            return "FreeCodeCamp is all you need to excel⭐"
        case _:
            return "Not a valid language"
def chill_mood (chill):
    match chill:
        case "quote":
            return "It is not a cage if you've built it👀"
        case "analogy":
            return "If you wanna do something, stick to it like a lizard sticks to ceiling😂🦎"
        case _:
            return "Type something valid!"

is_running = True

while is_running: 
    time.sleep (1.75)
    print ("✨⭐💗✨⭐💗✨⭐💗✨⭐💗✨")
    time.sleep (0.1)
    print ("Lets talk to an AI Assistant!")
    time.sleep (0.1)
    print ("✨⭐💗✨⭐💗✨⭐💗✨⭐💗✨")
    for x in reversed(range (1, 4)):
        print (f"Starting in {x}⌛...")
        time.sleep (1)
    print ("Select a mood")
    print ("1. Study")
    print ("2. Healt" \
    "h")
    print ("3. Tech")
    print ("4. Chill")
    print ("5. Exit")
    print ("✨⭐💗✨⭐💗✨⭐💗✨⭐💗✨")
    time.sleep (1)

    user_mood = int(input ("Enter (1-5): "))
    print (AI_assistant(user_mood))

    time.sleep (0.75)

    if user_mood == 1:
        print ("Subjects:")
        print ("Phy")
        print ("Chem")
        print ("Bio")
        time.sleep(0.5)
        subject = input ("Enter a subject name: ")
        print (study_mood(subject))
    elif user_mood == 2:
        sleep_hours = int (input ("Enter the number of whole hours u sleep: "))
        print (health_mood(sleep_hours))
    elif user_mood == 3:
        print ("Enter a langauge u wanna learn.")
        print ("1. Python")
        print ("2. Cpp")
        print ("3. HTML")
        time.sleep(0.5)
        languages = int (input ("Enter a number 1/2/3: "))
        print (tech_mood(languages))
    elif user_mood == 4:
        print ("Enter:")
        print ("Quote")
        print ("Analogy")
        time.sleep(0.5)
        fun = input ("Enter: "). lower()
        print (chill_mood(fun))
    elif user_mood == 5:
        print ("Ba bye!")
        is_running = False

print ("It was so nice talking to you!")
