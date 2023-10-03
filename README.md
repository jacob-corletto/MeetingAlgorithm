# Collaborators
- Raxel Ortiz raxelortiz7@csu.fullerton.edu

- Jacob Corletto jacob.corletto@gmail.com

- Esteban Zapata eazapata@csu.fullerton.edu



# Description

This code finds the times available for a meeting given the schedules of two people. It takes input from a file called input.txt and writes the output to a file called output.txt.

`Input`

The input file should be in the following format:

```
person_one_schedule
person_one
person_two_schedule
person_two
duration 
```
person_one_schedule is a list of lists where each sublist contains the start and end time of a meeting. The times should be in the format `"HH:MM"`.
person_one is a list containing the start and end time of person one's availability. The times should be in the format `"HH:MM"`.
person_two_schedule is a list of lists where each sublist contains the start and end time of a meeting. The times should be in the format `"HH:MM"`.
person_two is a list containing the start and end time of person two's availability. The times should be in the format `"HH:MM"`.
duration is the duration of the meeting in minutes.


The output file will be a list of lists where each sublist contains the start and end time of a time available for a meeting. The times will be in the format `"HH:MM"`.

# Example

Input:

```[["11:30", "13:00"], ["14:00", "14:30"], ["14:30", "15:00"]]
["9:00", "19:00"]
[["10:00", "11:00"], ["15:00", "16:00"], ["17:00", "18:00"]]
["10:00", "20:00"]
60
```

Output:
```
Case #1: [["13:00", "14:00"], ["16:00", "17:00"]]
```
# Usage
Make sure there is a input.txt file with the agendas that you want to find a free time for

To use the code, run the following command:

`python3 schedule_meeting.py`

This will create the output file output.txt.