# -*- coding: utf-8 -*-
import queue
import random
q = queue.Queue(maxsize=0)
root = [0,0,None]
goal = [2,0,None]
q.put(root)
final = root
found = False

#For exploring nodes using BFS
while (found == False and q.empty()==False):
    E = q.get()
    x = E[0]
    y = E[1]
    Parent = E[2]
    
    succ = random.randint(1,3)
    print (succ)
    if (x==2 and y==0):
        found=True
        #print (E)
        final = E
        print ("Found")
        break
    if (succ==1):
        if (x<4):
            e1 = [4,y,E]
            q.put(e1)
        else:
            q.put(E)
        if (y<3):
            e1 = [x,3,E]
            q.put(e1)
    if (succ==2):
        if (x>0):
            e1 = [0,y,E]
            q.put(e1)
        else:
            q.put(E)
        if (y>0):
            e1 = [x,0,E]
            q.put(e1)
        else:
            q.put(E)
    if (succ==3):
        if (x+y>=3 and x>0):
            e1 = [x-(3-y),3,E]
            q.put(e1)
        else:
            q.put(E)
        if (x+y>=4 and y>0):
            e1 = [4,y-(4-x),E]
            q.put(e1)
        else:
            q.put(E)
        if (x+y<=3 and x>0):
            e1 = [0,x+y,E]
            q.put(e1)
        else:
            q.put(E)
        if (x+y<=4 and y>0):
            e1 = [x+y,0,E]
            q.put(e1)
        else:
            q.put(E)
    if (x==0 and y==2):
        e1 = [2,0,E]
        q.put(e1)
    else:
            q.put(E)
    if (x==2):
        e1 = [0,y,E]
        q.put(e1)
    else:
            q.put(E)
    


#For printing the answer in Correct sequence

Answer = queue.LifoQueue(maxsize=0)

while final[2]!=None:
    result=[final[0],final[1]]
    Answer.put(result)
    final = final[2]
    
while (Answer.empty()==False):
    x = Answer.get()
    print(x)