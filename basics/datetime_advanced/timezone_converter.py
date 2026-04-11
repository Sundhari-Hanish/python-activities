from datetime import datetime
import pytz
local = pytz.timezone("Asia/Kolkata")
target = pytz.timezone("US/Eastern")
local_time = datetime.now(local)
# Convert
target_time = local_time.astimezone(target)
print("Local Time:", local_time.strftime("%Y-%m-%d %H:%M:%S"))
print("US Time:", target_time.strftime("%Y-%m-%d %H:%M:%S"))