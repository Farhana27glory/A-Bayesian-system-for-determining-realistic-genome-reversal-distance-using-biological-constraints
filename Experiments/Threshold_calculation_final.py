#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 19:53:16 2021

@author: gloryfz
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 19:49:26 2021

@author: gloryfz
"""
import re
import math
import os


def str_list_to_int_list(str_list):
        int_list = [int(n) for n in str_list]
        return int_list
    
i = 0
with open("testvvv.txt") as fp:
    for line in fp:
        i+=1
        if i == 3:
            destination = line
#print(destination)

def function(found):
    
    
    items_1 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', found)
    items_1 = re.sub('[,]', '', items_1)
    #print(items_1) 
    
    
    
    ListA = list(items_1.split(" "))
    ListB = list(destination.split(" "))
    #print(ListA)
    #print(ListB)
    
    
    ListA =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in ListA]
    ListB =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in ListB]
    #print(ListA)
    #print(ListB)
    
    
    ListA = (str_list_to_int_list(ListA))
    ListB = (str_list_to_int_list(ListB))
    #print(ListA)
    #print(ListB)
    
    count = 0
    division = math.ceil(len(ListA)/2)
    #print(division)
    for i in range(0,len(ListA),2):
        
       if ListA[i]==ListB[i]:
          count+=1
          #print(count)
       else:
           pivot_min = min(ListA[i],ListB[i])
           pivot_max = max(ListA[i],ListB[i])
           pivot = pivot_min/pivot_max
           count+=pivot
           #print(count)
    
    #print(count)
    x = ((count/division)*100)
    #print(x)
    return x
    

def threshold_40(number):
    
    if number >= 40:
        file1.write(str(1)+' ')
    else:
        file1.write(str(0)+' ')
     


def threshold_60(number):
    
    if number >= 60:
        file2.write(str(1)+' ')
    else:
        file2.write(str(0)+' ')
    #file2.close()   
    
    
def threshold_80(number):
    
    if number >= 80:
        file3.write(str(1)+' ')
    else:
        file3.write(str(0)+' ')
    #file3.close()   
        
file1 = open('40.txt', 'a+')
file2 = open('60.txt', 'a+')
file3 = open('80.txt', 'a+')
with open('Top_1_result_updated.txt') as fp:
   cnt = 0
   total = 0
   for line in fp:
       cnt +=1
       length = line.count("->")
       #print(length)
       #print(line)
       line.split('->')
       lst = (line.split('->')[length-1])
       ##my_list = line.split("->")
       #print(my_list)
      
       #lst = my_list
       
           
       List12 = lst
       #print(List12) 
       found = List12
       total += function(found)

   #print(total)
   avg = total/cnt 
   #print(avg) 
   #file1.write("\n")
   threshold_40(avg)
   #file1.write("\n")
   threshold_60(avg)
   #file1.write("\n")
   threshold_80(avg)
   #file1.write("\n")
   
  
with open('Top_5_results_updated.txt') as fp:
   cnt = 0
   total = 0
   for line in fp:
       cnt +=1
       length = line.count("->")
       #print(length)
       #print(line)
       line.split('->')
       lst = (line.split('->')[length-1])
       ##my_list = line.split("->")
       #print(my_list)
      
       #lst = my_list
       
           
       List12 = lst
       #print(List12) 
       found = List12
       total += function(found)

   #print(total)
   avg = total/cnt 
   #print(avg) 
   
   threshold_40(avg)
   #file1.write("\n")
   threshold_60(avg)
   #file1.write("\n")
   threshold_80(avg)
   #file1.write("\n")

with open('Top_15_results_updated.txt') as fp:
   cnt = 0
   total = 0
   for line in fp:
       cnt +=1
       length = line.count("->")
       #print(length)
       #print(line)
       line.split('->')
       lst = (line.split('->')[length-1])
       ##my_list = line.split("->")
       #print(my_list)
      
       #lst = my_list
       
           
       List12 = lst
       #print(List12) 
       found = List12
       total += function(found)

   #print(total)
   avg = total/cnt 
   #print(avg) 
   
   threshold_40(avg)
   #file1.write("\n")
   threshold_60(avg)
   #file1.write("\n")
   threshold_80(avg)
   #file1.write("\n")
   
   
with open('Top_25_results_updated.txt') as fp:
   cnt = 0
   total = 0
   for line in fp:
       cnt +=1
       length = line.count("->")
       #print(length)
       #print(line)
       line.split('->')
       lst = (line.split('->')[length-1])
       ##my_list = line.split("->")
       #print(my_list)
      
       #lst = my_list
       
           
       List12 = lst
       #print(List12) 
       found = List12
       total += function(found)

   #print(total)
   avg = total/cnt 
   #print(avg) 
   
   threshold_40(avg)
   #file1.write("\n")
   threshold_60(avg)
   #file1.write("\n")
   threshold_80(avg)
   #file1.write("\n")
  
    
file1.close()
file2.close()  
file3.close()       
   




