# IMF API explorer

from ast import Index
import requests
import os
import time
import platform
import pandas as pd
import PyIMF

if platform.system() == 'Linux':
    clear_command = 'clear'
else:
    os.system('color 02')
    clear_command = 'cls'

def search():
    print(' ')
    print('Type the term you want to search')
    series_list = PyIMF.find_series(str(input()))
    for i in range(0,len(series_list)):
        print(series_list['series_name'][i]+': '+series_list['series_ID'][i])
    print(' ')
    print('Hit ENTER to return to the main menu')
    input()

def finddims():
    print(' ')
    print('Type data from which you want to search')
    dims = PyIMF.find_dims(str(input()))
    print(' ')
    for d in range(0,len(dims)):
        print('Dimension '+str(d+1)+': '+dims['Dimensions'][d])
    print(' ')
    print('Hit ENTER to return to the main menu')
    input()

def findcodes():
    print(' ')
    print('Print the dimension from which you want to search')
    code_list = PyIMF.find_codes(str(input()))
    print(' ')
    for c in range(0, len(code_list)):
        print(code_list['Description'][c]+': '+code_list['Code'][c])
    print(' ')
    print('Hit ENTER to return to the main menu')
    input()

def request_data():
    print(' ')
    print('Enter the dataset from which you want to retrieve data')
    dataset = str(input())
    print(' ')
    print('Enter the country from which you want to retrieve data:')
    print('*If you want a panel with all available countries type "ALL", and wait a couple of minutes for the data to be retrieved.')
    countries = str(input())
    print(' ')
    print('Enter the parameters you want to retrieve:')
    parameters = str(input())
    print('Choose a frequency: annual ("A"), quarterly ("Q"), monthly ("M")')
    F = str(input())
    print(' ')
    print('Enter the directory where you want to store the data (using regular slash /):')
    dir = str(input())
    print(' ')
    print('Enter the name you want for the file:')
    filename = str(input())
    print(' ')
    DATA = PyIMF.request_data(dataset,parameters,countries=countries,F=F,save_file=[dir,filename])
    DATA.to_csv(dir+'/'+filename+'.csv', header=True, index=False)
    print('Hit ENTER to return to the main menu')
    input()

def ERROR():
    print(' ')
    print('ERROR')
    print(' ')
    print('Hit ENTER to return to the main menu')
    input()
    
active = 'true'
session = 0

while active == 'true':
    print(' ')
    if session == 0:
        os.system(clear_command)
        print('Welcome, here you can explore the IMF data API')
        print(' ')
    print('Type "search" to look for datasets that containing some term')
    print('Type "finddims" to look for the dimensions of a dataset')
    print('Type "findcodes" to look for the codes of a dimension')
    print('Type "request" to request data')
    print('Type "exit" to close this file')
    print(' ')
    session = session + 1
    action = str(input())
    if action == 'search':
        try:
            search()
        except:
            ERROR()
    elif action == 'finddims':
        try:
            finddims()
        except:
            ERROR()
    elif action == 'findcodes':
        try:
            findcodes()
        except:
            ERROR()
    elif action == 'request':
        try:
            request_data()
        except:
            ERROR()
    elif action == 'exit':
            for i in range(1,4):
                os.system(clear_command)
                print('Closing the API explorer in '+str(4-i))
                time.sleep(0.5)
            os.system(clear_command)
            active = 'false'
    else:
        print(' ')
        print('Error: '+action+' is not a recognized command')
        print(' ')
        print('Hit ENTER to return to the main menu')
        input()