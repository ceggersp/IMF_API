#import PyIMF
#print(PyIMF.request_data('IFS','PMP_IX', country = 'GB+US'))

import pandas as pd
import numpy as np
import requests
import time
import os
url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
F = 'A'
country = ''
indicator = 'PMP_IX'
parameters = F+'.'+country+'.'+indicator
dataset = 'IFS'

key = 'CompactData/'+dataset+'/'+parameters # adjust codes here
# Navigate to series in API-returned JSON data
data = (requests.get(f'{url}{key}').json()
        ['CompactData']['DataSet']['Series'])

# Create pandas dataframe from the observations

#data_list = [[obs.get('@TIME_PERIOD'), obs.get('@OBS_VALUE')]
#             for obs in data['Obs']]
#country_data = pd.DataFrame(data_list, columns=['year', 'price'])

print(data)

#country_data['country'] = country
#country_data['country_name'] = country_name
#os.system(clear_command)
#print(country+' data retrieved succesfully')
#time.sleep(0.51)