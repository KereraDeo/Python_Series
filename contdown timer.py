import time
my_time=int(input("enter the time in seconds:"))
for x in range(my_time,0,-1):
    seconds=x%60
    mins=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{mins:02}:{seconds:02}")
    #02 is for the padding on 09,08...
    time.sleep(1)
print("TIME'S UP!")