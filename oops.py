"""
@Author: Zeehan 
@Date: 2021-29-11 19:00:30
@Title :  read write count display search operation in csv file
"""

import csv 
class CsvReader():
    def __init__(self, fileName) :
        self.fileName = fileName
        fileName = "details.csv"
    def create(self):
        """
        Description: create() function for write something in csv file
        Parameter: newline=, obj
        Return: True
        """
        with open(self.fileName,"w",newline="") as obj:
            fobj=csv.writer(obj)
            fobj.writerow(['Roll','Name',"Total"])
            while True:
                Roll= int(input("Enter a Roll no: "))
                Name=input("Enter name :")
                Total= int(input("Enter total marks :"))
                record=[Roll, Name, Total]
                record.count([Roll, Name, Total])
                fobj.writerow(record)

            
                ch=int(input("press 1 for more \n press 2 for exit \n enter your choice :"))
                if ch==2:
                    break
    def count(self):
        """
        Description: create a function to count the rows inside the csv file 
        Parameter: obj
        Return: 
        """
    
        with open(self.fileName,"r") as obj:
            fobj = csv.reader(obj,delimiter = ",")
            next(fobj)
            data = list(fobj)
            row_count = len(data)
            print("Number of rows",row_count)


    def getheader(self):
        """
        Description: create a function to print header of the file 
        Parameter: obj
        Return: 
        """
        with open(self.fileName, 'r') as obj:
            fobj = csv.DictReader(obj)
            fieldnames = fobj.fieldnames
            print("this is header of the file",fieldnames)

    def display(self):
        """
        Description: create a function to display the contant of the file 
        Parameter: obj
        Return: 
        """
        with open(self.fileName,"r") as obj:
            fobj=csv.reader(obj)
            for i in fobj:
            # fob=row=row+i
            # print("no of rows :",fobj)
                print(i)

    def search(self):
        """
    Description: create a function search the items in list 
    Parameter: obj
    Return: 
        """
    
        with open(self.fileName,"r") as obj:

            fobj=csv.reader(obj)
            next(fobj)
            for i in fobj:
            #if i.len(<1)
                if int(i[2])>=60:
                    print("marks greater then 60:",i)
    
                    





if __name__=='__main__': 
    csv1 = CsvReader("DPS.csv")
    csv1.create()
    csv1.count()
    csv1.getheader()
    csv1.display()
    csv1.search()
    
    
   
