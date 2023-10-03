import ast

def to_hours(time):
  '''Converts a time in minutes to a string in the format "HH:MM".'''
  hours = time // 60
  minutes = time % 60
  if hours < 10:
    hours = '0' + str(hours)
  else:
    hours = str(hours)
  if minutes < 10:
    minutes = '0' + str(minutes)
  else:
    minutes = str(minutes)
  return hours + ':' + minutes

def to_mins(time):
  """Converts a time string in the format "HH:MM" to minutes."""
  hours, minutes = time.split(":")
  return int(hours) * 60 + int(minutes)

def combine_daily_active(person_one, person_two, agenda):
  """Combines the daily active times of two people into a single list
  uses to_mins to conver person_one and person_two into minutes and 
  compares them so that we can determin our start time and out end time."""
  if (to_mins(person_one[0]) > to_mins(person_two[0])):
      agenda.append(person_one[0])
  elif (to_mins(person_one[0]) < to_mins(person_two[0])):
      agenda.append(person_two[0])
  elif (to_mins(person_one[0]) == to_mins(person_two[0])):
      agenda.append(person_one[0])
  
  if (to_mins(person_one[1]) < to_mins(person_two[1])):
      agenda.append(person_one[1])
  elif (to_mins(person_one[1]) > to_mins(person_two[1])):
      agenda.append(person_two[1])
  elif (to_mins(person_one[1]) == to_mins(person_two[1])):
      agenda.append(person_one[1])
          

def schedule_meeting(person_one_schedule, person_two_schedule, agenda,
                      duration, times_available):
  '''Finds the times available for a meeting given the schedules of two people.'''
#create variables to store the earliest start time and the latest end time for usage later
  earliest_start = to_mins(agenda[0])
  latest_end = to_mins(agenda[1])

#we are going to merge all the schedules into one list and sort them by the start time so that we can see
#the times that are available
  merged_schedule = sorted(person_one_schedule + person_two_schedule, key=lambda x: x[0])

  end = earliest_start
#we will loop through the merged schedule and compare the end time to the start time of the next meeting
  for i in range(len(merged_schedule)):
      start_time = to_mins(merged_schedule[i][0])
#we will find the difference between the start time and the end time and if the difference is greater than or equal to the duration
      diff = start_time - end
      if diff >= duration:
#we will append the times available to the times_available list
          times_available.append([to_hours(end), merged_schedule[i][0]])
#we will update the end time to the end time of the current meeting
      end = max(end, to_mins(merged_schedule[i][1]))
#we will check if the latest end time minus the end time is greater than or equal to the duration
  if latest_end - end >= duration:
#we will append the times available to the times_available list
      times_available.append([to_hours(end), agenda[1]])

  return times_available

 

#make some lists to store the data that we will take from the file
var1 = []
var2 = []
var3 = []
var4 = []
var5 = 0
agenda = []
times_available = []
# Opens the file in read mode ('r') so that we can read its contents
with open("input.txt") as file:
# Read all lines in the file one by one so that we can store them in variables
  x = 1
  counter = 1
#we will write to the output file
  with open("output.txt", "w") as f:
    f.write("")
#we will read the input file
  for line in file:
    if line == "\n":
      x = 1
      continue
    exec(f"var{x} = line")

    if x % 5 == 0:
#we will use ast.literal_eval to convert the string to lists and we will store them in variables created earlier
      person_one_schedule = ast.literal_eval(str(var1))  #[["11:30", "13:00"], ["14:00", "14:30"], ["14:30", "15:00"]]
      person_one = ast.literal_eval(str(var2))  #["9:00", "19:00"]
      person_two_schedule = ast.literal_eval(str(var3))  
      person_two = ast.literal_eval(str(var4))
      duration = ast.literal_eval(str(var5))
#we will call the functions to find the times available
      combine_daily_active(person_one, person_two, agenda)
      schedule_meeting(person_one_schedule, person_two_schedule, agenda, duration, times_available)

#we will write the output to the output file
      with open("output.txt", "a") as f:
        f.write("Case #" + str(counter) + ": " + str(times_available) + "\n")

#we will reset the lists and variables so that we can used them for the other test cases
      var1 = []
      var2 = []
      var3 = []
      var4 = []
      var5 = 0
      agenda = []
      times_available = []
      person_one_schedule = ast.literal_eval(str(var1))  #[["11:30", "13:00"], ["14:00", "14:30"], ["14:30", "15:00"]]
      person_one = ast.literal_eval(str(var2))  #["9:00", "19:00"]
      person_two_schedule = ast.literal_eval(str(var3))  
      person_two = ast.literal_eval(str(var4))
      duration = ast.literal_eval(str(var5))
      counter += 1
      x = 1
      continue
    x += 1
