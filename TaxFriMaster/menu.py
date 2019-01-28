"""
created on Jan 26 2019
@author: DANNY CERON
 """
from User import User
from Questions import Questions
from DateClass import DateClass
class menu(User):
    
    
    def new_user(self):
        
        user_input = None
        main_user = User()
        item_date = DateClass()
        checker = main_user.checkFile()
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
                    print("figuring out a date structure for it")
                elif(user_input == 2):
                    item, price, category = main_user.AskForItem()
                    
                    main_user.add_item(item, price, category, item_date.__str__(), note = None)
        else:
            print("Something went wrong!")
    def menu_display(self):
        questions = Questions()
        print("""
        
        1) Check list
        2)Add item
        3)Delete item
        4)User info
        0)quit
        
        """)
        input = questions.number_in_between("Enter number choice: ",0,4)
        return input
            