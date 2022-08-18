# Python module to request data from the IMF API
import pandas as pd
import requests
import time
import os
import platform
url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'

if platform.system() == 'Linux':
    clear_command = 'clear'
else:
    clear_command = 'cls'

def codelist(indicator):
    key = f"CodeList/{indicator}"
    code_list = requests.get(f'{url}{key}').json()\
            ['Structure']['CodeLists']['CodeList']['Code']
    return code_list

def country_request(F,dataset,country,country_name,indicator,name):

    parameters = F+'.'+country+'.'+indicator
    key = 'CompactData/'+dataset+'/'+parameters # adjust codes here
    try:
        # Navigate to series in API-returned JSON data
        data = (requests.get(f'{url}{key}').json()
                ['CompactData']['DataSet']['Series'])

        # Create pandas dataframe from the observations
        data_list = [[obs.get('@TIME_PERIOD'), obs.get('@OBS_VALUE')]
                     for obs in data['Obs']]
        country_data = pd.DataFrame(data_list, columns=['year', name])
        country_data['country'] = country
        country_data['country_name'] = country_name
        os.system(clear_command)
        print(country+' data retrieved succesfully')
        time.sleep(0.51)
        return country_data
    except:
        country_data = pd.DataFrame(columns=['year', name, 'country', 'country_name'])
        os.system(clear_command)
        print(country+' data not found')
        time.sleep(0.51)
        return country_data

def request_data(F,dataset,country,indicator,name):

    PANEL = pd.DataFrame(columns=['year', name, 'country', 'country_name'])

    if country == 'ALL':
        for c in codelist('CL_AREA_'+dataset):
            country_data = country_request(F,dataset,c['@value'],c['Description']['#text'],indicator,name)
            PANEL = pd.concat([PANEL,country_data],axis=0)

    else:
        PANEL = country_request(F,dataset,country,country,indicator,name)

    return PANEL