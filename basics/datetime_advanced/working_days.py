from datetime import datetime, timedelta
start=datetime(2026,4,1)
end=datetime(2026,4,10)
working_days=0
current=start
while current<=end:
    if current.weekday()<5:
        working_days+=1
    current += timedelta(days=1)
print("working days:", working_days)