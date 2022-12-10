import json
import pickle

from class_holder import *
from def_holder import *

#with open('classes_map.json') as f_classes_map:
#    classes_map = json.load(f_classes_map)

file1 = open("dic_known_workouts.json")
dic_known_workouts = json.load(file1)

#the first user prompt after starting the code
purpose = input('Update (U) or Examine (E)? ')

if(purpose == 'U'):
    keepGoing = True

while(keepGoing == True):
    exercise = input('Exercise? ')
    if(check_workouts(exercise)==0):
        break
    elif(check_workouts(exercise)==2):
        new_workout_type("dic_known_workouts.json")

    event = record_exercise(exercise)



print("Go drink some water")



# #def note
# #def last(workout, total/average/print, days, counts)



# with open (saveAddr+'.csv','a'): 
#     month = data['month_number'].tolist()

# with open('test.txt', 'r') as text:
#     lines = text.readlines()
#     for x in lines:
#         if x.startswith('Meters'):
#             vec_meters = text_file.read().split(',').
#     vec_split = text_file.read().split(',').
#     vec_strokeRate = text_file.read().split(',').
#     vec_HR = text_file.read().split(',').
#     vec_time = text_file.read().split(',').