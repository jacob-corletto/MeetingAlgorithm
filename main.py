import datetime
#import json

file_path = 'input.txt'
file_content = []

# Open the file in read mode ('r')
with open(file_path, 'r') as file:
    # Read the entire file content into a string
    file_content = file.readlines()

for i in range(len(file_content)):
  print(i, file_content[i])  
    

def sorter(u):
  print("will do somthing")
  print("this will do something too")
