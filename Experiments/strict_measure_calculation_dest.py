#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 02:45:12 2021

@author: gloryfz
"""
import re


def str_list_to_int_list(str_list):
        int_list = [int(n) for n in str_list]
        return int_list

def strict_measure(lsA, lsB):
    count = 0
    
    for p in range(len(lsA)):       
        if lsA[p] == lsB[p]:
            count+=1
    '''
    if count == len(lsA):
        print("fully matched")
        file1.write(str(1)+" ")
    else:
        print("Not matched")
        file1.write(str(0)+" ")
    '''
    return count        

i = 0
with open("testvvv.txt") as fp:
    for line in fp:
        i+=1
        if i == 3:
            destination = line
#print(destination)
ListB = list(destination.split(" "))
ListB =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in ListB]
ListB = (str_list_to_int_list(ListB))
#print(ListB)


file1 = open('strict.txt', 'a+')
with open('Top_1_result_updated.txt') as fp:
   cnt = 0
   count = 0
   for line in fp:
       cnt +=1
       length = line.count("->")
       #print(length)
       #print(line)
       line.split('->')
       lst = (line.split('->')[length-1])
       List12 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', lst)
       List12 = re.sub('[,]', '', List12)
       ListA = list(List12.split(" "))
       ListA =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in ListA]
       ListA = (str_list_to_int_list(ListA))
       #print(ListA)
       cnt +=1
       count = strict_measure(ListA, ListB)
       if count == len(ListA):
          #print("fully matched")
          file1.write(str(1)+" ")
       else:
          #print("Not matched")
          file1.write(str(0)+" ")
   file1.write("\n")
   fp.close()  
#file1.close()


with open('Top_5_results_updated.txt') as fp:
   cnt = 0
   count = 0
   for line in fp:
       cnt +=1
       length = line.count("->")
       #print(length)
       #print(line)
       line.split('->')
       lst = (line.split('->')[length-1])
       List12 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', lst)
       List12 = re.sub('[,]', '', List12)
       ListA = list(List12.split(" "))
       ListA =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in ListA]
       ListA = (str_list_to_int_list(ListA))
       #print(ListA)
       cnt +=1
       count = strict_measure(ListA, ListB)
       if count == len(ListA):
          #print("fully matched")
          file1.write(str(1)+" ")
       else:
          #print("Not matched")
          file1.write(str(0)+" ")
   file1.write("\n")
   fp.close()  
#file1.close()

with open('Top_15_results_updated.txt') as fp:
   cnt = 0
   cnt = 0
   count = 0
   for line in fp:
       cnt +=1
       length = line.count("->")
       #print(length)
       #print(line)
       line.split('->')
       lst = (line.split('->')[length-1])
       List12 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', lst)
       List12 = re.sub('[,]', '', List12)
       ListA = list(List12.split(" "))
       ListA =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in ListA]
       ListA = (str_list_to_int_list(ListA))
       #print(ListA)
       cnt +=1
       count = strict_measure(ListA, ListB)
       if count == len(ListA):
          #print("fully matched")
          file1.write(str(1)+" ")
       else:
          #print("Not matched")
          file1.write(str(0)+" ")
   file1.write("\n")
   fp.close()   
#file1.close()

with open('Top_25_results_updated.txt') as fp:
   cnt = 0
   count = 0
   for line in fp:
       cnt +=1
       length = line.count("->")
       #print(length)
       #print(line)
       line.split('->')
       lst = (line.split('->')[length-1])
       List12 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', lst)
       List12 = re.sub('[,]', '', List12)
       ListA = list(List12.split(" "))
       ListA =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in ListA]
       ListA = (str_list_to_int_list(ListA))
       #print(ListA)
       cnt +=1
       count = strict_measure(ListA, ListB)
       if count == len(ListA):
          #print("fully matched")
          file1.write(str(1)+" ")
       else:
          #print("Not matched")
          file1.write(str(0)+" ")
   file1.write("\n")
   fp.close()

with open('Top_40_results_updated.txt') as fp:
   cnt = 0
   count = 0
   for line in fp:
       cnt +=1
       length = line.count("->")
       #print(length)
       #print(line)
       line.split('->')
       lst = (line.split('->')[length-1])
       List12 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', lst)
       List12 = re.sub('[,]', '', List12)
       ListA = list(List12.split(" "))
       ListA =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in ListA]
       ListA = (str_list_to_int_list(ListA))
       #print(ListA)
       cnt +=1
       count = strict_measure(ListA, ListB)
       if count == len(ListA):
          #print("fully matched")
          file1.write(str(1)+" ")
       else:
          #print("Not matched")
          file1.write(str(0)+" ")
   file1.write("\n")
   fp.close()

file1.close()
