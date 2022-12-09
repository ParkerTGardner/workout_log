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


def check_workouts(exercise_now):
    sport = [key for key, v in dic_known_workouts.items() if exercise_now in v]
    if sport:
        print("Known workout! Tell me more:")
        return True
    else:
        addOrNot = input("Unknown workout! Would you like to add it? (y/n): ")
        if(addOrNot == 'y'):
            #function for creating workout class nd writing a csv for furture storage
            new_workout_type
            return True
        else:
            continueOrNot = input("Record another workout? (y/n): ")
            if(continueOrNot == 'n'):
                #some redundancies here with changing global to false and returnng false
                global keepGoing
                keepGoing = False
                return False
            else:
                keepGoing = True
                return True


def record_exercise(exercise_now):
    sport = [key for key, v in dic_known_workouts.items() if exercise_now in v][0]
    obj = classes_map[sport].from_input()
    #add workout to the correct csv
    store_workout
    #add workout to tbeautiful text file
    publish_workout

def store_workout():
    #publish to beautiful text file
    #gonna be a function built on pandas
    i = 123 
def publish_workout():
    #publish to beautiful text file
    i = 123

def new_workout_type():
    #update the dictionary
    #update the classes_map
    #create a csv with proper columns
    i = 123


#list of names for known workouts, can grow
dic_known_workouts = {
    'dic_erg_names' : ['Erg','erg','erging','rower'],
    'dic_run_names' : ['Run','run','jog','Jog']
}
classes_map = {'dic_erg_names': class_erg, 'dic_run_names': class_run}

#the first user prompt after starting the code
purpose = input('Update (U) or Examine (E)? ')

if(purpose == 'U'):
    keepGoing = True

while(keepGoing == True):
    exercise = input('Exercise? ')
    if not check_workouts(exercise):
        break
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