
#the first user prompt after starting the code
purpose = input("Update (1) or Examine (2)? ")
if(purpose == 1):
    exercise = input("Exercise? ")
#list of names for known workouts, can grow
known_workouts = ['Erg','erg','erging','Run','run','jog','Jog']
class_known_workouts = ['Erg','erg','erging','Run','run','jog','Jog']



def check_workouts(exercise_now):
    #exit code for starting the known workout class, or adding a workout, or third option
    if exercise_now in known_workouts:
        #start to find the right class to prompt user inputs
        print("Known workout! Tell me more:")
        #open the right csv file
        #use the right class to gather info
        return known_workouts.index(exercise)
    else:
        addOrnot = input("Unknown workout! Would you like to add? y/n")
        if(addOrnot == y):
            return 2
            #return the exit code that starts the add workout program
            #go through procedure of adding workout
        else:
            return strange
            #not sure what to do n the case where they dont add.
            #maybe ask if they want to update with a different workout or examine, or leave.
            #return the exit code that does this^

#def note
#def last(workout, total/average/print, days, counts)



with open (saveAddr+".csv",'a'): 
    month = data['month_number'].tolist()

with open('test.txt', 'r') as text:
    lines = text.readlines()
    for x in lines:
        if x.startswith('Meters'):
            vec_meters = text_file.read().split(',').
    vec_split = text_file.read().split(',').
    vec_strokeRate = text_file.read().split(',').
    vec_HR = text_file.read().split(',').
    vec_time = text_file.read().split(',').

class erg:
    def __init__(self, meters, split, strokeRate, HR, time):
        self.meters = input("meters: ")
        self.split = input("split: ")
        self.strokeRate = input("strokeRate: ")
        self.HR = input("HR: ")
        self.time = input("time: ")
    def append(self):
        vec_meters.append(meters)
        vec_split.append(split)
        vec_strokeRate.append(strokeRate)
        vec_HR.append(HR)
        vec_time.append(time)