
#the first user prompt after starting the code

purpose = input('Update (U) or Examine (E)? ')
if(purpose == 'U'):
     exercise = input('Exercise? ')

#list of names for known workouts, can grow
#erg_names = ['Erg','erg','erging','rower']
#run_names = ['Run','run','jog','Jog']
#known_workouts = [erg_names,run_names]
#
#if any(exercise in sub for sub in known_workouts):
#    print("NAME OF LIST?")

dic_known_workouts = {
    'dic_erg_names' : ['Erg','erg','erging','rower'],
    'dic_run_names' : ['Run','run','jog','Jog']
}
sport = [k for k, v in dic_known_workouts.items() if v == exercise]
classes = {"erg": erg, "run": run}
obj = classes[sport]

#list_of_keys = [key
#    for key, list_of_values in dic_known_workouts.items()
#    if exercise in list_of_values]
#if list_of_keys:


class Foo:
    ...

class Bar:
    ...

