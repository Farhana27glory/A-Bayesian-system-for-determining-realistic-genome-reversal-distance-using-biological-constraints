#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 19:33:41 2021

@author: gloryfz
"""
import re
import math
import os
from datetime import datetime

with open('result.txt') as fp:
   str1 = "12"
   count = 0
   file1 = open('frequency.txt', 'a+')
   for line in fp:
       number = line.strip()
       #print(number)
       if str1 == number:
           count+=1
   #file1.write(str(count)+" ")
   file1.write(str(count)+"times\n")
    #print("4 length path found in Bayesian System in 50000 iterations:",(count), "times")   
file1.close()       
fp.close()

if os.path.exists("outputtest.txt"):
  os.remove("outputtest.txt")
else:
  print("The file does not exist")

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
