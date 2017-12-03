'''
Created on 25.11.2017

@author: pho
'''


class FadeInSettings:
    
    def __init__(self, active):
        self.active = active
        
        
def get_default():
    fadeSettings = FadeInSettings(True)
    return fadeSettings