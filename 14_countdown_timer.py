import time
second = int(input("enter the countdown : "))
for i in range(second, 0, -1):
    print(i)
    time.sleep(1)
print("Time's Up")