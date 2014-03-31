import time
import os

ALARM_SOUND = "C:\\Users\\Aspire D270\\Music\\Ennio Morricone - The Crisis.mp3"

def alarmClock(hour, minute):
    print(time.strftime("Started on: %H.%M"))
    print("Alarm set for: {}.{}".format(hour, minute))
	
    while True:
        localTime = time.localtime()
        if(localTime.tm_hour == hour and localTime.tm_min == minute):
            print("It's time to sleep...")
            os.startfile(ALARM_SOUND)
            break

alarmClock(22, 0)
