from datetime import datetime
logs = [
    "2026-04-09 10:30:45 User login",
    "2026-04-08 09:15:20 File uploaded",
    "2026-04-09 12:00:00 Error occurred"
]
filter_date = "2026-04-08"
for log in logs:
    log_date = log.split(" ")[0]
    if log_date == filter_date:
        print(log)