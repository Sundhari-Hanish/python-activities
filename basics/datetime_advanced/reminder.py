from datetime import datetime
import time
reminder_time=input("Enter reminder time( HH:MM:SS): ")
message=input("Enter reminder message:")
while True:
    now=datetime.now().strftime("%H:%M:%S")
    if now ==reminder_time:
        print("\nReminder:",message)
        break
    time.sleep(1)

