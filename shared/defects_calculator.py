"""
This file contains functions to calculate total number of bugs for every period
Reliability - 1 week
Conformance - 2 weeks
"""

import pandas as pd

def get_defect_dict():
    print("Calculating total number of bugs with weight for every week")

    #read
    bugs_sheet = pd.read_excel('..\\data\\Masters thesis draft 1.4.xlsx', sheet_name='Bugs sorted', index_col=0)
    #remove rows not related to defects
    real_bugs = bugs_sheet.loc[bugs_sheet['Danger'].notnull()]
    #remove rows with unclear danger
    real_bugs["Danger_lvl"] = pd.to_numeric(real_bugs["Danger"], errors='coerce')
    real_bugs = real_bugs.loc[real_bugs['Danger_lvl'].notnull()]

    #create week and year columns
    real_bugs["Week"] = real_bugs["Found"].dt.isocalendar().week
    real_bugs["Year"] = real_bugs["Found"].dt.isocalendar().year

    danger_lvls_2022_dict = {}
    danger_lvls_2023_dict = {}

    for index, row in real_bugs.iterrows():
        if (row['Year'] == 2022):
            if (row['Week'] not in danger_lvls_2022_dict):
                danger_lvls_2022_dict[row['Week']] = row['Danger_lvl']
            else:
                danger_lvls_2022_dict[row['Week']] = danger_lvls_2022_dict[row['Week']] + row['Danger_lvl']
        
        if (row['Year'] == 2023):
            if (row['Week'] not in danger_lvls_2023_dict):
                danger_lvls_2023_dict[row['Week']] = row['Danger_lvl']
            else:
                danger_lvls_2023_dict[row['Week']] = danger_lvls_2023_dict[row['Week']] + row['Danger_lvl']

    result = {"2022": danger_lvls_2022_dict, "2023": danger_lvls_2023_dict}
    print(result)
    
    return result