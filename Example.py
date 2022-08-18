import IMF_API
dir = 'C:/Users/CARLOSEG/OneDrive - Inter-American Development Bank Group/Documents/IMF_API/Data'

dataset = 'FM'
indicator = 'GGXWDN_G01_GDP_PT'
F = 'A'
country = 'ALL'

DATA = IMF_API.request_data(F,dataset,country,indicator)

DATA = DATA[DATA['year'] == 2022]

DATA.to_csv(dir+'/Example.csv', header=True, index=False)