import pandas as pd

from shared.defects_calculator import get_defect_dict
from shared.constants import verification_start_date, services_metadata

columns_to_analyze = [
"Total Cyclomatic Complexity", "Average Cyclomatic Complexity per file", 
"Total Maintainability Index", "Average Maintainability Index per file",
"Total Halstead Volume", "Average Halstead Volume per file",
"Total Lines of Code (raw analysis)", "Average Lines of Code (raw analysis) per file",
"Total percentage of comments (raw analysis)", "Average percentage of comments (raw analysis) per file"
]

defect_dict = get_defect_dict()

for current_service in services_metadata["source_code"]:
    service_name = current_service["service"]
    sheet_name = current_service["sheet_name"]

    source_code_data = pd.read_excel('..\\data\\Masters thesis final.xlsx', sheet_name=sheet_name)

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

    #print the whole data table for ml model
    source_code_data.to_excel('..\\output\\source_code_for_ml_' + service_name + '.xlsx')

    #analyze only the data before verification period
    verification_period = source_code_data[ source_code_data['Date'] >=  verification_start_date].index
    source_code_data.drop(verification_period , inplace=True)

    print("Metrics for service : ", service_name)
    for column in columns_to_analyze:
        print('{0} correlation = {1}'.format(column, source_code_data[column].corr(source_code_data["Danger"])))
