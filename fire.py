# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:16:33 2018

@author: Samqua

Cellular automaton forest-fire model. The rules are:
` White cells ("trees") grow spontaneously from black ("empty") cells with probability p.
` They ignite ("struck by lightning") spontaneously with probability f, becoming red ("burning") cells for one iteration.
` Any cell with a burning Moore neighbor will ignite in the next iteration.
` Any currently burning cell will blacken in the next iteration.
Behavior depends heavily on the parametric ratio p/f: for p>>f, the model may display so-called self-organized criticality.
Saves the model as an .mp4 using x264 encoding. The average density of each iteration is also saved to a text file.
"""

import random
import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
import datetime
import copy

start=datetime.datetime.now()
print("START: "+str(start))

L=200 # side length
f=0.00005 # recommended 0.00005
p=0.005 # recommended 0.005
seconds=10 # length of the final .mp4 file

forest = [[random.randint(0,2) for i in range(L)] for j in range(L)] # randomize forest
ratiolist=[]

def hasBurningNeighbor(i,j):
        if forest[(i+1)%L][j]==1:
                return True
        elif forest[(i-1)%L][j]==1:
                return True
        elif forest[i][(j+1)%L]==1:
                return True
        elif forest[i][(j-1)%L]==1:
                return True
        elif forest[(i+1)%L][(j+1)%L]==1:
                return True
        elif forest[(i+1)%L][(j-1)%L]==1:
                return True
        elif forest[(i-1)%L][(j+1)%L]==1:
                return True
        elif forest[(i-1)%L][(j-1)%L]==1:
                return True
        else:
                return False

def density():
        global forest
        z=0
        for i in range(L):
                for j in range(L):
                        z+=forest[i][j]
        return z/(L**2)

def evolve():
        global forest
        global ratiolist
        nextforest = [[0 for i in range(L)] for j in range(L)] # initialize next forest
        for i in range(L):
                for j in range(L):
                        ff=random.random()
                        pp=random.random()
                        if forest[i][j]==1:
                                nextforest[i][j]=0 # burnout
                        if forest[i][j]==2:
                                if hasBurningNeighbor(i,j)==True:
                                        nextforest[i][j]=1
                                elif ff<f:
                                        nextforest[i][j]=1
                                else:
                                        nextforest[i][j]=2 # no change
                        if forest[i][j]==0:
                                if pp<p:
                                        nextforest[i][j]=2
        forest=copy.deepcopy(nextforest)
        ratiolist.append(density())

fig = plt.figure(figsize=(8,8),dpi=100)
plt.title("f="+str(f)+", p="+str(p)+", p/f="+str(p/f))
ax = fig.add_subplot(1,1,1)
im = plt.imshow(np.matrix(forest), interpolation='nearest', cmap=plt.cm.gist_heat, animated=True)
#plt.colorbar()
def updatefig(*args):
        evolve()
        im.set_array(np.matrix(forest))
        return im,

anim = animation.FuncAnimation(fig, updatefig, frames=60*seconds)
plt.show()
anim.save('forestfire-'+datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")+'.mp4', fps=60, extra_args=['-vcodec', 'libx264'])

print("END: "+str(datetime.datetime.now()))
print("RUN TIME: "+str(datetime.datetime.now()-start))
print("\n")

f=open('ratio-'+datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")+'.txt', 'w')
f.write("ratiolist="+str(ratiolist))
f.close()
