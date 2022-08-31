#Our data are available through APIs/Data Services. These allow machine-to-machine communication of data. You can use Data Services to import data from databases available on http://data.imf.org/ into your data systems or applications. Developers can build applications and integrate IMF data into those applications via Data Services.
#The Data Services are .NET Framework 4.5 applications.
#
#Please note that the old IMF SDMX web service that was previously available at http://sdmxws.imf.org is no longer supported.
#
#Also, please be aware of the following rate limits and throttle your requests accordingly:
#       10 requests in 5 second window from one user (IP)
#       50 requests per second overall on the application

import PyIMF
gross_debt = PyIMF.request_data('FM', 'G_XWDG_G01_GDP_PT', countries = ['CR', 'SV', 'DO', 'GT', 'HN', 'NI', 'PA'], save_file='gross_debt')
gross_debt['obs_code'] = 
print(gross_debt)