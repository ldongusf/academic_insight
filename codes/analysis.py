import pandas as pd



data_path = '../data/'

data = pd.read_csv(data_path + 'new_data.csv', index_col = 0, 
    skipinitialspace = True)

col_types = pd.read_csv(data_path + 'column_names.csv', skipinitialspace = True, header = None, index_col = 0)


for i in range(0, len(col_types.count(1))):
    cols = col_types.iloc[i, ].dropna()
    print cols.name
    

a = col_types.iloc[1, ].dropna()

a.name == 'Percentage'

check = data[a]
