import json
import pickle
#import os
#import sys

#print (os.getcwd())
#my_dir = os.path.expanduser('~/Desktop/shape_log/')
# sys.path is a list of absolute path strings.
#sys.path.append(my_dir+'shape_log.py')
#print(my_dir+'shape_log.py')

from class_holder import class_erg, class_run

#list of names for known workouts, can grow
dic_known_workouts = {
    'dic_erg_names' : ['Erg','erg','erging','rower'],
    'dic_run_names' : ['Run','run','jog','Jog']
}
with open('dic_known_workouts.json', 'w') as f_dic_known_workouts:
    json.dump(dic_known_workouts, f_dic_known_workouts)

classes_map = {
    'dic_erg_names': class_erg,
    'dic_run_names': class_run
}

with open('classes_map.p', 'wb') as f_classes_map:
     pickle.dump(classes_map, f_classes_map, protocol=pickle.HIGHEST_PROTOCOL)