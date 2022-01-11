#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 18:26:15 2021

@author: gloryfz
"""

import random
import math
import sys
import os
import re
from datetime import datetime

def createList(r1, r2): 
    return [item for item in range(r1, r2+1)] 

def reverse_sign(l, start, end): 
    for i in range(start, end+1): 
         l[i] *= (-1)
         i=i+1
    return l

def negative(p):
      k = -(p)
      return k

def reverse(l, first=0, last=-1):
 #for i in range(1): 
   #reverse_sign(l, first, last)
 #reverse_sign(l, first, last)
 if (first >= last): return
 #reverse_sign(l, first, last)   
 l[first], l[last] = l[last], l[first]
 #reverse_sign(l, first, last)
 reverse(l, first+1, last-1)
 
 
      
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


def main():
    ############  gene number
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)

    r1, r2 = 1, 60
    
    
    ListA = (createList(r1, r2)) 
    index=len(ListA)
    #print(ListA) 
    
    
    i = 1
    while i < 2*index-2: 
     ############# intergenic regions
     s=1
     ListA.insert(i, '*'+str(s))
     i += 2
    print(ListA) 
    
    output = [str(x) for x in ListA] 
    #print(output)
        
    InputA =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in output]
    for i in range(0, len(InputA)): 
     if i % 2==0: 
        InputA[i] = int(InputA[i]) 
    
    InputA =(intergenic_conversion(InputA))
    #print(InputA) 
    
    reversal_count = 0
    length_limit= 55
    while (reversal_count < length_limit):
        # randomly generate a reversal
        # generate the range
        s = random.randint(0,(len(InputA)-1))
        r = random.randint(0,(len(InputA)-1))
        #print(s, r)
        if (abs(s-r) >= 2) and (abs(s-r)+0 < len(InputA)):
            reverse_sign(InputA,min(r,s),max(r,s)) 
            reverse(InputA,min(r,s),max(r,s))
            reversal_count +=1
            #print(InputA)

   
    Final_Input = InputA
    List_Source = InputA
    
    reversal_count_1 = 0
    ################## reversal length
    length_limit_1= 4
    result_file = open('transformations.txt', 'w')
    #result_file1 = open('Final_result1.txt', 'w')
    #result_file2 = open('Final_result2.txt', 'w')
    result_file.write(str(Final_Input)+'\n')
    #result_file1.write(str(Final_Input)+'\n')
    #print(List_Source)
    
    
    ###############################
    ##############################  destination genome processing ##########################
    
    
    ListA = List_Source
    ListB = []

    count = 0
    
    for k in range(len(ListA)):
          if ListA[k] == 0:
             count +=1 
          else:
             #print(count)
             ListB.append(count)
             k+=1
             count = 0
        
    ListB.append(count)
    
    ListA = [i for i in ListA if i != 0]
    #print(ListA)
    pivot = len(ListA)
    
    ListC = [str(x) for x in ListB]
    #print(ListC)
    
    ListP = ["*"]
    aces = ["*" + x for x in ListC]
    #print(aces)
    
               
    Combined_List = [None]*(len(aces)+len(ListA))
    Combined_List[::2] = aces
    Combined_List[1::2] = ListA  
    
    #print(Combined_List)
    
    
    
    result_file1 = open('Final_result2.txt', 'w')
    result_file1.write(str(Combined_List))
    result_file1.close()
          
    with open('Final_result2.txt') as f:
        genome = f.read()
        #print(genome)
    
    genome = re.sub(r'(?<=[.,])(?=[^\s])', r' ', genome)
    genome = re.sub('[,]', '', genome)
    
    #print(genome)
    
    genome = re.sub(r'\[(?:[^\]|]*\|)?([^\]|]*)\]', r'\1', genome)
    genome = genome.replace('\'','')
    
    #genome = re.sub('[,]', '', genome)
    
    #print(genome)
    result_file2 = open('testvvv.txt', 'w')
    result_file2.write(str(pivot)+'\n')
    result_file2.write(str(genome))
    
    #########################################  source genome processing done######################
    
    
    
    
    #######################################   destination genome creating #######################
    while (reversal_count_1 < length_limit_1):
        s = random.randint(0,(len(Final_Input)-1))
        r = random.randint(0,(len(Final_Input)-1))
        #print(s, r)
        if (abs(s-r) >= 2) and (abs(s-r)+0 < len(Final_Input)):
            ### have to change this parameter when reversal length parameter is changed
            if (reversal_count_1 != 3):  
                reverse_sign(Final_Input,min(r,s),max(r,s)) 
                reverse(Final_Input,min(r,s),max(r,s))
                reversal_count_1 +=1
                result_file.write(str(Final_Input)+'\n')
                #print(Final_Input)
            else:
                reverse_sign(Final_Input,min(r,s),max(r,s)) 
                reverse(Final_Input,min(r,s),max(r,s))
                reversal_count_1 +=1
                result_file.write(str(Final_Input)+'\n')
                #result_file2.write(str(Final_Input)+'\n')
                #print(Final_Input)
                List_destination = Final_Input
            
    result_file.close()

    List_final = List_destination
    ##########################
    
    def adjacency(Lis):
        
        ListD = []
        count = 0
        
        for k in range(len(List_destination)):
              if List_destination[k] == 0:
                 count +=1 
              else:
                 #print(count)
                 ListD.append(count)
                 k+=1
                 count = 0
            
        ListD.append(count)
    #print(ListA)
    
    
        ListD = ListD[1:-1]
        #print(ListD)
    
        ListG = [i for i in List_destination if i != 0]
        #print(ListG)
        pivot = len(ListG)
    
    
        with open('adjvvv.txt', 'w') as f:
           for index in range(len(ListG)+1):
              f.write(str(ListG[index]) + " " + str(ListG[index+1]) + " " + str(ListD[index]) + "\n")
              f.write(str(negative(ListG[index+1])) + " " + str(negative(ListG[index])) + " " + str(ListD[index]) + "\n")
        f.close()
    ###############################
    ##############################  destination genome processing ##########################

    #print(List_destination)  
    
    ListA = List_destination
    ListB = []

    count_1 = 0
    
    for k in range(len(ListA)):
          if ListA[k] == 0:
             count_1 +=1 
          else:
             #print(count)
             ListB.append(count_1)
             k+=1
             count_1 = 0
        
    ListB.append(count_1)
    
    ListA = [i for i in ListA if i != 0]
    #print(ListA)
    pivot = len(ListA)
    
    ListC = [str(x) for x in ListB]
    #print(ListC)
    
    ListP = ["*"]
    aces = ["*" + x for x in ListC]
    #print(aces)
    
               
    Combined_List = [None]*(len(aces)+len(ListA))
    Combined_List[::2] = aces
    Combined_List[1::2] = ListA  
    
    #print(Combined_List)
    
    
    
    result_file1 = open('Final_result2.txt', 'w')
    result_file1.write(str(Combined_List))
    result_file1.close()
          
    with open('Final_result2.txt') as f:
        genome = f.read()
        #print(genome)
    
    genome = re.sub(r'(?<=[.,])(?=[^\s])', r' ', genome)
    genome = re.sub('[,]', '', genome)
    
    #print(genome)
    
    genome = re.sub(r'\[(?:[^\]|]*\|)?([^\]|]*)\]', r'\1', genome)
    genome = genome.replace('\'','')
    
    #genome = re.sub('[,]', '', genome)
    
    #print(genome)
   # result_file2 = open('testvvv.txt', 'w')
    #result_file2.write(str(pivot)+'\n')
    result_file2.write('\n' + str(genome))
    result_file2.close()
    #f.close()

    adjacency(List_final)


if __name__ == "__main__":
    main()
