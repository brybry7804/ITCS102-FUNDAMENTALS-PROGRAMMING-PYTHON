import time 

def timer(x):
    for s in range (x, 0, -1):
        time.sleep(1)
        print(s)
    print("stop")
    

# timer(20)