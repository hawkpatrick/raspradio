'''
Created on 05.11.2017

@author: pho
'''
import json

DAY_MONDAY = 0
DAY_TUESDAY = 1
DAY_WEDNESDAY = 2
DAY_THURSDAY = 3
DAY_FRIDAY = 4
DAY_SATURDAY = 5
DAY_SUNDAY = 6

def create_repetition(repeatType, customDays):
    if repeatType == 'once':
        return None
    result = RepeatAlarm()
    if repeatType == 'alldays':
        result.days = [DAY_MONDAY, DAY_TUESDAY, DAY_WEDNESDAY, DAY_THURSDAY, DAY_FRIDAY, DAY_SATURDAY, DAY_SUNDAY]
    if repeatType == 'weekdays':
        result.days = [DAY_MONDAY, DAY_TUESDAY, DAY_WEDNESDAY, DAY_THURSDAY, DAY_FRIDAY]
    return result


class RepeatAlarm(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.days = []
        
    def __repr__(self):
        return self.toJSON()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    
def create_repeat_from_dict(jsonDict):
    if not jsonDict:
        return None
    result = RepeatAlarm()
    if 'days' in jsonDict:
        result.days = jsonDict['days']
    return result

