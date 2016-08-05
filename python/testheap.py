import heap
import random
n=heap.Heap()
num=1000

for i in range(num):
    n.insert(random.uniform(0,num))
sorted1=[]

print "Done inserting"
for i in range(num):
    sorted1.append(n.extractmin())

print "Done extracting"

for i in range(num-1):
    if sorted1[i+1]<sorted1[i]:
        print "ERRRORRR"+str(i)

