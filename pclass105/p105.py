import csv
import pandas as pd
import plotly.express as px


with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    filedata=list(reader)
#filedata.pop(0)
data=filedata[0]
total_marks = 0
total_entries = len(data)
print(total_entries)
for marks in data:
    total_marks += int(marks)
print(total_marks)
mean = total_marks / total_entries
print("Mean (Average) is -> "+str(mean))



    
import math
squarelist=[]
for i in data:
  #  a=int((i)-mean(data))
    a=int(i)-float(mean)
    a=a**2
    squarelist.append(a)
    sum=0
    for i in squarelist:
        sum=sum+i

result=sum/i 
sd=math.sqrt(result) 
print(sd)