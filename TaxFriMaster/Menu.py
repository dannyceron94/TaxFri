'''
Created on Jan 9, 2019

@author: DANNY
'''
from User import User
from Questions import Questions
from filecmp import clear_cache
class Menu(User,Questions):
    """Menu selection""" 
    def menu(self):
        print("""
         1)Check Item list
         2)Add item
         3)Delete item
         4)Format Data
         
         Enter: quit to exist
        """)
        
    def on_the_main(self):
        
        question = Questions()
        user1 = User()
        
        if not user1.checkFile():
            name = question.string_question("What is your first and last name: ")
            bday = question.string_question("Enter your data birth")
            #ID = question.int_question("Enter your SSN")
            user1.__init__(name = name,Birthday=bday,user_id= None)
            user1.createFile()

        userInPut = None
        while(userInPut != "quit" and userInPut != "Quit" and userInPut != "Quit" and
              userInPut != "QUIT"):
            self.menu()
            userInPut = input("Enter your choice: ")
                
            if(userInPut =="1"):#checking item list
                if(user1.checkFile()):
                    print("file is there")
                    print("Under construction")
                    input("Press enter to continue")
            elif(userInPut =="2"):#adding items

                input("Press enter to continue ")
            elif(userInPut =="3"):#Deleting items
                print("Under construction")
                input("Press enter to continue ")
            elif(userInPut =="4"):#Formating data
                print("Under construction")
                input("Press enter to continue ")
                
