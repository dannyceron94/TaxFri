'''
Created on Jan 8, 2019

@author: DANNY
'''
# from ctypes.wintypes import DOUBLE
class Questions(object):
    
    def string_question(self, question):
        return input(question)
    
    def int_question(self,question):
        #this might need an exception 
        return int(input(question))
    def number_in_between(self,question,low,high):
        #we might need an exception
        response = None
        # while(response not in range(low,high+1)):#+1 to include the highest number as well
        try:
            response = int(input(question))
        except ValueError:
            print("you tried to input an invalid value")
            input("\n\npress enter to continue")
            
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

        