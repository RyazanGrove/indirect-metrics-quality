import pandas as pd
import numpy as np

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
dimensions_array = np.zeros((len(columns_to_analyze),6))
correlation_pearson_df = pd.DataFrame(dimensions_array)
correlation_spearman_df = correlation_pearson_df.copy()
std_df = correlation_pearson_df.copy()
coefficient_of_variation_df = correlation_pearson_df.copy()
service_names_list = []

for service_index, current_service in enumerate(services_metadata["source_code"]):
    service_name = current_service["service"]
    service_names_list.append(service_name)
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
    source_code_data.to_excel('..\\output\\source_code\\source_code_for_ml_' + service_name + '.xlsx')

    #analyze only the data before verification period
    verification_period = source_code_data[ source_code_data['Date'] >=  verification_start_date].index
    source_code_data.drop(verification_period , inplace=True)

    print('\nNumber of items in the dataset for service {0}: {1}'.format(service_name, source_code_data.shape[0]))
    for metric_index, column in enumerate(columns_to_analyze):
        correlation_pearson_df.iloc[metric_index, service_index] = source_code_data[column].corr(source_code_data["Danger"], method='pearson')
        correlation_spearman_df.iloc[metric_index, service_index] = source_code_data[column].corr(source_code_data["Danger"], method='spearman')
        std_df.iloc[metric_index, service_index] = source_code_data[column].std()
        coefficient_of_variation_df.iloc[metric_index, service_index] = source_code_data[column].std() / source_code_data[column].mean()

correlation_pearson_df.columns = service_names_list
correlation_spearman_df.columns = service_names_list
std_df.columns = service_names_list
coefficient_of_variation_df.columns = service_names_list

correlation_pearson_df.to_excel('..\\output\\source_code\\source_code_corr_pearson.xlsx', float_format="%.3f")
correlation_spearman_df.to_excel('..\\output\\source_code\\source_code_corr_spearman.xlsx', float_format="%.3f")
std_df.to_excel('..\\output\\source_code\\source_code_std.xlsx', float_format="%.3f")
coefficient_of_variation_df.to_excel('..\\output\\source_code\\source_code_cv.xlsx', float_format="%.3f")

print("Pearson correlation", correlation_pearson_df)
print("Spearman correlation", correlation_spearman_df)
print("Std", std_df)
print("Coefficient of variation", coefficient_of_variation_df)
