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


#convert time to minutes for easier comparison 
def convertToMins(time):
    hours, minutes = list(map(int, time.split(':')))
    return hours * 60 + minutes


def main():
    print("Hello World!")