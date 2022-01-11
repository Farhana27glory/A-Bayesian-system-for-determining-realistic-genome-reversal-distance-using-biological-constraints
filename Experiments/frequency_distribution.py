result_file1 = open('freq_percentage_Top_1_5_15_25.txt', 'a+')
pivot = 0
with open('Top_1_result_updated.txt') as fp:
   cnt = 0
   rev = 5
   #rev = 6
   #rev = 8
   
   for line in fp:
       length = 0
       cnt +=1
       
       length = line.count("->")
       #print(length)
       if length == rev:
           pivot =+ 1
           #print(pivot)
   result_file1.write(str(pivot)+" ")
       
   fp.close()  
   
pivot1 = 0
with open('Top_5_results_updated.txt') as fp:
   cnt = 0
   rev = 5
   #rev = 6
   #rev = 8
   
   for line in fp:
       length = 0
       cnt +=1
       length = line.count("->")
       #print(length)
       #print(line)
       if length == rev:
           pivot1 = pivot1 + 1
           #print(pivot1)
            
           #result_file1.write("found" +" ") 
   result_file1.write(str(pivot1)+" ")
   fp.close()


pivot2 = 0
with open('Top_15_results_updated.txt') as fp:
   cnt = 0
   rev = 5
   #rev = 6
   #rev = 8
   
   for line in fp:
       length = 0
       cnt +=1
       length = line.count("->")
       #print(length)
       #print(line)
       if length == rev:
           pivot2 = pivot2 + 1
           #print(pivot1)
            
           #result_file1.write("found" +" ") 
   result_file1.write(str(pivot2)+" ")
   fp.close()


pivot3 = 0
with open('Top_25_results_updated.txt') as fp:
   cnt = 0
   rev = 5
   #rev = 6
   #rev = 8
   
   for line in fp:
       length = 0
       cnt +=1
       length = line.count("->")
       #print(length)
       #print(line)
       if length == rev:
           pivot3 = pivot3 + 1
           #print(pivot1)
            
           #result_file1.write("found" +" ") 
   result_file1.write(str(pivot3)+"\n")
   fp.close()

result_file1.close() 
