#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:59:58 2021

@author: gloryfz
"""

import re

file11 = open('Top_1_result.txt',
             'r')
file21 = open('Top_5_results.txt',
             'r')
file31 = open('Top_15_results.txt',
             'r')
file41 = open('Top_25_results.txt',
             'r')
file51 = open('Top_40_results.txt',
             'r')
  
# defining object file2 to 
# open GeeksforGeeksUpdated file
# in write mode
file12 = open('Top_1_result_updated.txt',
             'w')
file22 = open('Top_5_results_updated.txt',
             'w')
file32 = open('Top_15_results_updated.txt',
             'w')
file42 = open('Top_25_results_updated.txt',
             'w')
file52 = open('Top_40_results_updated.txt',
             'w')
  
# reading each line from original 
# text file
for line in file11.readlines():
    
    # reading all lines that begin 
    # with "TextGenerator"
    x = re.findall("times", line)
      
    if not x:
        
        # printing those lines
        #print(line)
          
        # storing only those lines that 
        # do not begin with "TextGenerator"
        file12.write(line)
          
# close and save the files
file11.close()
file12.close()

for line in file21.readlines():
    
    # reading all lines that begin 
    # with "TextGenerator"
    x = re.findall("times", line)
      
    if not x:
        
        # printing those lines
        #print(line)
          
        # storing only those lines that 
        # do not begin with "TextGenerator"
        file22.write(line)
          
# close and save the files
file21.close()
file22.close()


for line in file31.readlines():
    
    # reading all lines that begin 
    # with "TextGenerator"
    x = re.findall("times", line)
      
    if not x:
        
        # printing those lines
        #print(line)
          
        # storing only those lines that 
        # do not begin with "TextGenerator"
        file32.write(line)
          
# close and save the files
file31.close()
file32.close()

for line in file41.readlines():
    
    # reading all lines that begin 
    # with "TextGenerator"
    x = re.findall("times", line)
      
    if not x:
        
        # printing those lines
        #print(line)
          
        # storing only those lines that 
        # do not begin with "TextGenerator"
        file42.write(line)
          
# close and save the files
file41.close()
file42.close()

for line in file51.readlines():
    
    # reading all lines that begin 
    # with "TextGenerator"
    x = re.findall("times", line)
      
    if not x:
        
        # printing those lines
        #print(line)
          
        # storing only those lines that 
        # do not begin with "TextGenerator"
        file52.write(line)
          
# close and save the files
file51.close()
file52.close()
