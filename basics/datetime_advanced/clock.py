from datetime import datetime
import time
while True:
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    print("\r Current Time:",current_time,end="")
    time.sleep(1)

    