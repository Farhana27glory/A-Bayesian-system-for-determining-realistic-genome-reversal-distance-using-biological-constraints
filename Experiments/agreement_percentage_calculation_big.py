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
          List11 = line.strip()
       elif cnt ==1:
          List21 = line.strip()
       elif cnt ==2:
          List31 = line.strip()
       elif cnt ==3:
          List41 = line.strip()
       elif cnt ==4:
          List51 = line.strip()   
       elif cnt ==5:
          List61 = line.strip()
       elif cnt ==6:
          List71 = line.strip()
       elif cnt ==7:
          List81 = line.strip()
          
       elif cnt ==8:
          List91 = line.strip()
       elif cnt ==9:
          List101 = line.strip()
       elif cnt == 10:
          List111 = line.strip()
       
       elif cnt ==11:
          List121 = line.strip()
       elif cnt ==12:
          List131 = line.strip()
       '''
       elif cnt ==13:
          List141 = line.strip()
       elif cnt ==14:
          List151 = line.strip()   
       elif cnt ==15:
          List161 = line.strip()
       elif cnt ==16:
          List171 = line.strip()
       elif cnt ==17:
          List181 = line.strip()
       elif cnt ==18:
          List191 = line.strip()
       elif cnt ==19:
          List201 = line.strip()
       elif cnt ==20:
          List211 = line.strip()
       
       elif cnt ==21:
          List221 = line.strip()
       elif cnt ==22:
          List231 = line.strip()
       elif cnt ==23:
          List241 = line.strip()
       elif cnt ==24:
          List251 = line.strip()
       elif cnt ==25:
          List261 = line.strip()
       elif cnt ==26:
          List271 = line.strip()
       elif cnt ==27:
          List281 = line.strip()
       elif cnt ==28:
          List291 = line.strip()
       elif cnt ==29:
          List301 = line.strip()
       elif cnt ==30:
          List311 = line.strip()
       '''
       cnt +=1

List11 = list(List11.split(" "))
List21 = list(List21.split(" "))
List31 = list(List31.split(" "))
List41 = list(List41.split(" "))
List51 = list(List51.split(" "))
List61 = list(List61.split(" "))
List71 = list(List71.split(" "))
List81 = list(List81.split(" "))
List91 = list(List91.split(" "))
List101 = list(List101.split(" "))
List111 = list(List111.split(" "))
List121 = list(List121.split(" "))
List131 = list(List131.split(" "))
'''
List141 = list(List141.split(" "))
List151 = list(List151.split(" "))
List161 = list(List161.split(" "))
List171 = list(List171.split(" "))
List181 = list(List181.split(" "))
List191 = list(List191.split(" "))
List201 = list(List201.split(" "))
List211 = list(List211.split(" "))
List221 = list(List221.split(" "))
List231 = list(List231.split(" "))
List241 = list(List241.split(" "))
List251 = list(List251.split(" "))
List261 = list(List261.split(" "))
List271 = list(List271.split(" "))
List281 = list(List281.split(" "))
List291 = list(List291.split(" "))
List301 = list(List301.split(" "))
List311 = list(List311.split(" "))
'''



List11 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List11]
List21 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List21]
List31 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List31]
List41 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List41]
List51 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List51]
List61 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List61]
List71 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List71]
List81 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List81]
List91 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List91]
List101 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List101]
List111 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List111]
List121 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List121]
List131 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List131]
'''
List141 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List141]
List151 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List151]
List161 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List161]
List171 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List171]
List181 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List181]
List191 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List191]
List201 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List201]
List211 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List211]
List221 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List221]
List231 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List231]
List241 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List241]
List251 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List251]
List261 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List261]
List271 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List271]
List281 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List281]
List291 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List291]
List301 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List301]
List311 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List311]
'''



