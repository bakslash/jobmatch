#!/usr/bin/env python
import random

li=[]
for x in random.sample(range(1,100),50):
    for y in random.sample(range(1,100),50):
        li.append((x,y))
        li.sort()
print li
