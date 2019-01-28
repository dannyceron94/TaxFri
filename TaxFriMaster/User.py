'''
Created on Jan 8, 2019

@author: DANNY
'''
from TaxClass import TaxClass
from Questions import Questions
class User(TaxClass,Questions):
    
    def __init__(self,name = None, Birthday = None,user_id = None):
        
        super(User,self).__init__(name = name, birth_data = Birthday,id = user_id)
    
    def __str__(self):
        return super(User,self).__str__()
    
    def change_info(self):
        question = Questions()
        yes_or_no = question.yes_no_question("Wanna change name?")
        if yes_or_no == "y":
            self.name = question.string_question("Enter name:")
            """WE need to still figureout how to change the name in the csv File"""
        else:
            print("Name was not changed")
            
    def SetMyAcount(self):
        question = Questions()
        self.name = question.string_question("enter your full name: ")
        self.birthday = question.string_question("Enter your birthday (ex 01/01/2000): ")
        self.ID = question.int_question("Enter you SSN: ")