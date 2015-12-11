import pandas as pd
import numpy as np
import os
import re


data_path = '../data/'
data_files = [data_file 
              for data_file in os.listdir(data_path) if '.csv' in data_file]

schools = []
frames = []
duplicated_in_same_file = []
for data_file in data_files:
    print data_file
    data = pd.read_csv(data_path + data_file).iloc[:,0:4]
    data.columns = ['school', 'value', 'metric', 'year']
    # data = data[~data['school'].isin(schools)]
    # schools += list(set(list(data.school)))
    frames.append(data)
    # grouped = data.groupby('school')
    # size = grouped.size()
    # print size[size != 4246]
    # print type(size[size != 4246].index)
    # duplicated_in_same_file += list(size[size != 4246].index)
    # print data[(data['school'].isin(duplicated_in_same_file)) & 
    #             (data['metric'] == 'Full-time enrollment') & 
    #             (data['year'] == 2005)]


result = pd.concat(frames)

grouped = result.groupby('school')
size = grouped.size()
print size[size != 4246] / 4246




result = result[result['year'].isin([2005, 2015])]

# grouped = result.groupby('metric')
# select_col_bool = grouped['value'].count() > grouped['value'].size() * 0.8

# select_cols = [idx for idx in select_col_bool.index if select_col_bool[idx] == True]

# select_result = result[result['metric'].isin(select_cols)]


# def compute_metrics(x):
#     print x['year'] == 2015

# grouped = select_result.groupby(['school', 'metric'])

grouped = result.groupby(['school'])

grouped['value'].size()
# grouped.apply(compute_metrics)

check = result[result['school'] == 'AIB College of Business']
check2 = result[result['school'] == 'York College']

a = check[check['metric'] == '% of classes with 20-49 students']

# schools = result['school'].unique()
# metric = result['metric'].unique()



# new_data.to_csv('../data/new_data.csv')

