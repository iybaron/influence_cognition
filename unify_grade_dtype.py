
import pandas as pd

k12_data = pd.read_csv('data/data_k12_orig_wgrade.csv')

k12_data.loc[k12_data['GRADE'] == 'K', 'GRADE'] = 0
k12_data.loc[k12_data['GRADE'] == 'P', 'GRADE'] = 13
k12_data.loc[k12_data['GRADE'] == 'S', 'GRADE'] = 14
k12_data.loc[k12_data['GRADE'] == 'T', 'GRADE'] = 15
k12_data.loc[k12_data['GRADE'] == 'U', 'GRADE'] = 16

k12_data.loc[k12_data['GRADEEQ'] == 'K', 'GRADEEQ'] = 0
k12_data.loc[k12_data['GRADEEQ'] == 'T', 'GRADEEQ'] = 15
k12_data.loc[k12_data['GRADEEQ'] == 'U', 'GRADEEQ'] = 16

k12_data.to_csv('data/data_k12_orig.csv', index=False)
