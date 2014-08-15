import os
import time

ALARM_SOUND = "C:\\Users\\Aspire D270\\Music\\Moongazer.mp3"

def alarmClock(hour, minute):
    print(time.strftime("Started on: %H:%M"))
    print("Alarm set for: {:02}:{:02}".format(hour, minute))
	
    while True:
        localTime = time.localtime()
        if localTime.tm_hour == hour and localTime.tm_min == minute:
            print("It's time to sleep...")
            os.startfile(ALARM_SOUND)

            # Shutdown Windows via Command Prompt
            os.system("shutdown /s /t 180 /c \"Time to Sleep...\"")
            break

choice = 0

try:
    with open("alarms.txt") as alarmFile:
        hour = int(alarmFile.readline())
        minute = int(alarmFile.readline())
except FileNotFoundError:
    hour = -1
    minute = -1

while choice != 3:
    print("PyAlarm")
    print("By: Edo Morgen")
    print("")

    if hour == -1 and minute == -1:
        print("Alarm has not been set")
    else:
        print("Alarm set for {:02}:{:02}".format(hour, minute))
    
    print("1. Turn on alarm")
    print("2. Configure alarm")
    print("3. Exit")
    print("")

    choice = int(input("Choice: "))
    if choice == 1:
        if hour == -1 and minute == -1:
            print("Alarm has not been set")
            print("Please set it first...")
        else:
            alarmClock(hour, minute)
    elif choice == 2:
        hour = int(input("Input the hour (in 24-hour format): "))
        minute = int(input("Input the minute: "))

        alarmFile = open("alarms.txt", mode = 'w')
        alarmFile.write("{}\n".format(str(hour)))
        alarmFile.write("{}\n".format(str(minute)))
        alarmFile.close()
        
    elif choice == 3:
        pass
    else:
        print("Invalid input...")

    print("")
    print("")
    print("")
