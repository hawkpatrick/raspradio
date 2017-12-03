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

def create_repetition(reqargs):
    days = []
    if not 'selectDaysSlider' in reqargs:
        return None
    if 'checkMo' in reqargs:
        days.append(DAY_MONDAY)
    if 'checkDi' in reqargs:
        days.append(DAY_TUESDAY)
    if 'checkMi' in reqargs:
        days.append(DAY_WEDNESDAY)
    if 'checkDo' in reqargs:
        days.append(DAY_THURSDAY)
    if 'checkFr' in reqargs:
        days.append(DAY_FRIDAY)
    if 'checkSa' in reqargs:
        days.append(DAY_SATURDAY)
    if 'checkSo' in reqargs:
        days.append(DAY_SUNDAY)
    if not days:
        return None

    result = RepeatAlarm()
    result.days = days
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

