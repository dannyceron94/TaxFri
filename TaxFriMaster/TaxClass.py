'''
Created on Aug 18, 2018
updated on Dec 24,2018

@author: DANNY CERON
'''

#my imports
import csv
from _csv import Dialect, get_dialect
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
    def __init__(self,name = None,birth_data= None, id = None):
        self.name = name
        self.birthday= birth_data
        self.ID= id#probably not needed
        self.item_name= None
        self.item_price= None# I dont think I need this here.
        self.fileName = "infoData.csv"
     
    def __str__(self):
         return "TaxClass "
     
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
        
    """creates a csv file with that info
        @param: name, birth-date
        @"""
    def createFile(self):

        with open(self.fileName ,"w+",newline='') as csvfile:
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
        
        for index,cat in enumerate(self.LISTOFCATEGORY):
            print("\n", index+1, cat)
            
        where = int(input("pick items category: "))-1
                   
        return item,price,self.LISTOFCATEGORY[where]
    
   #this needs a lot fixing the way data is going to be save is in process. 
    """this adds a new item to the chosen array
           @param: itemName
           @return true if item in any of the arrays, false otherwise"""
           #there is no method overloading on python just method overriding 
#     def saveItem(self,itemName = None,itemPrice = None, itemCategory = None, date = None):
#         
#         if itemPrice == None and itemName == None and itemCategory== None:
#             item,price = self.AskForItem()
#             for index,cat in enumerate(self.LISTOFCATEGORY):
#                 print("\n", index+1, cat)
#                 
#             where = int(input("pick items category: "))-1
#             
#             category = self.LISTOFCATEGORY[where]
#             #here we pushed the data into a excel file
#             with open(self.fileName,"a") as csvfile:
#                 writer = csv.writer(csvfile)
#                 writer.writerow([where,,,,])
#             #self.ALLARRAY[where].append()


    """This method adds all information to the csv file
        @param: itemName,itemPrice, itemCategory, date, note.
        @Returns true if it was succesfull
    """
    def add_item(self,itemName = None,itemPrice = None, itemCategory = None, 
                      date = None, note =None):
        r_value = False
        if self.checkFile():            
            with open(self.fileName,"a",newline='') as csvfile:#Add newline='' to not get an extra empty line.
                writer = csv.writer(csvfile)
                writer.writerow([itemCategory,date,itemName,itemPrice,note])
            r_value = True
                
        return r_value
    
    def readData(self):
        with open(self.fileName)as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            next(csv_reader)
            
            for row in csv_reader:
                
                print(row)

        input("\nPress enter to continue")
                
    def userInfo(self):
        with open(self.fileName) as csvfile:
            csv_reader = csv.reader(csvfile)
            #use next to access iterator
            print(next(csv_reader))#prints 1st line
            print(next(csv_reader))#prints 2nd line
            