import pandas as pd
import numpy as np
import os
import re


data_path = '../data/'
data_files = [
    data_file for data_file in os.listdir(data_path) if '.csv' in data_file]


for data_file in data_files:
# data_file = data_files[1]
    data_file

    try:
        school = re.search('School_Trend_((\D+))_T', data_file).group(1)
    except AttributeError:
        school = None
        
    print school

    data = pd.read_csv(data_path + data_file, index_col = 0)
    data_sm = data[['2005', '2015']]
    data_sm = data_sm.rename(columns = lambda x: school + '_' + x)
    
    try:
        final_data = pd.merge(final_data, data_sm, left_index=True, right_index=True)
    except NameError as e:
        print e
        final_data = data_sm



new_data = final_data.transpose()
new_data.columns = pd.Series(new_data.columns).apply(lambda x: x.strip())
new_data = new_data.loc[:, new_data.count() >= 40]

# rank = pd.DataFrame(check['Overall rank'])

new_data.loc[new_data.index.map(lambda x: '2005' in x), 'relative_rank'] = \
    -(new_data.loc[new_data.index.map(
            lambda x: '2005' in x), 'Overall rank'] - \
        list(new_data.loc[new_data.index.map(
            lambda x: '2005' in x and 'San-Francisco' in x), 'Overall rank']))

new_data.loc[new_data.index.map(lambda x: '2015' in x), 'relative_rank'] = \
    -(new_data.loc[new_data.index.map(
            lambda x: '2015' in x), 'Overall rank'] - \
        list(new_data.loc[new_data.index.map(
            lambda x: '2015' in x and 'San-Francisco' in x), 'Overall rank']))

new_data.to_csv('../data/new_data.csv')

