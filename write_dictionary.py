import json

#import os
#from os.path.expanduser("~/Desktop/workout_log/workout_log.py") import class_erg, class_run

class class_erg:
    def __init__(self, meters, split, SR, HR, time):
        self.meters = meters
        self.split = split
        self.SR = SR
        self.HR = HR
        self.time = time
    @classmethod
    def from_input(cls):
        return cls(
            input('meters: '),
            input('split: '), 
            input('SR: '),
            input('HR: '),
            input('time: ')
        )

class class_run:
    def __init__(self, miles, time, HR, elevationChange):
        self.miles = miles
        self.time = time
        self.HR = HR
        self.elevationChange = elevationChange
    @classmethod
    def from_input(cls):
        return cls(
            input('miles: '),
            input('time: '), 
            input('HR: '),
            input('elevationChange: ')
        )



#list of names for known workouts, can grow
dic_known_workouts = {
    'dic_erg_names' : ['Erg','erg','erging','rower'],
    'dic_run_names' : ['Run','run','jog','Jog']
}
with open('dic_known_workouts.json', 'w') as f_dic_known_workouts:
    json.dump(dic_known_workouts, f_dic_known_workouts)

# classes_map = {
#     'dic_erg_names': class_erg, 
#     'dic_run_names': class_run
# }

# with open('classes_map.json', 'w') as f_classes_map:
#     json.dump(classes_map, f_classes_map)