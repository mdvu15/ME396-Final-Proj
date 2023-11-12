import numpy as np
import pandas as pd
import pickle
import sys

np.set_printoptions(threshold=sys.maxsize)

pd.set_option('display.max_columns', 500)

cols = ["year", "stfips", "cbsafips", "county", "age", "sex",\
            "grade92", "race", "ethnic", "marital", "prcitshp", \
            "lfsr94", "ftpt94", "class94", "earnhre", "earnwke", \
            "occ2012", "ihigrdc", "docc00", "dind02"]

# Initialize empty data frame
cps_data = pd.DataFrame(columns = cols)

# Append all data from 2010 to 2020 to the data frame
for year in range(10, 21):
    temp = pd.read_stata('data/morg' + str(year) + '.dta')
    if year == 10:
        temp.rename(columns={"occ00" : "occ2012"}, inplace=True)
    if year == 11:
        temp.rename(columns={"occ2011" : "occ2012"}, inplace=True)
    temp = temp[cols]
    cps_data = cps_data.append(temp, ignore_index=True)

### Data cleaning
# Remove rows where both hourly and weekly wage is NaN
cps_data = cps_data[~(cps_data.earnhre.isna() & cps_data.earnwke.isna())]

# Remove records with invalid dind02 (Industry) code
cps_data = cps_data[~cps_data.dind02.isin([3895.0, 3875.0, 8191.0, 7071.0, 6991.0, 6992.0, 3291.0, 7072.0, 8891.0, 8192.0])]

# Drop ind02 (use dind02 instead)
cps_data = cps_data.drop(['lfsr94'], axis=1)

# Recast columns to their correct data type
cps_data = cps_data.astype(
    {
        "age":'float64', 
        "sex":'category',
        "county":'category',
        "cbsafips":'category',
        "grade92":'int64',
        "race":'int64',
        "marital":'int64',
        "dind02":'category',
    }
) 

# Load a pickled occupation code mapping from a file
with open('occ_code.pkl', 'rb') as file:
    occ_code_mapping = pickle.load(file)

cps_data['occ'] = cps_data['occ2012'].map(occ_code_mapping)
cps_data['occ'].fillna(cps_data['occ2012'], inplace=True)

# Drop rows where occupation is NaN
cps_data = cps_data[~cps_data.occ.isna()]

# Drop rows where occupation is still occupation code
cps_data = cps_data[cps_data['occ'].apply(lambda x: isinstance(x, str))]

# Remove occupation code in occupation string
cps_data['occ'] = cps_data['occ'].str.replace('\s\([^)]*\)', '')
cps_data['occ'] = cps_data['occ'].str.replace('\s.*[0-9]+-[0-9]+', '')

# Drop old occupation column
cps_data = cps_data.drop(['occ2012'], axis=1)

# Annual earning calculation
cps_data['annual_earn'] = cps_data['earnwke'] * 52

# Compound inflation 
inflation = {
    2010 : 1.41,
    2011 : 1.36,
    2012 : 1.33,
    2013 : 1.32,
    2014 : 1.30,
    2015 : 1.29,
    2016 : 1.27,
    2017 : 1.25,
    2018 : 1.22,
    2019 : 1.20,
    2020 : 1.18
}

# Calculat adjusted annual earnings as of September 2023
cps_data['annual_earn_adj'] = cps_data['annual_earn'] * cps_data['year'].map(inflation)

# Fill NaN in ethnicity with 0
cps_data.ethnic.fillna(0, inplace=True)

# Drop some redundant columns
cps_data = cps_data.drop(['year', 'earnhre', 'earnwke', 'county', 'ihigrdc', 'annual_earn'], axis=1)

# Save data
cps_data.to_csv('cps_data_2010_2020.csv', index=False)