# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:42:35 2016

@author: Vladimir
"""

import POSmodeler
#checks for the bad comand
def BadCommandException():
    raise Exception("Bad Command, please try again")
    
#chck user input for what comman to execute
def checkUserInput(userentry):
    
    if userentry=="quit":
        return userentry
    inputlist=userentry.split()
    if len(inputlist)<1:
        BadCommandException()
    userCommand=inputlist[0].lower()
    if userCommand not in (("sale","report","customer","crm","quit","closeday")):
        BadCommandException()
    elif userCommand=="sale":
        registerSale(inputlist)
    elif userCommand=="customer":
        registerCustomer(inputlist)
    elif userCommand=="report":
        POSmodeler.reportCCbreakdown()
    elif userCommand=="crm":
        POSmodeler.CRM()
    elif userCommand=="closeday":
        POSmodeler.closeday()
        
    return userCommand
    
    
    
#register and add sale to the sale list
def registerSale(inputlist):
    customerid=getcustomeridfromcommand(inputlist)
    cc=getccfromcommand(inputlist)
    sku=getskufromcommand(inputlist)
    amount=getamountfromcommand(inputlist)   
    newsale=[customerid,amount,cc,sku]
    print("check the sale ",newsale)
    POSmodeler.addSales(newsale)
#register a new customer
def registerCustomer(inputlist):
            POSmodeler.dictCustomer[inputlist[1]]=input('Customer name\n')
    
#checks for having customer id in input
def getcustomeridfromcommand(inputlist):
    customerid=0
    for item in inputlist:
        if 'id:' in item:
            customerid=item.split(":")[1]
            inputlist.remove(item)
    return customerid
#checks for having amount in input 
def getamountfromcommand(inputlist):
    amount=0
    amount=int(inputlist[1])
    inputlist = []
    return amount
#checks for having cc in input
def getccfromcommand(inputlist):
    cc=0
    for item in inputlist:
        if 'cc' in item:
            cc=1
            inputlist.remove(item)
    return cc
#checks for having sku in input
def getskufromcommand(inputlist):
    sku=0
    for item in inputlist:
        if 'sku:' in item:
            sku=item.split(":")[1]
            inputlist.remove(item)
    return sku
    

#sales.append[customerid,ammount,cc,sku]

 
