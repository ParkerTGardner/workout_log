import json


class BaseClass(object):
    def __init__(self, classtype):
        self._type = classtype

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

classes_map = {
    'dic_erg_names': class_erg, 
    'dic_run_names': class_run
}

def check_workouts(exercise_now):
    sport = [key for key, v in dic_known_workouts.items() if exercise_now in v]
    if sport:
        print("Known workout! Tell me more:")
        return 1
    else:
        addOrNot = input("Unknown workout! Would you like to add it? (y/n): ")
        if(addOrNot == 'y'):
            #function for creating workout class nd writing a csv for furture storage
            #new_workout_type()
            return 2
        else:
            continueOrNot = input("Record another workout? (y/n): ")
            if(continueOrNot == 'n'):
                #some redundancies here with changing global to false and returnng false
                global keepGoing
                keepGoing = False
                return 0
            else:
                keepGoing = True
                return 1


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

def new_workout_type(mydict1,file1):
    #update the workout dictionary
    #create the dynamic class
    #update the classes_map dictionary
    key_name = input("Proper name? ")
    string_of_names = str(input("Other possible names, sperated by comma with no space: "))
    list_of_names = string_of_names.split(",")
    mydict1[key_name]=list_of_names

    #does this need to go here? function complained about operation on closed file, but cant it just say, "ok when im passed the file i will assume its open"
    with open("%s" % file1 + ".json") as file1:
        mydict1 = json.load(file1)

    json.dump(mydict1, file1)

    argnames = []
    kind = input('cardio or resistence or other? (c/r/o)')
    if(kind=='r'):
        sets = input("are sets relevant? (y/n)")
        if(sets=='y'): argnames.append(sets)

        reps =input("are reps relevant? (y/n)")
        if(reps=='y'): argnames.append(reps)

        weight =input("is weight relevant? (y/n)")
        if(weight=='y'): argnames.append(weight)

        rest =input("is rest relevant? (y/n)")
        if(rest=='y'): argnames.append(rest)
        argnames.append(input("what else is relevant? seperated by comma with no spaces"))
    elif(kind=='c'):
        time =input("is time relevant? (y/n)")
        if(time=='y'): argnames.append(time)

        miles =input("are miles relevant? (y/n)")
        if(miles=='y'): argnames.append(miles)

        meters =input("are meters relevant? (y/n)")
        if(meters=='y'): argnames.append(meters)

        HR =input("is HR relevant? (y/n)")
        if(HR=='y'): argnames.append(HR)
        argnames.append(input("what else is relevant? seperated by comma with no spaces"))
    else:
        argnames.append(input("what crit is relevant? seperated by comma with no spaces"))

    #dynamical class creation, see create_class function, this isnt creating any objects yet, just the constructor
    map_class_name = create_class(key_name,argnames.split(","))

    classes_map[key_name]=map_class_name

    #json.dump(mydict2, file2) -- come back to this, dict cant be created

#this is take from "ClassFactory" at 
#stackoverflow.com/questions/15247075/how-can-i-dynamically-create-derived-classes-from-a-base-class
#not exactly sure how it works yet
def create_class(class_name, argnames, BaseClass=BaseClass):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        BaseClass.__init__(self, class_name[:-len("Class")])

        #from START to FINISH this is not part of original definition ClassFactory, thus might not work
        
        @classmethod
        def from_input(cls):
            user_input_args = []
            #for key, value in self.__dict__.items():
            for key, value in kwargs.items():
                user_input_args.append(input("{0}: ".format(key)))
            return cls(user_input_args)
        #FINISH new addition

    newclass = type(name, (BaseClass,),{"__init__": __init__})
    return newclass




#with open('classes_map.json') as f_classes_map:
#    classes_map = json.load(f_classes_map)


#the first user prompt after starting the code
purpose = input('Update (U) or Examine (E)? ')

if(purpose == 'U'):
    keepGoing = True

while(keepGoing == True):
    exercise = input('Exercise? ')
    if(check_workouts(exercise)==0):
        break
    elif(check_workouts(exercise)==2):
        new_workout_type(dic_known_workouts,f_dic_known_workouts)

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