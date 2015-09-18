import os
import time
import threading

######################
# Constant Variables #
######################

# Set this to the directory + file name of an alarm sound
# Any music file type can be used
ALARM_SOUND = ""

# Set this to the directory + file name of an alarm list
# Any plain text file type can be used
ALARM_LIST = "alarmList.txt"

###########
# Classes #
###########

class Alarm(threading.Thread):
    def __init__(self, startHour, startMinute):
        threading.Thread.__init__(self)
        self.startHour = startHour
        self.startMinute = startMinute

    # Main routine of alarm clock
    # When it's time for the alarm, shutdown the computer
    def run(self):
        print(time.strftime("Started on: %H:%M"))
        print("Alarm set for: {:02}:{:02}".format(self.startHour, self.startMinute))

        while True:
            localTime = time.localtime()
            if localTime.tm_hour == self.startHour and localTime.tm_min == self.startMinute:
                print("It's time to sleep...")
                os.startfile(ALARM_SOUND)

                # Shutdown Windows via Command Prompt
                os.system("shutdown /s /t 1800 /c \"Time to Sleep...\"")
                return

#############
# Functions #
#############

################
# Main Routine #
################

# Check if run as a script (not imported by another module), execute the following codes
if __name__ == "__main__":
    print("PyAlarm")
    print("By: Alfredo Morgen")
    print("")
        
    choice = 0
    while choice != 3:
        try:
            with open(ALARM_LIST, 'r') as alarmFile:
                hour, minute = [int(x) for x in alarmFile.readline().split()]
                alarm = Alarm(hour, minute)
        except FileNotFoundError:
            hour = -1
            minute = -1

        if hour == -1 and minute == -1:
            print("Alarm has not been set")
        else:
            print("Alarm set for: {:02}:{:02}".format(hour, minute))

        print("1. Turn on alarm")
        print("2. Configure alarm")
        print("3. Exit")
        print("")

        try:
            choice = int(input("Choice: "))
        except Exception as e:
            print("Please input numbers only")

            input("\nPress enter to continue...")

        if choice == 1:
            if hour == -1 and minute == -1:
                print("Alarm has not been set")
                print("Please set it first...")
            else:
                alarm.start()
        elif choice == 2:
            try:
                hour, minute = [int(x) for x in input("Input alarm time (in 'HH MM' format): ").split()]
                with open(ALARM_LIST, 'w') as alarmFile:
                    alarmFile.write("{} {}\n".format(str(hour), str(minute)))
                print("Alarm has been successfully added!")
            except Exception as e:
                print("Error reading time")
                print("Please input only numbers in 'HH MM' format (with space in between)")
                print("Example: '22 00', '12 30', or '07 05'")

            input("\nPress enter to continue...");
        elif choice == 3:
            pass
        else:
            print("Invalid input...")

        os.system("cls")
