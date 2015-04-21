import threading
max_loop_count = 10

k=[]
k.append(0)

class MyThread (threading.Thread):
    def run(self):
        for i in range(max_loop_count):
            k[0] = i
            print("Value of i = ",i)
            if k[0]!=i:
                print("This cant print ######################## from thread")
 

thread1 = MyThread()
thread1.start()
print("Started thread");
for j in range (max_loop_count):
    print("************Value of j =",j)
    if k[0] != j:
        print("This cant print ######################## from main")
 
