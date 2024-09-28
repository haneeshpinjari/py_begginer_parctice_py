import time
alarm_time = input("Enter the alarm time (HH:MM:SS): ")
while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("wake up! It's time!")
        break
    time.sleep(1)