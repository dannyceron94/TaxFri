'''
Created on Jan 8, 2019

@author: DANNY
'''
from ctypes.wintypes import DOUBLE
class Questions(object):
    
    def string_question(self, question):
        return input(question)
    
    def int_question(self,question):
        #this might need an exception 
        return int(input(question))
    def number_in_between(self,question,low,high):
        response = None
        while(response not in range(low,high)):
            response = input(question)
            
        return response
    def yes_no_question(self,question):
        response = None
        while(response not in ("y","n")):
            response = input(question).lower()
        return response
    def price_question(self, question):
        response = None
        #we need a exception
        return DOUBLE(input(question))