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
# Any plaintext file type can be used
ALARM_LIST = "alarmList.txt"

####################
# Global Variables #
####################

alarmList = []

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
        while True:
            localTime = time.localtime()
            if localTime.tm_hour == self.startHour and localTime.tm_min == self.startMinute:
                print("It's time to sleep...")
                os.startfile(ALARM_SOUND)

                # Shutdown Windows via Command Prompt
                os.system("shutdown /s /t 1800 /c \"Time to Sleep...\"")
                return

################
# Main Routine #
################

# Check if run as a script (not imported by another module), execute the following codes
if __name__ == "__main__":
    print("PyAlarm")
    print("By: Alfredo Morgen")
    print("")
    
    # Open ALARM_LIST and get all the alarms
    try:
        with open(ALARM_LIST, 'r') as alarmFile:
            for line in alarmFile:
                hour, minute = [int(x) for x in line.split()]
                newAlarm = Alarm(hour, minute)
                newAlarm.start()
                alarmList.append(newAlarm)
    except FileNotFoundError:
        hour = -1
        minute = -1

    choice = 0
    while choice != 2:
        print("PyAlarm")

        # Print all the alarms
        if hour == -1 and minute == -1:
            print("Alarm has not been set")
        else:
            for alarm in alarmList:
                print("Alarm set for: {:02}:{:02}".format(alarm.startHour, alarm.startMinute))

        print()
        print("1. Add new alarm")
        print("2. Exit")
        print()

        try:
            choice = int(input("Choice: "))
        except Exception as e:
            print("Please input numbers only")
            print()
            input("Press enter to continue...")

        if choice == 1:
            try:
                hour, minute = [int(x) for x in input("Input alarm time (in 'HH MM' format): ").split()]
                assert hour >= 0 and hour <= 23
                assert minute >= 0 and minute <= 59

                newAlarm = Alarm(hour, minute)
                alarmList.append(newAlarm)
                newAlarm.start()

                with open(ALARM_LIST, 'w') as alarmFile:
                    for alarm in alarmList:
                        alarmFile.write("{} {}\n".format(str(alarm.startHour), str(alarm.startMinute)))

                print("Alarm has been successfully added!")
            except Exception as e:
                print("Error reading time")
                print("Please input only numbers in 'HH MM' format (with space in between)")
                print("Example: '22 00', '12 30', or '07 05'")

            input("\nPress enter to continue...");
        elif choice == 2:
            pass
        else:
            print("Invalid input...")

        os.system("cls")
