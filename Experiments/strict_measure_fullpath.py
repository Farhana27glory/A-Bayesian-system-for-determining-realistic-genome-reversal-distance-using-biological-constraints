#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 01:01:55 2021

@author: gloryfz
"""
import re
import math

def str_list_to_int_list(str_list):
        int_list = [int(n) for n in str_list]
        return int_list

def intergenic_conversion(Lis):
  for k in range(math.floor(len(Lis))):
    for i in range(len(Lis)):
       if type(Lis[i]) == str:
          M = int(Lis[i])
          Lis.pop(i)
          if M!=0:
            for j in range(M):
              Lis.insert(j+i,0)
          else:
              break
       else:
          continue

  return(Lis)  

def function(string):  
    lst = my_list
    #print(extractDigits(lst))
    
    List12 = lst[0]
    List22 = lst[1]
    List32 = lst[2]
    List42 = lst[3]
    #List52 = lst[4]
    #List62 = lst[5]
    #List72 = lst[6]
    #List82 = lst[7]
    
    
    '''
    print(List12)
    print(List22)
    print(List32)
    print(List42)
    print(List52)
    print(List62)
    print(List72)
    '''
    
    List12 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List12)
    List12 = re.sub('[,]', '', List12)
    List22 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List22)
    List22 = re.sub('[,]', '', List22)
    List32 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List32)
    List32 = re.sub('[,]', '', List32)
    List42 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List42)
    List42 = re.sub('[,]', '', List42)
    #List52 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List52)
    #List52 = re.sub('[,]', '', List52)
    #List62 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List62)
    #List62 = re.sub('[,]', '', List62)
    #List72 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List72)
    #List72 = re.sub('[,]', '', List72)
    
    #print(List12)
            
    List12 = list(List12.split(" "))
    List22 = list(List22.split(" "))
    List32 = list(List32.split(" "))
    List42 = list(List42.split(" "))
    #List52 = list(List52.split(" "))
    #List62 = list(List62.split(" "))
    #List72 = list(List72.split(" "))
    
    #print(List12)
    
    List12 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List12]
    List22 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List22]
    List32 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List32]
    List42 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List42]
    #List52 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List52]
    #List62 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List62]
    #List72 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List72]
    
    #print(List12)
    
    
    for i in range(0, len(List12)): 
        if i % 2==1: 
            List12[i] = int(List12[i]) 
    
    for i in range(0, len(List22)): 
        if i % 2==1: 
            List22[i] = int(List22[i]) 
    
    for i in range(0, len(List32)): 
        if i % 2==1: 
            List32[i] = int(List32[i]) 
    
    for i in range(0, len(List42)): 
        if i % 2==1: 
            List42[i] = int(List42[i]) 
    '''
    for i in range(0, len(List52)): 
        if i % 2==1: 
            List52[i] = int(List52[i]) 
    
    for i in range(0, len(List62)): 
        if i % 2==1: 
            List62[i] = int(List62[i]) 
    
    for i in range(0, len(List72)): 
        if i % 2==1: 
            List72[i] = int(List72[i]) 
    '''
    
    
    #print(List12)
    
    
    List12 =(intergenic_conversion(List12))
    List22 =(intergenic_conversion(List22))
    List32 =(intergenic_conversion(List32))
    List42 =(intergenic_conversion(List42))
    #List52 =(intergenic_conversion(List52))
    #List62 =(intergenic_conversion(List62))
    #List72 =(intergenic_conversion(List72))
    
    
    #print(List12)
    #print(List22)
    #print(List32)
    #print(List42)
    #print(List52)
    #print(List62)
    
    return(List12, List22, List32, List42)
    #return(List12, List22, List32, List42, List52, List62)

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


def common_elements(list1, list2):
    result = []
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            result.append(list1[i])
    #print(result)
    return len(result)



cnt = 0
with open('transformations.txt') as fp:
   
   for line in fp:
       #print("Line {}: {}".format(cnt, line.strip()))
       if cnt == 0:
          List11 = line.strip()
       elif cnt ==1:
          List21 = line.strip()
       elif cnt ==2:
          List31 = line.strip()
       elif cnt ==3:
          List41 = line.strip()
       '''
       elif cnt ==4:
          List51 = line.strip()  
       elif cnt ==5:
          List61 = line.strip()
       elif cnt ==6:
          List71 = line.strip()
       '''
       
       cnt +=1

#print(cnt)
List11 = list(List11.split(" "))
List21 = list(List21.split(" "))
List31 = list(List31.split(" "))
List41 = list(List41.split(" "))
#List51 = list(List51.split(" "))
#List61 = list(List61.split(" "))
#List71 = list(List71.split(" "))



List11 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List11]
List21 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List21]
List31 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List31]
List41 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List41]
#List51 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List51]
#List61 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List61]
#List71 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List71]



List11 = (str_list_to_int_list(List11))
List21 = (str_list_to_int_list(List21))
List31 = (str_list_to_int_list(List31))
List41 = (str_list_to_int_list(List41))
#List51 = (str_list_to_int_list(List51))
#List61 = (str_list_to_int_list(List61))
#List71 = (str_list_to_int_list(List71))


#print(List11)
#print(List21)
#print(List31)
#print(List41)
#print(List51)
#print(List61)


file1 = open('strict_full.txt', 'a+')
'''
with open('Top_1_result_updated.txt') as fp:
   cnttd = 0
   for line in fp:
       cnttd +=1
       length = line.count("->")
       print(length)
fp.close()
'''
cnttd = 0  
length = 0
with open('Top_1_result_updated.txt') as fp:
     for line in fp:
        cnttd +=1
        length = line.count("->")
        #print(length)
fp.close()


with open('Top_1_result_updated.txt') as fp:
     if length == cnt:
               total = 0
               #print(total)
               pivot = 0
               for line in fp:
                  #print("Line {}: {}".format(pivot, line.strip())) 
                  my_list = line.split("->")
                  List12, List22, List32, List42 = function(my_list)
                  #List12, List22, List32, List42, List52, List62 = function(my_list)
                  #print(common_elements(List11, List12))
                  total = common_elements(List11, List12)
                  #print(common_elements(List21, List22))
                  total += common_elements(List21, List22)
                  #print(common_elements(List31, List32))
                  total += common_elements(List31, List32)
                  #print(common_elements(List41, List42))
                  total += common_elements(List41, List42)
                  #print(common_elements(List51, List52))
                  #total += common_elements(List51, List52)
                  #print(common_elements(List61, List62))
                  #total += common_elements(List61, List62)
                  #total += common_elements(List71, List72)
                  #total += common_elements(List81, List82)
                  #print(total)
                  if total == 716:
                     #print("fully matched")
                     file1.write(str(1)+" ")
                  else:
                     #print("Not matched")
                     file1.write(str(0)+" ")
     else:
               #print("Not matched")
               file1.write(str(0)+" ")
                     
     file1.write("\n")
fp.close() 


cnttd = 0  
length = 0
with open('Top_5_results_updated.txt') as fp:
     for line in fp:
        cnttd +=1
        length = line.count("->")
        #print(length)
fp.close()

with open('Top_5_results_updated.txt') as fp:
    abcd = 0 
    pivot = 0
    for line in fp:
       #print("Line {}: {}".format(pivot, line.strip())) 
       my_list = line.split("->")
       abcd +=1
       pivot+=1
       length = line.count("->")
       #print(length)
       #print(my_list)
       if length == cnt:
                  total = 0
                  #print(total)
                  List12, List22, List32, List42 = function(my_list)
                  #List12, List22, List32, List42, List52, List62 = function(my_list)
                  #print(common_elements(List11, List12))
                  total = common_elements(List11, List12)
                  #print(common_elements(List21, List22))
                  total += common_elements(List21, List22)
                  #print(common_elements(List31, List32))
                  total += common_elements(List31, List32)
                  #print(common_elements(List41, List42))
                  total += common_elements(List41, List42)
                  #print(common_elements(List51, List52))
                  #total += common_elements(List51, List52)
                  #print(common_elements(List61, List62))
                  #total += common_elements(List61, List62)
                  #total += common_elements(List71, List72)
                  #total += common_elements(List81, List82)
                  #print(total)
                  if total == 716:
                     #print("fully matched")
                     file1.write(str(1)+" ")
                  else:
                     #print("Not matched")
                     file1.write(str(0)+" ")
       else:
               #print("Not matched")
               file1.write(str(0)+" ")
                     
    file1.write("\n")
fp.close() 


cnttd = 0  
length = 0
with open('Top_15_results_updated.txt') as fp:
     for line in fp:
        cnttd +=1
        length = line.count("->")
        #print(length)
fp.close()

with open('Top_15_results_updated.txt') as fp:
    abcd = 0 
    pivot = 0
    for line in fp:
       #print("Line {}: {}".format(pivot, line.strip())) 
       my_list = line.split("->")
       abcd +=1
       pivot+=1
       length = line.count("->")
       #print(length)
       #print(my_list)
       if length == cnt:
                  total = 0
                  #print(total)
                  List12, List22, List32, List42 = function(my_list)
                  #List12, List22, List32, List42, List52, List62 = function(my_list)
                  #print(common_elements(List11, List12))
                  total = common_elements(List11, List12)
                  #print(common_elements(List21, List22))
                  total += common_elements(List21, List22)
                  #print(common_elements(List31, List32))
                  total += common_elements(List31, List32)
                  #print(common_elements(List41, List42))
                  total += common_elements(List41, List42)
                  #print(common_elements(List51, List52))
                  #total += common_elements(List51, List52)
                  #print(common_elements(List61, List62))
                  #total += common_elements(List61, List62)
                  #total += common_elements(List71, List72)
                  #total += common_elements(List81, List82)
                  #print(total)
                  if total == 716:
                     #print("fully matched")
                     file1.write(str(1)+" ")
                  else:
                     #print("Not matched")
                     file1.write(str(0)+" ")
       else:
               #print("Not matched")
               file1.write(str(0)+" ")
                     
    file1.write("\n")
fp.close() 



cnttd = 0  
length = 0
with open('Top_25_results_updated.txt') as fp:
     for line in fp:
        cnttd +=1
        length = line.count("->")
        #print(length)
fp.close()

with open('Top_25_results_updated.txt') as fp:
    abcd = 0 
    pivot = 0
    for line in fp:
       #print("Line {}: {}".format(pivot, line.strip())) 
       my_list = line.split("->")
       abcd +=1
       pivot+=1
       length = line.count("->")
       #print(length)
       #print(my_list)
       if length == cnt:
                  total = 0
                  #print(total)
                  List12, List22, List32, List42 = function(my_list)
                  #List12, List22, List32, List42, List52, List62 = function(my_list)
                  #print(common_elements(List11, List12))
                  total = common_elements(List11, List12)
                  #print(common_elements(List21, List22))
                  total += common_elements(List21, List22)
                  #print(common_elements(List31, List32))
                  total += common_elements(List31, List32)
                  #print(common_elements(List41, List42))
                  total += common_elements(List41, List42)
                  #print(common_elements(List51, List52))
                  #total += common_elements(List51, List52)
                  #print(common_elements(List61, List62))
                  #total += common_elements(List61, List62)
                  #total += common_elements(List71, List72)
                  #total += common_elements(List81, List82)
                  #print(total)
                  if total == 716:
                     #print("fully matched")
                     file1.write(str(1)+" ")
                  else:
                     #print("Not matched")
                     file1.write(str(0)+" ")
       else:
               #print("Not matched")
               file1.write(str(0)+" ")
                     
    file1.write("\n")
fp.close()

cnttd = 0  
length = 0
with open('Top_40_results_updated.txt') as fp:
     for line in fp:
        cnttd +=1
        length = line.count("->")
        #print(length)
fp.close()

with open('Top_40_results_updated.txt') as fp:
    abcd = 0 
    pivot = 0
    for line in fp:
       #print("Line {}: {}".format(pivot, line.strip())) 
       my_list = line.split("->")
       abcd +=1
       pivot+=1
       length = line.count("->")
       #print(length)
       #print(my_list)
       if length == cnt:
                  total = 0
                  #print(total)
                  List12, List22, List32, List42 = function(my_list)
                  #List12, List22, List32, List42, List52, List62 = function(my_list)
                  #print(common_elements(List11, List12))
                  total = common_elements(List11, List12)
                  #print(common_elements(List21, List22))
                  total += common_elements(List21, List22)
                  #print(common_elements(List31, List32))
                  total += common_elements(List31, List32)
                  #print(common_elements(List41, List42))
                  total += common_elements(List41, List42)
                  #print(common_elements(List51, List52))
                  #total += common_elements(List51, List52)
                  #print(common_elements(List61, List62))
                  #total += common_elements(List61, List62)
                  #total += common_elements(List71, List72)
                  #total += common_elements(List81, List82)
                  #print(total)
                  if total == 716:
                     #print("fully matched")
                     file1.write(str(1)+" ")
                  else:
                     #print("Not matched")
                     file1.write(str(0)+" ")
       else:
               #print("Not matched")
               file1.write(str(0)+" ")
                     
    file1.write("\n")
fp.close() 

file1.close()
