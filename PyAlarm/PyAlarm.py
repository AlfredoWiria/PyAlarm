import os
import time

######################
# Constant Variables #
######################

# Set this to the directory + file name of an alarm sound (any music file type can be used)
ALARM_SOUND = ""

# Set this to the directory + file name of an alarm list (any plain text file type can be used)
ALARM_LIST = "alarmList.txt"

#############
# Functions #
#############

# Main routine of alarm clock
# When it's time for the alarm, shutdown the computer
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

################
# Main Routine #
################

# If run as a script (not imported by another module), execute the following codes
if __name__ == "__main__":
	try:
		with open(ALARM_LIST) as alarmFile:
			hour, minute = [int(x) for x in alarmFile.readline().split()]
	except FileNotFoundError:
		hour = -1
		minute = -1

	choice = 0
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
			hour, minute = [int(x) for x in input("Input alarm time (in 'HH MM' format): ").split()]
			
			alarmFile = open(ALARM_LIST, mode = 'w')
			alarmFile.write("{} {}\n".format(str(hour), str(minute)))
			alarmFile.close()

			print("Alarm has been successfully added!")
			input("Press enter to continue...")
		elif choice == 3:
			pass
		else:
			print("Invalid input...")

		os.system("cls")