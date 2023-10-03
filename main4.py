from datetime import datetime, timedelta
import ast


def mins_hours(minutes):
  """Converts a number of minutes to a time string in the format HH:MM.

  Args:
    minutes: The number of minutes to convert.

  Returns:
    A time string in the format HH:MM.
  """

  hours = minutes // 60
  minutes %= 60

  hours_string = str(hours) if hours >= 10 else "0" + str(hours)
  minutes_string = str(minutes) if minutes >= 10 else "0" + str(minutes)

  return hours_string + ":" + minutes_string


def toMins(time):
  hours, minutes = time.split(':')
  return hours * 60 + minutes


# def toMins(time):
#   time_str = str(time)
#   parsed_time = datetime.strptime(time_str, "%H:%M")
#   # Calculate the total minutes
#   return parsed_time.hour * 60 + parsed_time.minute

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

person_one = ast.literal_eval(str(var1))
person_one_activity = ast.literal_eval(str(var2))
person_two = ast.literal_eval(str(var3))
person_two_activity = ast.literal_eval(str(var4))
duration = ast.literal_eval(str(var5))

merged_activity = sorted(person_one + person_two, key=lambda x: x[0])

person_one_start, person_one_end = toMins(person_one_activity[0]), toMins(person_one_activity[1])
person_two_start, person_two_end = toMins(person_two_activity[0]), toMins(person_two_activity[1])

start_time = max(person)



# start_time = max(toMins(person_one_activity[0]), toMins(person_two_activity[0]))
# int(f"this is the start_time var: {start_time}")

# end_time = min(toMins(person_one_activity[1]), toMins(person_two_activity[1]))
# print(f"this is the end_time var: {end_time}")

# agenda.append([mins_hours(start_time), mins_hours(end_time)])
# print(f"this is the agenda: {agenda}")


start = toMins(agenda[0])
print(f"this is the start var: {start}")

end = toMins(agenda[1])
print(f"this is the end var: {end}")


end_time = end
starting_point = toMins(merged_activity[0][0])

while starting_point < end:
  difference = starting_point - end_time
  if difference >= duration:
    times_available.append([mins_hours(end_time), mins_hours(starting_point)])

  next_ending = toMins(merged_activity[0][1])
  next_start = toMins(merged_activity[1][0])

  starting_point = next_start
  end_time = next_ending

print(times_available)
