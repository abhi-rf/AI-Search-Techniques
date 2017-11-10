# -*- coding: utf-8 -*-
import queue
q = queue.Queue(maxsize=0)
root = [0,0,None]
goal = [2,0,None]
q.put(root)
final = root
found = False

#For exploring nodes using BFS
while (found == False and q.empty() == False):
    E = q.get()
    x = E[0]
    y = E[1]
    Parent = E[2]
    #print ("Parent",E)
    if (x==2 and y==0):
        found=True
        #print (E)
        final = E
        print ("Found")
        break
    if (x<4):
        e1 = [4,y,E]
        #print (e1)
        q.put(e1)
    if (y<3):
        e1 = [x,3,E]
        #print (e1)
        q.put(e1)
    if (x>0):
        e1 = [0,y,E]
        #print (e1)
        q.put(e1)
    if (y>0):
        e1 = [x,0,E]
        #print (e1)
        q.put(e1)
    if (x+y>=3 and x>0):
        e1 = [x-(3-y),3,E]
        #print (e1)
        q.put(e1)
    if (x+y>=4 and y>0):
        e1 = [4,y-(4-x),E]
        #print (e1)
        q.put(e1)
    if (x+y<=3 and x>0):
        e1 = [0,x+y,E]
        #print (e1)
        q.put(e1)
    if (x+y<=4 and y>0):
        e1 = [x+y,0,E]
        #print (e1)
        q.put(e1)
    if (x==0 and y==2):
        e1 = [2,0,E]
        #print (e1)
        q.put(e1)
    if (x==2):
        e1 = [0,y,E]
        #print (e1)
        q.put(e1)
    
    #print ("")


#For printing the answer in Correct sequence

Answer = queue.LifoQueue(maxsize=0)

while final[2]!=None:
    result=[final[0],final[1]]
    Answer.put(result)
    final = final[2]
    
while (Answer.empty()==False):
    x = Answer.get()
    print(x)