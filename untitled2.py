# -*- coding: utf-8 -*-
"""
Created on Fri May  6 20:46:30 2022

@author: heost
"""
import random

player = 0
maximum = 20
star = random.randint(1, maximum/2)


def show_status():
    for i in range(maximum):# first line
        if i==0:
            print("---", end='')
        else:
            print("--", end='')
    
    print(" ")
    
    for i in range(maximum):# second line
        print("|", end='')
        if i == player:
            print("P", end='')
            if i == star:
                print("S", end='')
        elif i == star:
            print("S", end='')
        else:
            print(" ", end='')
            
    print("|")
    
    for i in range(maximum):# third line
        if i==0:
            print("---", end='')
        else:
            print("--", end='')
        
    print("")


# get user input
# work in the loop and update the player & star position

while (player != star) and (star < maximum):
    show_status()
    step = input("make your next step: ")
    player = player + int(step)
    star = star + random.randint(1, 3)
    
if (player == star):
    show_status()
    print("you got the star")
else:
    show_status()
    print("game over")
    