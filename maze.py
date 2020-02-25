# -*- coding: utf-8 -*-
import numpy as np
import random

def make_maze(mX, mY):
    mZ = mX * mY
    m = np.arange(0,mZ).reshape((mX, mY))
    m[:] = 0
    return m

def oddNumber(num):
    if num % 2 == 0:
        return False
    else:
        return True

def maze_set(mX, mY):
    # wall
    maze[0][:mY]=9 # y0
    maze[mX-1][:mY-1]=9 # y8
    for _ in range(0, mX):
        maze[_][0]=9 # x0
        maze[_][mX-1]=9 # x8

def rnd():
    num=random.randint(1,4)
    return num

def chkMv(maze, pX, pY, mRnd):
    if mRnd==1: # 東
        if maze[pX][pY+1] == 0 or maze[pX][pY+1] == 9 or maze[pX][pY+2] == 0:
            maze[pX][pY+1]=maze[pX][pY+2]=1
            return pX, pY+2
    elif mRnd==2: # 南
        if maze[pX+1][pY] == 0 or maze[pX+1][pY] == 9 or maze[pX+2][pY] == 0:
            maze[pX+1][pY]=maze[pX+2][pY]=1
            return pX+2, pY
    elif mRnd==3: # 西
        if maze[pX][pY-1] == 0 or maze[pX][pY-1] == 9 or maze[pX][pY-2] == 0:
            maze[pX][pY-1]=maze[pX][pY-2]=1
            return pX, pY-2
    elif mRnd==4: # 北
        if maze[pX-1][pY] == 0 or maze[pX-1][pY] == 9 or maze[pX-2][pY] == 0:
            maze[pX-1][pY]=maze[pX-2][pY]=1
            return pX-2, pY
    else:
        return False

# mazeSize
mX=7
mY=7

if oddNumber(mX) and oddNumber(mY):
    if mX>3:
        maze=make_maze(mX, mY)
        # print (maze)
    else:
        print ('Odd number of 3 or more')
else:
    print ('not Odd number')

maze_set(mX, mY)

# start
nX=3
nY=3
maze[nX][nY]=3

cnt=0
mvlist=[]

while cnt<10:
    mRnd=rnd() # 行動決定
    print ('mRnd='+str(mRnd),'nX='+str(nX) ,'nY='+str(nY))

    flag=chkMv(maze, nX, nY, mRnd)
    print ('set=', flag)
    if not flag==False:
        nX=flag[0]
        nY=flag[1]
        print (maze)
    else:
        continue

    cnt+=1


print ('done')
