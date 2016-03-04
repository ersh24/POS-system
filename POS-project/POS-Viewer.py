# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:42:15 2016

@author: Vladimir
"""
#%%
import POSController
def instructions():
	print(
    'Welcome to the POS! \n\n\n'
    'If you want to add a new sale operation, please input with the blank: \n'
      '1. "sale" \n' 
      '2. "customerid:(AB*****)" \n'
      '3. "cc" - for transactions paid by a credit card \n'
      '4. "sku:(P*****)" \n'
      '5. "amount" - for the amount of money paid \n (Like "sale customerid:AB00008 cc sku:P00000 1700")\n'
 
     'If you want to add a new customer, please enter with space: \n'
      '1. "customer AB*****:" \n (Like customer AB00010'
      ' \n\n'
	
     'If you want to get a sales report for the day, please type "report" \n\n'
	
     'If you want to get a breakdown of sales for the day by client, please type "crm" \n\n'
      
     'If you want to finish your work with the system, please type "quit" \n\n'
	)
 
     #call all the functions
def main():
    instructions()    
    userinputstring = ""
    while userinputstring!="quit":
        userinputstring = input("Please write what do you want: ")
        #try
        userinputstring=POSController.checkUserInput(userinputstring)

main()
