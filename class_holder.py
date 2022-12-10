import json
import pickle

from def_holder import create_class

file1 = open("dic_known_workouts.json")
dic_known_workouts = json.load(file1)

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

file1.close()