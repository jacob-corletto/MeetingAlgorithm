import ast

def convert_time_to_minutes(time):
  """Converts a time string in the format "HH:MM" to minutes."""
  hours, minutes = time.split(":")
  return int(hours) * 60 + int(minutes)

def combine_daily_active(person_one, person_two, agenda):
  """Combines the daily active times of two people into a single list."""
  agenda.append(min(person_one[0], person_two[0]))
  agenda.append(max(person_one[1], person_two[1]))

def schedule_meeting(person_one_schedule, person_two_schedule, agenda,
                      duration, times_available):
  """Finds all available meeting times for two people, given their schedules and meeting duration."""

  # Combine the two people's schedules into a single list.
  merged_schedule = person_one_schedule + person_two_schedule

  # Iterate over the schedule, finding all available meeting times.
  for i in range(len(merged_schedule) - 1):
    end_time = convert_time_to_minutes(merged_schedule[i][1])

    # Check if the index of the next event is within bounds.
    if i + 1 < len(merged_schedule):
      start_time = convert_time_to_minutes(merged_schedule[i + 1][0])

      # If there is enough time between the end of the current event and the start of the next event to schedule a meeting, add the available time slot to the list.
      if start_time - end_time >= duration:
        times_available.append([merged_schedule[i][1], merged_schedule[i + 1][0]])


file_path = 'input.txt'
var1 = []
var2 = []
var3 = []
var4 = []
var5 = 0
agenda = []
times_available = []

# Open the file in read mode ('r')
with open(file_path, 'r') as file:
  # Read all lines in the file one by one
  x = 0
  for line in file:
    x += 1
    exec(f"var{x} = line")

person_one_schedule = ast.literal_eval(str(var1))  #[["11:30", "13:00"], ["14:00", "14:30"], ["14:30", "15:00"]]
person_one = ast.literal_eval(str(var2))  #["9:00", "19:00"]
person_two_schedule = ast.literal_eval(str(var3))  
person_two = ast.literal_eval(str(var4))
duration = ast.literal_eval(str(var5))
combine_daily_active(person_one, person_two, agenda)
schedule_meeting(person_one_schedule, person_two_schedule, agenda, duration, times_available)
print(times_available)
