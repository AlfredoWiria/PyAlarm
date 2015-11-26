import os
import time
import threading

####################
# Global Variables #
####################

alarmList = []

###########
# Classes #
###########

class AlarmFile:
    def __init__(self, fileDirectory):
        self.fileDirectory = fileDirectory

    def alarmFileOpen(self):
        global alarmList

        try:
            with open(self.fileDirectory, 'r') as alarmFile:
                for line in alarmFile:
                    hour, minute = [int(x) for x in line.split()]
                    newAlarm = Alarm(hour, minute)
                    newAlarm.start()
                    alarmList.append(newAlarm)
        except FileNotFoundError:
            open(self.fileDirectory, 'w')
        except Exception as e:
            print(e)

    def alarmFileSave(self):
        global alarmList

        with open(self.fileDirectory, 'w') as alarmFile:
            for alarm in alarmList:
                alarmFile.write("{} {}\n".format(str(alarm.startHour), str(alarm.startMinute)))

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
                # os.startfile(ALARM_SOUND)

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

    alarmFileObject = AlarmFile("alarmList.txt")
    alarmFileObject.alarmFileOpen()

    choice = 0
    while choice != 3:
        print("PyAlarm")

        # Print all the alarms
        if len(alarmList) == 0:
            print("Alarm has not been set")
        else:
            for alarm in alarmList:
                print("{}. Alarm set for: {:02}:{:02}".format(alarmList.index(alarm) + 1, alarm.startHour, alarm.startMinute))

        print()
        print("Menu")
        print("====")
        print("1. Add alarm")
        print("2. Delete alarm")
        print("3. Exit")
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

                alarmFileObject.alarmFileSave()
                print("Alarm has been successfully added!")
            except Exception as e:
                print("Error reading time")
                print("Please input only numbers in 'HH MM' format (with space in between)")
                print("Example: '22 00', '12 30', or '07 05'")

            input("\nPress enter to continue...");
        elif choice == 2:
            if len(alarmList) != 0:
                try:
                    alarmIndexDelete = int(input("Input the index of alarm you want to delete : "))
                    alarmList.pop(alarmIndexDelete - 1)
                    alarmFileObject.alarmFileSave()
                    print("Alarm has been successfully deleted!")
                except Exception as e:
                    print("Error reading input")
                    print("Please input only numbers (without leading zeroes) (e.g: 1, 4, 8)")
            else:
                print("There is no alarm")
            
            input("\nPress enter to continue...");
        elif choice == 3:
            pass
        else:
            print("Invalid input...")

        os.system("cls")
