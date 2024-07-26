import time
sec=int(input("Enter secons: "))
for x in (range(sec,0,-1)):
    print(x,end=" ")
    time.sleep(1)
print("TIME IS UP NOW")