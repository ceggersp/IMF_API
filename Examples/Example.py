# In this example, we want to build a panel with some data for 7 countries, and then make some plots.
import PyIMF
import pandas as pd
import matplotlib.pyplot as plt

countries_list = ['CR', 'SV', 'DO', 'GT', 'HN', 'NI', 'PA']

# Requesting data
gross_debt = PyIMF.request_data('FM', 'G_XWDG_G01_GDP_PT', countries = countries_list, save_file='gross_debt')
expenditure = PyIMF.request_data('FM', 'G_X_G01_GDP_PT', countries = countries_list, save_file='expenditure')
nominal_gdp = PyIMF.request_data('IFS', 'NGDP_R_XDC', countries = countries_list, save_file='nominal_gdp')

# Building the final panel
PANEL = pd.merge(pd.merge(gross_debt, expenditure, on = ['year', 'country'], how = 'outer'), nominal_gdp, on = ['year', 'country'], how = 'outer') # Merging the requested data.
PANEL = PANEL[['year', 'country', 'G_XWDG_G01_GDP_PT', 'G_X_G01_GDP_PT', 'NGDP_R_XDC']] # During the merging process, some auxiliary variables are created. In this line we keep just the original variables.
PANEL.sort_values(['country', 'year'], ignore_index=True, inplace=True) # We sort the data in order to work better with it.

# Create a new variable containing the GDP growth.
PANEL['gdp_growth'] = round(100*PANEL['NGDP_R_XDC'].astype(float)/PANEL['NGDP_R_XDC'].astype(float).shift() - 100, 1)

# Saving the panel
PANEL.to_excel('PANEL.xlsx', header=True, index=False) # We save the panel.

# Let's do some graphs for a specific year:
year = 2018
PANEL_ob = PANEL[PANEL['year'] == str(year)].reset_index()

def barplot(var,ylabel,file): # We define a function to avoid repiting the same lines over and over.
        plt.clf()
        PANEL_ob.sort_values([var], ignore_index=True, inplace=True)
        plt.bar(PANEL_ob['country'], round(PANEL_ob[var].astype(float),1))
        plt.xlabel('Country')
        plt.ylabel(ylabel)
        plt.savefig(file+'.png')

barplot('gdp_growth', 'growth', str(year)+' real GDP growth')
barplot('G_XWDG_G01_GDP_PT', 'gross_debt', str(year)+' as (%) of GDP')
barplot('G_X_G01_GDP_PT', 'expenditure', str(year)+' expenditure as (%) of GDP')