import time
from datetime import datetime


while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    time.sleep(10)