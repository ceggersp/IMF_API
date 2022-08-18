import IMF_API
dir = 'C:/Users/CARLOSEG/OneDrive - Inter-American Development Bank Group/Documents/IMF_API/Data'

dataset = 'IFS'
indicator = 'PMP_IX'
F = 'A'
country = 'GB'

DATA = IMF_API.request_data(dataset,country,indicator)

print(DATA)