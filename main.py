from datetime import datetime, timedelta
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
    x += 1
    exec(f"var{x} = line")

personOne = ast.literal_eval(str(var1))  
personOne_Activity = ast.literal_eval(str(var2))  
personTwo = ast.literal_eval(str(var3))  
personTwo_Activity = ast.literal_eval(str(var4))
duration = ast.literal_eval(str(var5))


#convert time to minutes for easier comparison



def mins_hours(time):
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

def toMins(time):
  time_str = str(time)
  parsed_time = datetime.strptime(time_str, "%H:%M")
  return parsed_time.hour * 60 + parsed_time.minute

def findAvailableTimeSlots(personOne, personTwo, duration):

  # Find the starting and ending points of the available time slots
  starting = max(toMins(personOne_Activity[0]), toMins(personTwo_Activity[0]))
  ending = min(toMins(personOne_Activity[1]), toMins(personTwo_Activity[1]))

def find_common_meeting_slots(person_a_schedule, person_b_schedule, workday_start, workday_end):
    # Initialize the merged schedule
    merged_schedule = person_a_schedule + person_b_schedule
    merged_schedule.sort(key=lambda x: x[0])  # Sort by start time

    # Initialize common meeting slots
    common_slots = []

    # Initialize availability flags
    person_a_available = workday_start
    person_b_available = workday_start

    # Iterate through the merged schedule
    for meeting in merged_schedule:
        start_time, end_time = meeting

        # Check if there is an available slot for both persons
        if person_a_available < start_time and person_b_available < start_time:
            common_slots.append([mins_hours(max(person_a_available, workday_start)), mins_hours(start_time)])

        # Update availability based on the meeting end time
        person_a_available = max(person_a_available, end_time)
        person_b_available = max(person_b_available, end_time)

    # Check if there is an available slot at the end of the workday
    if person_a_available < workday_end and person_b_available < workday_end:
        common_slots.append([mins_hours(max(person_a_available, workday_start)), mins_hours(workday_end)])

    return common_slots

# Example schedules
person_a_schedule = [[toMins('03:00'),toMins('04:00')]]
person_b_schedule = [[toMins('6:00'),toMins('7:00')]]

workday_start = toMins('03:00')
#supposed to look like person_a_9to5 = [time,time]
workday_end = toMins('08:00')
#i only changed line 72
common_meeting_slots = find_common_meeting_slots(person_a_schedule, person_b_schedule, workday_start, workday_end)
print(common_meeting_slots)