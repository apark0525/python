# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 20:30:04 2022

@author: heost
"""

namelist = ["mario", "emily", "ray", "zafar", "aladin"]

def sort_name(name):#함수의 입력값 변수 이름
    if (name[0] < 'f'):
        print(name, " in a - e")
    elif (name[0] < 's'):
        print(name, " in f - r")
    else:# s - z
        print(name, " in s - z")
        
for name in namelist:
    sort_name(name)
