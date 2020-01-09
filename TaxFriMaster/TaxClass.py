'''
Created on Aug 18, 2018
updated on Dec 24,2018

@author: DANNY CERON
'''

#my imports
import csv
from _csv import Dialect, get_dialect
from Questions import Questions
from DateClass import  DateClass
# import pandas as pd
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
            writer.writerow(["Category","Date","Item's name","Price","Notes","Receipt number","store number"])
            
    
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
#Needs fixing. App crashes if category is out of bound.
    def AskForItem(self,message):
        item  = ""
        isPrice = False
        while(item == ""):
            item = input("\n"+message)  
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

    def add_transaction(self):
        recNo = input("enter the receipt Number (optional)")
        storeNo = input("enter the store Number (optional)")
        numberOfItems = int(input("Enter number of items:"))
        if(recNo is None and storeNo is None):
            self.add_store_receipt("NA","NA")
        else:
            self.add_store_receipt(recNo,storeNo)

        if(numberOfItems>1):
            for index in range(numberOfItems):
                message = "Enter Item "+str(index+1)+": "
                item, price, category = self.AskForItem(message)
                item_date = self.date()
                self.add_item(item, price, category, item_date, note = None)
        elif numberOfItems==1:#might need the ()
            item, price, category = self.AskForItem("Enter item: ")
            item_date = self.date()
            self.add_item(item, price, category, item_date, note = None)
        else:
            print("Invalid input")

    def date(self):
        transaction_date = DateClass()
        change_date = input("1) Today's date\n2) Edit Date")
        if(change_date=="2"):
            new_month = input("Enter month(ex: 01): ")
            new_day   = input("Enter day(ex: 01): ")
            new_year  = input("Enter year(ex: 2000): ")
            transaction_date.set_month(new_month)
            transaction_date.set_day(new_day)
            transaction_date.set_year(new_year)
        return transaction_date
        

    def add_store_receipt(self,receiptNo,storeNum):
        with open(self.fileName,"a",newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["","","",
            "","",receiptNo,storeNum])

    
    def readData(self):
        #there is no need to close the reader
        with open(self.fileName)as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            next(csv_reader)
            total = 0
            for index, row in enumerate(csv_reader):
                print(row)
                total = index

        return total
                

    def userInfo(self):
        
        with open(self.fileName) as csvfile:
            csv_reader = csv.reader(csvfile)
            #use next to access iterator
            print(next(csv_reader))#prints 1st line
            print(next(csv_reader))#prints 2nd line

    #have not found an optimal way to do this.
    def deleteItem(self):
        question = Questions()
        maxRange = self.readData()
        itemToDelete = question.number_in_between("Select the item you wish to delete: ",1,maxRange)
        #Opening file to access data.
        #data = pd.read_csv(self.fileName, error_bad_lines=False)
        #print(itemToDelete)
        #data = data.drop([itemToDelete+2], axis=0)
        
        #testing if the item works
        
        input("item deleted \n\nPress enter to continue")
