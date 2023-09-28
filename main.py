from datetime import datetime
#import json
import ast

file_path = 'input.txt'
file_content = []

var1 = []
var2 = []
var3 = []
var4 = []
var5 = []

# Open the file in read mode ('r')
with open(file_path, 'r') as file:
    # Read all lines in the file one by one
    x = 0
    for line in file:
        x+=1
        exec(f"var{x} = line")

personOne = ast.literal_eval(str(var1))
personOne_Activity = ast.literal_eval(str(var2))
personeTwo = ast.literal_eval(str(var3))
personeTwo_Activity = ast.literal_eval(str(var4))
duration = ast.literal_eval(str(var5))


# Print the contents of the file to the console
# for i in range(len(file_content)):
#   print(i, file_content[i])  

#convert time to minutes for easier comparison 
def convertToMins(time):
    hours, minutes = list(map(int, time.split(':')))
    return hours * 60 + minutes

def convertlistToMins(lst):
    return [[convertToMins(j) for j in i] for i in lst]

def converminstohours(list):
    hours = minutes // 60
    minutes = minutes % 60
    tostr = '0' + str(hours) if minutes < 10 else str(hours)
    return tostr + ':' + str(minutes)

# Algo part
datestring = "5:00"
parsed_time = datetime.strptime(datestring, "%H:%M")
total_minutes = parsed_time.hour * 60 + parsed_time.minute
print(total_minutes)

datestring2 = "9:00"
parsed_time2 = datetime.strptime(datestring2, "%H:%M")
total_minutes2 = parsed_time2.hour * 60 + parsed_time2.minute
print(total_minutes2)

datestring = start 
datestring2 = end 

while start != end:
  



