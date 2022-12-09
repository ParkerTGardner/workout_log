import json

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

with open('classes_map.json', 'w') as f_classes_map:
    json.dump(classes_map, f_classes_map)