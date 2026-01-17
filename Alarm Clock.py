import time
import winsound
import datetime


def set_alarm (alarm_time):
    print (f"Alarm set for ⌚⭐{alarm_time}")
    print("😍✨🎇🎀😍✨🎇🎀😍✨🎇🎀😍✨🎇🎀")
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().time()
        print (current_time.strftime("%H:%M:%S"))
        time.sleep (1)

        if current_time >= alarm_time:
            is_running = False
            winsound.Beep(1500, 500)
            print ("WAKE UP!😉")
            time.sleep(0.5)
            print (f"'{message}'")
            time.sleep(0.5)
            print("😍✨🎇🎀😍✨🎇🎀😍✨🎇🎀😍✨🎇🎀")

            again = input ("Want to set another alarm? (y/n): ").lower()
            if again != "y":
                break

if __name__ == '__main__':

    print("🎀Welcome to the 'Alarm Clock'🎀")
    time.sleep (1)
    message = input("What message you want to see when the alarm rings👀?: ").title()

    while True:
        try:
            alarm_time_in = input ("✨Enter time(HH:MM:SS): ")
            split = alarm_time_in.split(":")
            alarm_time_numeric = [int(x) for x in split]
            alarm_time = datetime.time(alarm_time_numeric[0], alarm_time_numeric[1], alarm_time_numeric[2])
            set_alarm(alarm_time)
        except ValueError:
            print ("Please write appropriate values😒")
        except IndexError:
            print ("Please write time in the format HH:MM:SS🙄")

