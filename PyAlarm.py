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

alarmClock(21, 0)
