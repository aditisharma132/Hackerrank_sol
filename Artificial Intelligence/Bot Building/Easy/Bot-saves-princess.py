#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    for i in range(0, n):
        if 'p' in grid[i]:
            princess = (i, grid[i].index('p'))
        if 'm' in grid[i]:
            bot = (i, grid[i].index('m'))
    while princess[0] != bot[0]:
        if princess[0] > bot[0]:
            print("DOWN")
            bot = (bot[0] + 1, bot[1])
        else:
            print("UP")
            bot = (bot[0] - 1, bot[1])
    while princess[1] != bot[1]:
        if princess[1] > bot[1]:
            print("RIGHT")
            bot = (bot[0], bot[1] + 1)
        else:
            print("LEFT")
            bot = (bot[0], bot[1] - 1)

            

   

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)