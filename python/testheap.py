import heap
import random
from random import randint
n=heap.Heap()
num_items=10
for i in range(num_items):
    n.insert(random.uniform(0,100))
sorted1=[]

print "Done Inserting"
for i in range(num_items):
    sorted1.append(n.extractmin())
    if i%1000==0:
        print ".",
print "Done extracting"
for i in range(num_items-1):
    if sorted1[i+1]<sorted1[i]:
        print "ERRRORRR"
print sorted1
