import pandas as pd
from shared.defects_calculator import get_defect_dict

columns_to_analyze = [
"Total Cyclomatic Complexity", "Average Cyclomatic Complexity per file", 
"Total Maintainability Index", "Average Maintainability Index per file",
"Total Halstead Volume", "Average Halstead Volume per file",
"Total Lines of Code (raw analysis)", "Average Lines of Code (raw analysis) per file",
"Total percentage of comments (raw analysis)", "Average percentage of comments (raw analysis) per file"
]

defect_dict = get_defect_dict()

source_code_data = pd.read_excel('..\\data\\Masters thesis draft 1.4 copy.xlsx', sheet_name="17 rt-remote-desktop-service_so")

source_code_data["Week"] = source_code_data["Date"].dt.isocalendar().week
source_code_data["Year"] = source_code_data["Date"].dt.isocalendar().year
source_code_data["Danger"] = 0


for index, row in source_code_data.iterrows():
    if (row['Year'] == 2022):
        if(row['Week'] in defect_dict["2022"]):
            source_code_data.loc[index, 'Danger'] = defect_dict["2022"][row['Week']]

    if (row['Year'] == 2023):
        if(row['Week'] in defect_dict["2023"]):
            source_code_data.loc[index, 'Danger'] = defect_dict["2023"][row['Week']]

for column in columns_to_analyze:
    print('{0} correlation = {1}'.format(column, source_code_data[column].corr(source_code_data["Danger"])))

columns_to_analyze.append("Danger")
service_to_print = source_code_data[columns_to_analyze]

service_to_print.to_excel('..\\output\\source_code_for_ml.xlsx')