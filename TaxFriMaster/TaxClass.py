'''
Created on Aug 18, 2018
updated on Dec 24,2018

@author: DANNY CERON
'''
from pip._vendor.requests.certs import where
from test.test_io import MisbehavedRawIO
from sre_parse import CATEGORIES
#my imports
import csv
class TaxClass(object):
#____________________________ITEMS_ARRAYS___________________________________    
#     OFFICEITEMS =["book", "books","pencil", "pencils","pen",
#                   "pens","notebook", "notebooks"]
#     HARDWAREITEMS = []
#     MISCELLANEOUS = []#for random items
#     testr = []
#     LISTOFITEMS = []#saves user data
#    
# #Dictionary
#     ALLARRAY = {"office supply":OFFICEITEMS,"Hardware supply":HARDWAREITEMS,
#                 "Miscellaneous":MISCELLANEOUS,"office supply":testr}
#     #more items can be added

    """List of all categories, if possible make the user add more category"""
    LISTOFCATEGORY = ["Office supply","Hardware supply","Electronics","Groceries",
                      "Clothing & Accessories", "Media","software"]
    
#____________________________END_OF_ARRAYS___________________________________
    #constructor
    def __init__(self):
        self.name = None
        self.birthday= None
        self.ID= None#probably not needed
        self.item_name= None
        self.item_price= None
        self.fileName = "infoData.csv"
     
    """Menu selection""" 
    def menu(self):
        print("""
         1)Check Item list
         2)Add item
         3)Delete item
         4)Format Data
        """)  
    #checks if the file exist
    def checkFile(self):
        checked = False
        #put if stament
        try: 
            test = open(self.fileName,"r")
            test.close()
            checked = True
        except :
            print("Could not find Data")
            print("Creating new data\n")
        return checked     
        
    def askInfo(self):
        
        name = input("Please enter your name: ")
        date = input("Now enter your birth data")
           
        self.createFile(name, date)
        
        
    """creates a csv file with that info
        @param: name, birth-date
        @"""
    def createFile(self, name, birthdate):
        self.name = name
        self.birthday = birthdate

        with open(self.fileName ,"w+") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Full name","Birth date"])
            writer.writerow([self.name,self.birthday])
            writer.writerow(["Category","Date","Item name","Price","Notes"])
    
    """this check if the item already exist in the arrays
           @param: itemName
           @return true if item in any of the arrays, false otherwise"""
    def itemInlist(self,itemName):
        check = False
        for n in self.ALLARRAY:#n instantiates an array each iteration
            for i in n:#in each iteration i instantiate each element in array n
                if itemName == i:#checks if the worded input is already in an array
                    check = True
        return check
    
    """this asks the user to submit an item
           @param: itemName
           @return true if item in any of the arrays, false otherwise"""
    def AskForItem(self):
        item  = ""
        isPrice = False
        while(item == ""):
            item = input("\nInput Item name:")  
        while(isPrice == False):
            price = float(input("\bPlease enter the price of the item(example $0.00): $"))
            if type(price) == float:
                isPrice = True
               
        return item,price
    
   #this needs a lot fixing the way data is going to be save is in process. 
    """this adds a new item to the chosen array
           @param: itemName
           @return true if item in any of the arrays, false otherwise"""
           #there is no method overloading on python just method overriding 
    def saveItem(self,itemName = None,itemPrice = None, itemCategory = None):
        
        if itemPrice == None and itemName == None and itemCategory== None:
            item,price = self.AskForItem()
            for index,cat in enumerate(self.LISTOFCATEGORY):
                print("\n", index+1, cat)
                
            where = int(input("pick items category: "))-1
            
            category = self.LISTOFCATEGORY[where]
            #here we pushed the data into a excel file
            
            #self.ALLARRAY[where].append()

        