List11 = (str_list_to_int_list(List11))
List21 = (str_list_to_int_list(List21))
List31 = (str_list_to_int_list(List31))
List41 = (str_list_to_int_list(List41))
List51 = (str_list_to_int_list(List51))
List61 = (str_list_to_int_list(List61))
List71 = (str_list_to_int_list(List71))
List81 = (str_list_to_int_list(List81))
List91 = (str_list_to_int_list(List91))
List101 = (str_list_to_int_list(List101))
List111 = (str_list_to_int_list(List111))
List121 = (str_list_to_int_list(List121))
List131 = (str_list_to_int_list(List131))
'''
List141 = (str_list_to_int_list(List141))
List151 = (str_list_to_int_list(List151))
List161 = (str_list_to_int_list(List161))
List171 = (str_list_to_int_list(List171))
List181 = (str_list_to_int_list(List181))
List191 = (str_list_to_int_list(List191))
List201 = (str_list_to_int_list(List201))
List211 = (str_list_to_int_list(List211))
List221 = (str_list_to_int_list(List221))
List231 = (str_list_to_int_list(List231))
List241 = (str_list_to_int_list(List241))
List251 = (str_list_to_int_list(List251))
List261 = (str_list_to_int_list(List261))
List271 = (str_list_to_int_list(List271))
List281 = (str_list_to_int_list(List281))
List291 = (str_list_to_int_list(List291))
List301 = (str_list_to_int_list(List301))
List311 = (str_list_to_int_list(List311))
'''


########################## source preprocessing done

