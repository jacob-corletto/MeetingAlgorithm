from datetime import datetime, timedelta
import ast

class find_common_meeting_slots():
  def __init__(file_path):
    self.file_path = file_path

  var1 = []
  var2 = []
  var3 = []
  var4 = []
  var5 = []
  
  def setup(self,file_path):
    # Open the file in read mode ('r')
    with open(self.file_path, 'r') as file:
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

  # def findAvailableTimeSlots(personOne, personTwo, duration):
  
  #   # Find the starting and ending points of the available time slots
  #   starting = max(toMins(personOne_Activity[0]), toMins(personTwo_Activity[0]))
  #   ending = min(toMins(personOne_Activity[1]), toMins(personTwo_Activity[1]))

  # def find_common_meeting_slots(person_a_schedule, person_b_schedule, workday_start, workday_end):
      # Initialize the merged schedule
  merged_schedule = personOne + personTwo
  merged_schedule.sort(key=lambda x: x[0])  # Sort by start time

  # Initialize common meeting slots
  common_slots = []

  #find start
  workday_start = max(toMins(personOne_Activity[0]), toMins(personTwo_Activity[0]))
  workday_end = min(toMins(personOne_Activity[1]), toMins(personTwo_Activity[1]))

  # Initialize availability flags
  personOne_available = workday_start
  personTwo_available = workday_start

  # Iterate through the merged schedule
  for meeting in merged_schedule:
      start_time, end_time = meeting

      # Check if there is an available slot for both persons
      if personOne_available < start_time and personTwo_available < start_time:
          common_slots.append([mins_hours(max(personOne_available, workday_start)), mins_hours(start_time)])

      # Update availability based on the meeting end time
      person_a_available = max(personOne_available, end_time)
      person_b_available = max(personTwo_available, end_time)

  # Check if there is an available slot at the end of the workday
  if personOne_available < workday_end and personTwo_available < workday_end:
      common_slots.append([mins_hours(max(personOne_available, workday_start)), mins_hours(workday_end)])

  print(common_slots)
  # return common_slots
def main():
  case1 = find_common_meeting_slots('input.txt')
  print(case1)

if __name__=='__main__':
  main()
# # Example schedules
# person_a_schedule = [[toMins('03:00'),toMins('04:00')]]
# person_b_schedule = [[toMins('6:00'),toMins('7:00')]]

# workday_start = toMins('03:00')
# workday_end = toMins('08:00')

# common_meeting_slots = find_common_meeting_slots(person_a_schedule, person_b_schedule, workday_start, workday_end)
# print(common_meeting_slots)