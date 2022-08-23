# Python module to request data from the IMF API
# ceggers@fen.uchile.cl - github: ceggersp
import pandas as pd
import numpy as np
import requests
import time
import os
import platform
url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'

if platform.system() == 'Linux':
    clear_command = 'clear'
else:
    clear_command = 'cls'

def find_series(search_term):
    key = 'Dataflow'  # Method with series information
    search_series_list = pd.DataFrame(columns = ['series_name','series_ID'])
    full_series_list = requests.get(f'{url}{key}').json()\
                ['Structure']['Dataflows']['Dataflow']
    # Use dict keys to navigate through results:
    for series in full_series_list:
        if search_term in series['Name']['#text']:
            series_name = pd.DataFrame([series['Name']['#text']], columns = ['series_name'])
            series_ID = pd.DataFrame([series['KeyFamilyRef']['KeyFamilyID']], columns = ['series_ID'])
            search_series_list = pd.concat([search_series_list, pd.concat([series_name, series_ID], axis=1)], axis=0, ignore_index = True)

    return search_series_list

def find_dims(series):
    key = 'DataStructure/'+series  # Method / series
    dimension_list = requests.get(f'{url}{key}').json()\
                ['Structure']['KeyFamilies']['KeyFamily']\
                ['Components']['Dimension']
    dims = pd.DataFrame(columns = ['Dimensions'])
    for n in range(0, len(dimension_list)):
        dim = pd.DataFrame([dimension_list[n]['@codelist']], columns = ['Dimensions'])
        dims = pd.concat([dims, dim], axis=0, ignore_index = True)
    
    return dims

def find_codes(dim):
    
    key = f"CodeList/{dim}"
    code_list = requests.get(f'{url}{key}').json()\
            ['Structure']['CodeLists']['CodeList']['Code']

    codes = pd.DataFrame(columns = ['Description','Code'])
    # Use dict keys to navigate through results:
    for c in code_list:
        code_desc = pd.DataFrame([c['Description']['#text']], columns = ['Description'])
        code = pd.DataFrame([c['@value']], columns = ['Code'])
        codes = pd.concat([codes, pd.concat([code_desc, code], axis=1)], axis=0, ignore_index = True)

    return codes

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

def request_data(dataset, parameters, country = 'ALL', F='A', var_name=0, country_name=0,save_file=0,file_type='csv'):
    
    if country_name == 0:
        country_name = country

    if var_name == 0:
        var_name = parameters

    PANEL = pd.DataFrame(columns=['year', var_name, 'country', 'country_name'])

    if country == 'ALL':
        code_list = find_codes('CL_AREA_'+dataset)
        for c in range(0, len(code_list)):
            country_data = country_request(F,dataset,code_list['Code'][c],code_list['Description'][c],parameters,var_name)
            PANEL = pd.concat([PANEL,country_data],axis=0)

    else:
        PANEL = country_request(F,dataset,country,country_name,parameters,var_name)

    if save_file == 0:
        pass
    else:
        if file_type == 'csv':
            PANEL.to_csv(save_file[0]+'/'+save_file[1]+'.'+file_type, header=True, index=False)
        else:
            PANEL.to_excel(save_file[0]+'/'+save_file[1]+'.'+file_type, header=True, index=False)

    return PANEL

