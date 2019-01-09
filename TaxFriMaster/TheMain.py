'''
Created on Aug 18, 2018
updated on Dec 24,2018

@author: DANNY CERON
'''
import TaxClass
# item,price = TaxClass.TaxClass().AskForItem()
# end = TaxClass.TaxClass().itemInlist(item)

"""file name, name of class"""
user = TaxClass.TaxClass()
userInPut = None
while(userInPut != "quit" and userInPut != "Quit" and userInPut != "Quit"):
    
    user.menu()
    userInPut = input("Enter your choice: ")
    if(userInPut =="1"):#checking item list
        if(user.checkFile()):
            print("file is there")
            print("Under construction")
            input("Press enter to continue")
    elif(userInPut =="2"):#adding items
        if(user.checkFile()):
            print("file is there")
            print("Under construction")
        else:
            user.askInfo()
        input("Press enter to continue ")
    elif(userInPut =="3"):#Deleting items
        print("Under construction")
        input("Press enter to continue ")
    elif(userInPut =="4"):#Formating data
        print("Under construction")
        input("Press enter to continue ")
# print(TaxClass.TaxClass().saveIManuetem())