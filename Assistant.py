#TO DO:
#Points in health never display
#there's a bug in the health mood

import random
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
        case 5:
            return "Ba bye!"
        case _:
            return "Mood not found"
def study_mood (study):
    match study:
        case "phy":
            return "It is mostly memorizing than understanding. Make one-pager sheets for each chapter for better retaining"
        case "chem":
            return "Target the orgo first. Almost 75% of the exam usually comes from the orgo portion."
        case "bio":
            return "Ohh this is the loved one! Make sure to read the book actively."
        case _:
            return "Subject not found"
def health_mood (sleep, points):
    match sleep:
        case _ if sleep < 6:
            return "You are not sleeping enough😤"
            points += 0
        case _ if sleep > 8:
            return "You are sleeping too much🙄"
            points += 0
        case _ if 6 <= sleep <= 8:
            return "Yeah. That's the right number of hours to sleep💤"
            points += 2
        case _:
            return "Invalid"
def exercise_hours(exercise, points):
    match exercise:
        case _ if exercise == 1:
            print ("Superb! Your routine should ideally be: stretches in the morning or evening and intense exercises on alternate day")
            points += 3
        case _ if exercise == 2:
            print ("Good! but try at least doing body stretches everyday (morning or evening whatever suits you")
            points += 2
        case _ if exercise == 3:
            print ("Hmm... not good enough. Try finding a gym/exercise buddy who can remind you to stay consistent")
            points += 1
        case _ if exercise == 4:
            print ("Well, you're in the worse category. Move your body, don't stay idle. If you keep being in this categoy, then you are going to lament this in the long run.")
            points += 0
        case _:
            print ("Invalid")
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
def participated_hackathons(hackathons):
    match hackathons:
        case _ if hackathons > 5:
            print ("You are in a good place. Keep pushing forward!")
        case _ if hackathons < 5:
            print ("Umm.. May be try out devpost, they host a lot of hackathons")
        case _:
            print ("Not a valid input")
def chill_mood (chill):
    match chill:
        case "quote":
            quotes = ["Collect moments, not things.",
                      "Small steps every day add up to big results.",
                      "Be the energy you want to attract.",
                      "Happiness is an inside job.",
                      "Don’t wait for opportunity, create it.",
                      "It is not a cage if you've built it"]
            comp_quotes = random.choice(quotes)
            return comp_quotes
        case "analogy":
            analogies = ["If you wanna do something, stick to it like a lizard sticks to ceiling",
                         "Be as persistent as a 'Low Battery' notification when you’re at 1%.",
                         "Focus on your goals like a cat focuses on the tiny red dot of a laser pointer.",
                         "Commit to your work like a toddler commits to a permanent marker and a white wall.",
                         "If you have a dream, guard it like a squirrel guards its last nut."]
            comp_analogies = random.choice (analogies)
            return comp_analogies
        case _:
            return "Type something valid!"
def main ():

    is_running = True

    while is_running:
        time.sleep (1.75)
        print ("✨⭐💗✨⭐💗✨⭐💗✨⭐💗✨")
        time.sleep (0.4)
        print ("Lets talk to an AI Assistant!")
        time.sleep (0.4)
        print ("✨⭐💗✨⭐💗✨⭐💗✨⭐💗✨")
        for x in reversed(range (1, 4)):
            print (f"Starting in {x}⌛...")
            time.sleep (1)
        print ("Select a mood")
        print ("1. Study")
        print ("2. Health")
        print ("3. Tech")
        print ("4. Chill")
        print ("5. Exit")
        print ("✨⭐💗✨⭐💗✨⭐💗✨⭐💗✨")
        time.sleep (1)

        user_mood = int(input ("Enter (1-5): "))
        print (AI_assistant(user_mood))

        time.sleep (0.75)

        if user_mood == 1:
            print ("What among the following you need help with?")
            print ("1. Subject Related Tips")
            print ("2. Time Management")
            print ("3. Cope up stress")
            study_question = int(input ("Enter (1-3): "))
            if study_question == 1:
                print ("Subjects:")
                print ("Phy")
                print ("Chem")
                print ("Bio")
                time.sleep(0.5)
                subject = input ("Enter a subject name: ")
                print (study_mood(subject))
            elif study_question == 2:
                study_hours = int(input ("How many hours do you study a day"))
                if 3 < study_hours <= 5:
                    print (f"Remember Quality > Quantity. If you make the best out of these {study_hours} hours then this is more than enough!")
                elif study_hours < 3:
                    print ("Try studying a bit more everyday. Consistency beats intensity!")
                elif study_hours > 5:
                    print (f"Try reducing the amount of hours you spend studying. Studying {study_hours} a day is unhealthy!")
                else:
                    print ("Invalid input")
            elif study_question == 3:
                stress = input ("Do you often have to go through academic stress? (Yes/No): "). lower ()
                if stress == "yes":
                    print ("The main causes of academic stress among students are:")
                    print ("1. Long hours studying")
                    print ("2. Perfectionism")
                    print ("3. Trying to impress parents and others")
                    print ("4. Cutting yourself completely off social life")
                    print ("5. Deciding not to 'waste' time in the little happy moments")
                    print ("To cope up with the stress, try working on these. You'll see yourself more happy, focused and healthier too.")
                elif stress == "no":
                    print ("Keep Pushing champ!")
                else:
                    print ("Invalid input")
        elif user_mood == 2:
            points = 0
            sleep_hours = int (input ("Enter the number of whole hours u sleep: "))
            print (health_mood(sleep_hours))

            print ("How often do you exercise?")
            print ("1. Everyday")
            print ("2. Alternate days")
            print ("3. Few times in a month")
            print ("4. I don't")
            exercise = int(input ("Select (1-4): "))
            print (exercise_hours(exercise))

            print (f"Your total health points are {points}/5")
        elif user_mood == 3:
            print ("Enter a langauge u wanna learn.")
            print ("1. Python")
            print ("2. Cpp")
            print ("3. HTML")
            time.sleep(0.5)
            languages = int (input ("Enter a number 1/2/3: "))
            print (tech_mood(languages))

            hackathons = int(input ("How many hackathons did you ever participated in: "))
            print (participated_hackathons(hackathons))
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

if __name__ == '__main__':
    main ()