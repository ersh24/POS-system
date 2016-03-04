# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 22:06:37 2016

@author: Vladimir Ershov
"""
#%%
#Our initial list of all the transactions where user append new transactions
sales = [
            ['AB00001', 1500, 1, 'P00002'],
            ['AB00002', 700, 0, 'P00001'],
            ['AB00004', 800, 0, 'P00004'],
            ['AB00003', 700, 0, 0],
            ['AB00005', 700, 0, 'P00003']
                   
            ]
#adding a new transaction function 
def addSales(newsale):
    sales.append(newsale)
#Our initial dictionary of all the customers and their id where new customers added whe used registerCustomer() function
dictCustomer = {'AB00001':'Vova',
                'AB00002':'Tran',
                'AB00003':'Ruslan',
                'AB00004':'Alex'}
                
#def reportCCbreakdown():

#%%
#creates report of all money trasactions
def reportCCbreakdown():
    
    column = 1
    sumAll=sum(row[column] for row in sales)

    sumCC = 0
    for i in range(0,len(sales)):
        if sales[i][2] == 1:
            sumCC += sales [i][1]
    sumCash=sumAll-sumCC
    print(' Total money you got is\n', sumAll,"\n","Total money you got by cash is\n", sumCash,"\n","Total money you got by credit cards is\n",sumCC)
    return()
    
#%%
#get the information about client id and money he spent in the shop by transaction
def CRM():
    CRMlist=[]
    for i in range(0,len(sales)):
        CRMlist.append([sales[i][0],sales[i][1]])
    print(CRMlist)
#%%
def closeday():
    print(sales)
