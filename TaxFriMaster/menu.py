"""
created on Jan 26 2019
modified on Jan 1 2020
@author: DANNY CERON
 """
from User import User
from Questions import Questions
from DateClass import DateClass
class menu(User):
    
    def new_user(self):
        
        user_input = None
        #creates a user instance.
        main_user = User()
        item_date = DateClass()
        #checks if there is there existing data files.
        checker = main_user.checkFile()
        #creates new data file if no datafile is found.
        if(checker == False):
            name = main_user.string_question("What is your full name?")
            birth_day = main_user.string_question("enter your birth date (ex: 01/01/2000):")
            main_user.__init__(name, birth_day)
            main_user.createFile()
            
            self.new_user()
            #set my account can be used, recently added that method on User class
            
        elif(checker == True):
            while(user_input != 0):
                
                user_input = self.menu_display()
                if(user_input == 1):
                    #printing all the data stored in the file.
                    main_user.readData()
                    input("\nPress enter to continue")
                elif(user_input == 2):
                    main_user.add_transaction()                
                    #add the total
                elif(user_input == 3):
                    main_user.deleteItem()
 
                elif(user_input == 4):
                    main_user.userInfo()
                    input("\nPress enter to continue")
        else:
            print("Something went wrong!")

    def menu_display(self):
        questions = Questions()
        print("""
        
        1) Check list
        2) Add item
        3) Delete item
        4) User info
        0) Quit
        
        """)
        input = questions.number_in_between("Enter number choice: ",0,4)
        return input