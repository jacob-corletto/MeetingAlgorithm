from datetime import datetime
#import json
import ast

file_path = 'input.txt'

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
personTwo = ast.literal_eval(str(var3))
personTwo_Activity = ast.literal_eval(str(var4))
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

#simple tomins written with datetime library (idk if we can use it but easier than the ladder)
def toMins(time):
  parsed_time = datetime.strptime(time,"%H:%M")
  return parsed_time.hour*60 + parsed_time.minute
  
#Algo part
Answer = []

#find starting point
if toMins(personOne_Activity[0]) <= toMins(personTwo_Activity[0]):
  curr = toMins(personOne_Activity[0])

else:
  curr = toMins(personTwo_Activity[0])

#find ending point
print(curr)

  
# for i in range(len(personOne)):
#   for j in range(len(personOne[i])):
#     personOneTime += toMins(personOne[i][j])