def APM(List11,List12,List21,List22,List31,List32,List41,List42,List51,List52, List61,List62, List71,List72, List81, List82, List91, List92, List101, List102, List111, List112, List121, List122,
        List131, List132):

    pivot = len(List21)
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

    
    count = 0
    for i in range(0,len(List71)):
        
            if List71[i]==List72[i]:
                count+=1
        
    f = count/pivot
    cnt+=1
    
    count = 0
    for i in range(0,len(List81)):
        
            if List81[i]==List82[i]:
                count+=1
        
    g = count/pivot
    cnt+=1

    
    count = 0
    for i in range(0,len(List91)):
        
            if List91[i]==List92[i]:
                count+=1
        
    h = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List101)):
        
            if List101[i]==List102[i]:
                count+=1
        
    j = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List111)):
        
            if List111[i]==List112[i]:
                count+=1
        
    k = count/pivot
    cnt+=1

    
    count = 0
    for i in range(0,len(List121)):
        
            if List121[i]==List122[i]:
                count+=1
    l = count/pivot
    cnt+=1
                
    count = 0
    for i in range(0,len(List131)):
        
            if List131[i]==List132[i]:
                count+=1
    m = count/pivot
    cnt+=1         

    '''
    count = 0
    for i in range(0,len(List141)):
        
            if List141[i]==List142[i]:
                count+=1
            
    n = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List151)):
        
            if List151[i]==List152[i]:
                count+=1
        
    o = count/pivot
    cnt+=1

    
    count = 0
    for i in range(0,len(List161)):
        
            if List161[i]==List162[i]:
                count+=1
        
    p = count/pivot
    cnt+=1

    
    count = 0
    for i in range(0,len(List171)):
        
            if List171[i]==List172[i]:
                count+=1
        
    q = count/pivot
    cnt+=1
    
    count = 0
    for i in range(0,len(List181)):
        
            if List181[i]==List182[i]:
                count+=1
        
    r = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List191)):
        
            if List191[i]==List192[i]:
                count+=1
        
    s = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List201)):
        
            if List201[i]==List202[i]:
                count+=1
        
    t = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List211)):
        
            if List211[i]==List212[i]:
                count+=1
        
    u = count/pivot
    cnt+=1


    
    count = 0
    for i in range(0,len(List221)):
        
            if List221[i]==List222[i]:
                count+=1
        
    v = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List231)):
        
            if List231[i]==List232[i]:
                count+=1
        
    w = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List241)):
        
            if List241[i]==List242[i]:
                count+=1
        
    x = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List251)):
        
            if List251[i]==List252[i]:
                count+=1
        
    y = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List261)):
        
            if List261[i]==List262[i]:
                count+=1
        
    z = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List271)):
        
            if List271[i]==List272[i]:
                count+=1
        
    aa = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List281)):
        
            if List281[i]==List282[i]:
                count+=1
        
    bb = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List291)):
        
            if List291[i]==List292[i]:
                count+=1
        
    cc = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List301)):
        
            if List301[i]==List302[i]:
                count+=1
        
    dd = count/pivot
    cnt+=1

    count = 0
    for i in range(0,len(List311)):
        
            if List311[i]==List312[i]:
                count+=1
        
    ee = count/pivot
    cnt+=1
    '''
    
    #print(cnt)
    #total = a+b+c+d
    #total = a+b+c+d+e+f+g+h+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z+aa+bb+cc+dd+ee
    total = a+b+c+d+e+f+g+h+j+k+l+m
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
    List52 = lst[4]
    List62 = lst[5]
    List72 = lst[6]
    List82 = lst[7]
    List92 = lst[8]
    List102 = lst[9]
    List112 = lst[10]
    List122 = lst[11]
    List132 = lst[12]
    '''
    List142 = lst[13]
    List152 = lst[14]
    List162 = lst[15]
    List172 = lst[16]
    List182 = lst[17]
    List192 = lst[18]
    List202 = lst[19]
    List212 = lst[20]
    List222 = lst[21]
    List232 = lst[22]
    List242 = lst[23]
    List252 = lst[24]
    List262 = lst[25]
    List272 = lst[26]
    List282 = lst[27]
    List292 = lst[28]
    List302 = lst[29]
    List312 = lst[30]
    '''
    
    
    List12 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List12)
    List12 = re.sub('[,]', '', List12)
    List22 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List22)
    List22 = re.sub('[,]', '', List22)
    List32 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List32)
    List32 = re.sub('[,]', '', List32)
    List42 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List42)
    List42 = re.sub('[,]', '', List42)
    List52 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List52)
    List52 = re.sub('[,]', '', List52)
    List62 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List62)
    List62 = re.sub('[,]', '', List62)
    List72 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List72)
    List72 = re.sub('[,]', '', List72)
    List82 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List82)
    List82 = re.sub('[,]', '', List82)
    List92 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List92)
    List92 = re.sub('[,]', '', List92)
    List102 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List102)
    List102 = re.sub('[,]', '', List102)
    List112 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List112)
    List112 = re.sub('[,]', '', List112)
    List122 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List122)
    List122 = re.sub('[,]', '', List122)
    List132 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List132)
    List132 = re.sub('[,]', '', List132)
    '''
    List142 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List142)
    List142 = re.sub('[,]', '', List142)
    List152 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List152)
    List152 = re.sub('[,]', '', List152)
    List162 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List162)
    List162 = re.sub('[,]', '', List162)
    List172 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List172)
    List172 = re.sub('[,]', '', List172)
    List182 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List182)
    List182 = re.sub('[,]', '', List182)
    List192 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List192)
    List192 = re.sub('[,]', '', List192)
    List202 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List202)
    List202 = re.sub('[,]', '', List202)
    List212 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List212)
    List212 = re.sub('[,]', '', List212)
    List222 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List222)
    List222 = re.sub('[,]', '', List222)
    List232 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List232)
    List232 = re.sub('[,]', '', List232)
    List242 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List242)
    List242 = re.sub('[,]', '', List242)
    List252 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List252)
    List252 = re.sub('[,]', '', List252)
    List262 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List262)
    List262 = re.sub('[,]', '', List262)
    List272 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List272)
    List272 = re.sub('[,]', '', List272)
    List282 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List282)
    List282 = re.sub('[,]', '', List282)
    List292 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List292)
    List292 = re.sub('[,]', '', List292)
    List302 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List302)
    List302 = re.sub('[,]', '', List302)
    List312 = re.sub(r'(?<=[.,])(?=[^\s])', r' ', List312)
    List312 = re.sub('[,]', '', List312)
    '''


            
    List12 = list(List12.split(" "))
    List22 = list(List22.split(" "))
    List32 = list(List32.split(" "))
    List42 = list(List42.split(" "))
    List52 = list(List52.split(" "))
    List62 = list(List62.split(" "))
    List72 = list(List72.split(" "))
    List82 = list(List82.split(" "))
    List92 = list(List92.split(" "))
    List102 = list(List102.split(" "))
    List112 = list(List112.split(" "))
    List122 = list(List122.split(" "))
    List132 = list(List132.split(" "))
    '''
    List142 = list(List142.split(" "))
    List152 = list(List152.split(" "))
    List162 = list(List162.split(" "))
    List172 = list(List172.split(" "))
    List182 = list(List182.split(" "))
    List192 = list(List192.split(" "))
    List202 = list(List202.split(" "))
    List212 = list(List212.split(" "))
    List222 = list(List222.split(" "))
    List232 = list(List232.split(" "))
    List242 = list(List242.split(" "))
    List252 = list(List252.split(" "))
    List262 = list(List262.split(" "))
    List272 = list(List272.split(" "))
    List282 = list(List282.split(" "))
    List292 = list(List292.split(" "))
    List302 = list(List302.split(" "))
    List312 = list(List312.split(" "))
    '''

    
    
    List12 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List12]
    List22 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List22]
    List32 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List32]
    List42 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List42]
    List52 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List52]
    List62 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List62]
    List72 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List72]
    List82 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List82]
    List92 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List92]
    List102 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List102]
    List112 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List112]
    List122 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List122]
    List132 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List132]
    '''
    List142 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List142]
    List152 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List152]
    List162 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List162]
    List172 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List172]
    List182 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List182]
    List192 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List192]
    List202 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List202]
    List212 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List212]
    List222 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List222]
    List232 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List232]
    List242 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List242]
    List252 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List252]
    List262 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List262]
    List272 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List272]
    List282 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List282]
    List292 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List292]
    List302 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List302]
    List312 =[re.sub('[^-^a-zA-Z0-9]+', '', _) for _ in List312]
    '''
    
    
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
    
    for i in range(0, len(List52)): 
        if i % 2==1: 
            List52[i] = int(List52[i]) 
    
    for i in range(0, len(List62)): 
        if i % 2==1: 
            List62[i] = int(List62[i]) 
    
    for i in range(0, len(List72)): 
        if i % 2==1: 
            List72[i] = int(List72[i])

    for i in range(0, len(List82)): 
        if i % 2==1: 
            List82[i] = int(List82[i]) 

    for i in range(0, len(List92)): 
        if i % 2==1: 
            List92[i] = int(List92[i])

    for i in range(0, len(List102)): 
        if i % 2==1: 
            List102[i] = int(List102[i])
    
    for i in range(0, len(List112)): 
        if i % 2==1: 
            List112[i] = int(List112[i])
            
    for i in range(0, len(List122)): 
        if i % 2==1: 
            List122[i] = int(List122[i]) 
    
    for i in range(0, len(List132)): 
        if i % 2==1: 
            List132[i] = int(List132[i]) 
    '''
    for i in range(0, len(List142)): 
        if i % 2==1: 
            List142[i] = int(List142[i]) 
    
    for i in range(0, len(List152)): 
        if i % 2==1: 
            List152[i] = int(List152[i]) 
    
    for i in range(0, len(List162)): 
        if i % 2==1: 
            List162[i] = int(List162[i]) 

    for i in range(0, len(List172)): 
        if i % 2==1: 
            List172[i] = int(List172[i])

    for i in range(0, len(List182)): 
        if i % 2==1: 
            List182[i] = int(List182[i]) 

    for i in range(0, len(List192)): 
        if i % 2==1: 
            List192[i] = int(List192[i])

    for i in range(0, len(List202)): 
        if i % 2==1: 
            List202[i] = int(List202[i]) 

    for i in range(0, len(List212)): 
        if i % 2==1: 
            List212[i] = int(List212[i])

    
    for i in range(0, len(List222)): 
        if i % 2==1: 
            List222[i] = int(List222[i])
            
    for i in range(0, len(List232)): 
        if i % 2==1: 
            List232[i] = int(List232[i])
            
    for i in range(0, len(List242)): 
        if i % 2==1: 
            List242[i] = int(List242[i])
            
    for i in range(0, len(List252)): 
        if i % 2==1: 
            List252[i] = int(List252[i])
            
    for i in range(0, len(List262)): 
        if i % 2==1: 
            List262[i] = int(List262[i])

    for i in range(0, len(List272)): 
        if i % 2==1: 
            List272[i] = int(List272[i])


    for i in range(0, len(List282)): 
        if i % 2==1: 
            List282[i] = int(List282[i])

    for i in range(0, len(List292)): 
        if i % 2==1: 
            List292[i] = int(List292[i])

    for i in range(0, len(List302)): 
        if i % 2==1: 
            List302[i] = int(List302[i])

            
    for i in range(0, len(List312)): 
        if i % 2==1: 
            List312[i] = int(List312[i])
    '''
            
            
    List12 =(intergenic_conversion(List12))
    List22 =(intergenic_conversion(List22))
    List32 =(intergenic_conversion(List32))
    List42 =(intergenic_conversion(List42))
    List52 =(intergenic_conversion(List52))
    List62 =(intergenic_conversion(List62))
    List72 =(intergenic_conversion(List72))
    List82 =(intergenic_conversion(List82))
    List92 =(intergenic_conversion(List92))
    List102 =(intergenic_conversion(List102))
    List112 =(intergenic_conversion(List112))
    List122 =(intergenic_conversion(List122))
    List132 =(intergenic_conversion(List132))
    '''
    List142 =(intergenic_conversion(List142))
    List152 =(intergenic_conversion(List152))
    List162 =(intergenic_conversion(List162))
    List172 =(intergenic_conversion(List172))
    List182 =(intergenic_conversion(List182))
    List192 =(intergenic_conversion(List192))
    List202 =(intergenic_conversion(List202))
    List212 =(intergenic_conversion(List212))
    List222 =(intergenic_conversion(List222))
    List232 =(intergenic_conversion(List232))
    List242 =(intergenic_conversion(List242))
    List252 =(intergenic_conversion(List252))
    List262 =(intergenic_conversion(List262))
    List272 =(intergenic_conversion(List272))
    List282 =(intergenic_conversion(List282))
    List292 =(intergenic_conversion(List292))
    List302 =(intergenic_conversion(List302))
    List312 =(intergenic_conversion(List312))
    '''
    
    
    return(List12, List22, List32, List42, List52, List62, List72, List82, List92, List102, List112, List122, List132)
    '''
    return(List12, List22, List32, List42, List52, List62, List72, List82, List92, List102, List112, List122, List132, List142, List152, List162, List172, List182, List192, List202,
           List212, List222, List232, List242, List252, List262, List272, List282, List292, List302, List312)
    '''
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
       #List12, List22, List32, List42, List52, List62, List72, List82, List92, List102, List112, List122, List132, List142, List152, List162, List172, List182, List192, List202, List212, List222, List232, List242, List252, List262, List272, List282, List292, List302, List312  = function(my_list)
       List12, List22, List32, List42, List52, List62, List72, List82, List92, List102, List112, List122, List132 = function(my_list)
       cnt +=1 
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42,
                 List51,List52, List61,List62, List71,List72, List81, List82, List91, List92, List101, List102, List111, List112, List121, List122,
        List131, List132, List141, List142, List151, List152, List161, List162, List171, List172, List181, List182, List191, List192, List201, List202, List211, List212, List221, List222, List231, List232,
                      List241, List242, List251, List252, List261, List262, List271, List272, List281, List282, List291, List292, List301, List302, List311, List312)
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42, List51,List52, List61,List62, List71,List72, List81, List82, List91, List92, List101, List102, List111, List112, List121, List122,
                 List131, List132)
       
   if (cnt == 0):
       print("empty file found")
       file1.write(str(0)+" ")
   else:
       
       avg = measure/cnt
       avg = round(avg,2)
       print(avg,"%")
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
       #List12, List22, List32, List42, List52, List62, List72, List82, List92, List102, List112, List122, List132, List142, List152, List162, List172, List182, List192, List202, List212, List222, List232, List242, List252, List262, List272, List282, List292, List302, List312  = function(my_list)
       List12, List22, List32, List42, List52, List62, List72, List82, List92, List102, List112, List122, List132 = function(my_list)
       cnt +=1 
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42,
                 List51,List52, List61,List62, List71,List72, List81, List82, List91, List92, List101, List102, List111, List112, List121, List122,
        List131, List132, List141, List142, List151, List152, List161, List162, List171, List172, List181, List182, List191, List192, List201, List202, List211, List212, List221, List222, List231, List232,
                      List241, List242, List251, List252, List261, List262, List271, List272, List281, List282, List291, List292, List301, List302, List311, List312)
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42, List51,List52, List61,List62, List71,List72, List81, List82, List91, List92, List101, List102, List111, List112, List121, List122,
                 List131, List132)
   if (cnt == 0):
       print("empty file found")
       file1.write(str(0)+" ")
   else:
       
       avg = measure/cnt
       avg = round(avg,2)
       print(avg,"%")
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
       #List12, List22, List32, List42, List52, List62, List72, List82, List92, List102, List112, List122, List132, List142, List152, List162, List172, List182, List192, List202, List212, List222, List232, List242, List252, List262, List272, List282, List292, List302, List312  = function(my_list)
       List12, List22, List32, List42, List52, List62, List72, List82, List92, List102, List112, List122, List132 = function(my_list)
       cnt +=1 
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42,
                 List51,List52, List61,List62, List71,List72, List81, List82, List91, List92, List101, List102, List111, List112, List121, List122,
        List131, List132, List141, List142, List151, List152, List161, List162, List171, List172, List181, List182, List191, List192, List201, List202, List211, List212, List221, List222, List231, List232,
                      List241, List242, List251, List252, List261, List262, List271, List272, List281, List282, List291, List292, List301, List302, List311, List312)
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42, List51,List52, List61,List62, List71,List72, List81, List82, List91, List92, List101, List102, List111, List112, List121, List122,
                 List131, List132)
       
   if (cnt == 0):
       print("empty file found")
       file1.write(str(0)+" ")
   else:
       
       avg = measure/cnt
       avg = round(avg,2)
       print(avg,"%")
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
       #List12, List22, List32, List42, List52, List62, List72, List82, List92, List102, List112, List122, List132, List142, List152, List162, List172, List182, List192, List202, List212, List222, List232, List242, List252, List262, List272, List282, List292, List302, List312  = function(my_list)
       List12, List22, List32, List42, List52, List62, List72, List82, List92, List102, List112, List122, List132 = function(my_list)
       cnt +=1 
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42,
                 List51,List52, List61,List62, List71,List72, List81, List82, List91, List92, List101, List102, List111, List112, List121, List122,
        List131, List132, List141, List142, List151, List152, List161, List162, List171, List172, List181, List182, List191, List192, List201, List202, List211, List212, List221, List222, List231, List232,
                      List241, List242, List251, List252, List261, List262, List271, List272, List281, List282, List291, List292, List301, List302, List311, List312)
       '''
       measure += APM(List11,List12,List21,List22,List31,List32,List41,List42, List51,List52, List61,List62, List71,List72, List81, List82, List91, List92, List101, List102, List111, List112, List121, List122,
                 List131, List132)
       
   if (cnt == 0):
       print("empty file found")
       file1.write(str(0)+"\n")
   else:
       
       avg = measure/cnt
       avg = round(avg,2)
       print(avg,"%")
       file1.write(str(avg)+"\n")
   fp.close()  

file1.close()             
