#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 21:23:24 2021

@author: gloryfz
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 21:46:39 2021

@author: gloryfz
"""

'''
with open('Top_5_results_updated.txt') as f:
    my_string = f.readline()
my_list = my_string.split("->")
'''

result_file1 = open('APM_1.txt', 'w')

with open('Top_1_result_updated.txt') as fp:
   cnt = 0
   rev = 13
   #rev = 6
   #rev = 8
   
   for line in fp:
       #print("Line {}: {}".format(cnt, line.strip()))
       length = 0
       cnt +=1
       #my_list = line.split("->")
       
       length = line.count("->")
       #print(length)
       #print(line)
       if length == rev:
           
           result_file1.write(str(line))
       #function(my_list)
       
   fp.close()  
   #print(line_count)
result_file1.close() 

result_file1 = open('APM_5.txt', 'w')
length = 0
with open('Top_5_results_updated.txt') as fp:
   cnt = 0
   rev = 13
   #rev = 6
   #rev = 8
   #length = 0
   for line in fp:
       #print("Line {}: {}".format(cnt, line.strip()))
       length = 0
       cnt +=1
       #my_list = line.split("->")
       
       length = line.count("->")
       #print(length)
       #print(line)
       if length == rev:
           
           result_file1.write(str(line))
       #function(my_list)
       
   fp.close()  
   #print(line_count)
result_file1.close() 


result_file1 = open('APM_15.txt', 'w')

with open('Top_15_results_updated.txt') as fp:
   cnt = 0
   rev = 13
   #rev = 6
   #rev = 8
   #length = 0
   for line in fp:
       #print("Line {}: {}".format(cnt, line.strip()))
       length = 0
       cnt +=1
       #my_list = line.split("->")
       
       length = line.count("->")
       #print(length)
       #print(line)
       if length == rev:
           
           result_file1.write(str(line))
       #function(my_list)
       
   fp.close()  
   #print(line_count)
result_file1.close() 

result_file1 = open('APM_25.txt', 'w')

with open('Top_25_results_updated.txt') as fp:
   cnt = 0
   rev = 13
   #rev = 6
   #rev = 8
   #length = 0
   for line in fp:
       #print("Line {}: {}".format(cnt, line.strip()))
       length = 0
       cnt +=1
       #my_list = line.split("->")
       
       length = line.count("->")
       #print(length)
       #print(line)
       if length == rev:
           
           result_file1.write(str(line))
       #function(my_list)
       
   fp.close()  
   #print(line_count)

result_file1 = open('APM_40.txt', 'w')
with open('Top_40_results_updated.txt') as fp:
   cnt = 0
   rev = 13
   #rev = 6
   #rev = 8
   #length = 0
   for line in fp:
       #print("Line {}: {}".format(cnt, line.strip()))
       length = 0
       cnt +=1
       #my_list = line.split("->")
       
       length = line.count("->")
       #print(length)
       #print(line)
       if length == rev:
           
           result_file1.write(str(line))
       #function(my_list)
       
   fp.close()  
   #print(line_count)

result_file1.close()

