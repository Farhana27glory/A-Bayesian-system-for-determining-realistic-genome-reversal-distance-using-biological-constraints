#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:25:31 2021

@author: gloryfz
"""

import re
import math


#################  source preprocessing from the file
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
with open('transformations.txt') as fp:
   cnt = 0
   for line in fp:
       #print("Line {}: {}".format(cnt, line.strip()))
       if cnt == 0:
          Lis11 = line.strip()
       elif cnt ==1:
          Lis21 = line.strip()
       elif cnt ==2:
          Lis31 = line.strip()
       elif cnt ==3:
          Lis41 = line.strip()
       '''
       elif cnt ==4:
          Lis51 = line.strip()   
       elif cnt ==5:
          Lis61 = line.strip()
       '''
       cnt +=1

List11 = list(Lis11.split(" "))
List21 = list(Lis21.split(" "))
List31 = list(Lis31.split(" "))
List41 = list(Lis41.split(" "))
#List51 = list(Lis51.split(" "))
#List61 = list(Lis61.split(" "))


List11 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List11]
List21 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List21]
List31 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List31]
List41 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List41]
#List51 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List51]
#List61 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List61]


List11 = (str_list_to_int_list(List11))
List21 = (str_list_to_int_list(List21))
List31 = (str_list_to_int_list(List31))
List41 = (str_list_to_int_list(List41))
#List51 = (str_list_to_int_list(List51))
#List61 = (str_list_to_int_list(List61))     


########################## source preprocessing done


#def APM(List11,List12,List21,List22,List31,List32,List41,List42,List51,List52,List61,List62):
def APM(List11,List12,List21,List22,List31,List32,List41,List42):
        
    pivot = len(List11)
    cnt = 0
    count = 0
    for i in range(0,len(List21)):
        
            if List21[i]==List22[i]:
                count+=1
    a = count/pivot
    cnt+=1
                
    count = 0
    for i in range(0,len(List31)):
        
            if List31[i]==List32[i]:
                count+=1
    b = count/pivot
    cnt+=1         
    
    count = 0
    for i in range(0,len(List41)):
        
            if List41[i]==List42[i]:
                count+=1
            
    c = count/pivot
    cnt+=1

    '''
    count = 0
    for i in range(0,len(List51)):
        
            if List51[i]==List52[i]:
                count+=1
        
    d = count/pivot
    cnt+=1
    
    count = 0
    for i in range(0,len(List61)):
        
            if List61[i]==List62[i]:
                count+=1
        
    e = count/pivot
    cnt+=1
    '''
    #print(cnt)
    #total = a+b+c+d+e
    total = a+b+c
    division = cnt
    percentage = total/(division)*100
    return (percentage)
         
 


########################  destination preprocessing 
 
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
    
    
    
    #return(List12, List22, List32, List42, List52, List62)
    return(List12, List22, List32, List42)

    #print("List72 = ", List72)
########################## destination ptocessing done    

file1 = open('PM_final.txt', 'a+')
with open('APM_1.txt') as fp:
   cnt = 0
   measure = 0
   avg = 0   
   for line in fp:
       #print("Line {}: {}".format(cnt, line.strip())) 
       my_list = line.split("->")
       #print(my_list)
       #List12, List22, List32, List42, List52, List62 = function(my_list)
       List12, List22, List32, List42 = function(my_list)
       cnt +=1
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42,
                 List51,List52,List61,List62)
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42)
   if (cnt == 0):
       #print("empty file found")
       file1.write(str(0)+" ")
   else:
       
       avg = measure/cnt
       avg = round(avg,2)
       #print(avg,"%")
       file1.write(str(avg)+" ")
   fp.close()  
   
   
with open('APM_5.txt') as fp:
   cnt = 0
   measure = 0
   avg = 0   
   for line in fp:
       #print("Line {}: {}".format(cnt, line.strip())) 
       my_list = line.split("->")
       #print(my_list)
       #List12, List22, List32, List42, List52, List62 = function(my_list)
       List12, List22, List32, List42 = function(my_list)
       cnt +=1
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42,
                 List51,List52,List61,List62)
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42)
   if (cnt == 0):
       #print("empty file found")
       file1.write(str(0)+" ")
   else:
       
       avg = measure/cnt
       avg = round(avg,2)
       #print(avg,"%")
       file1.write(str(avg)+" ")
   fp.close() 
   #print(line_count)


with open('APM_15.txt') as fp:
   cnt = 0
   measure = 0
   avg = 0   
   for line in fp:
       #print("Line {}: {}".format(cnt, line.strip())) 
       my_list = line.split("->")
       #print(my_list)
       #List12, List22, List32, List42, List52, List62 = function(my_list)
       List12, List22, List32, List42 = function(my_list)
       cnt +=1
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42,
                 List51,List52,List61,List62)
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42)
   if (cnt == 0):
       #print("empty file found")
       file1.write(str(0)+" ")
   else:
       
       avg = measure/cnt
       avg = round(avg,2)
       #print(avg,"%")
       file1.write(str(avg)+" ")
   fp.close() 

with open('APM_25.txt') as fp:
   cnt = 0
   measure = 0
   avg = 0   
   for line in fp:
       #print("Line {}: {}".format(cnt, line.strip())) 
       my_list = line.split("->")
       #print(my_list)
       #List12, List22, List32, List42, List52, List62 = function(my_list)
       List12, List22, List32, List42 = function(my_list)
       cnt +=1
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42,
                 List51,List52,List61,List62)
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42)
   if (cnt == 0):
       #print("empty file found")
       file1.write(str(0)+" ")
   else:
       
       avg = measure/cnt
       avg = round(avg,2)
       #print(avg,"%")
       file1.write(str(avg)+"\n")
   fp.close()
   
file1.close()             
