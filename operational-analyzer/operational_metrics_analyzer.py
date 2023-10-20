from shared.constants import verification_start_date, services_metadata, operational_metrics_names
from shared.defects_calculator import get_defect_dict

import pandas as pd
import numpy as np

defect_dict = get_defect_dict()

dimensions_array = np.zeros((9,11))
correlation_pearson_df = pd.DataFrame(dimensions_array)
correlation_spearman_df = correlation_pearson_df.copy()
std_df = correlation_pearson_df.copy()
service_names_list = []

for service_index, current_service in enumerate(services_metadata["operational"]):
    service_name = current_service["service"]
    service_names_list.append(service_name)
    columns_to_analyze = current_service["metrics"]
    sheet_name = current_service["sheet_name"]

    operational_metrics_data = pd.read_excel('..\\data\\Masters thesis final.xlsx', sheet_name=sheet_name)

    operational_metrics_data["Week"] = operational_metrics_data["Date"].dt.isocalendar().week
    operational_metrics_data["Year"] = operational_metrics_data["Date"].dt.isocalendar().year
    operational_metrics_data["Danger"] = 0

    for index, row in operational_metrics_data.iterrows():
        if (row['Year'] == 2022):
            if(row['Week'] in defect_dict["2022"]):
                operational_metrics_data.loc[index, 'Danger'] = defect_dict["2022"][row['Week']]

        if (row['Year'] == 2023):
            if(row['Week'] in defect_dict["2023"]):
                operational_metrics_data.loc[index, 'Danger'] = defect_dict["2023"][row['Week']]

    #print the whole data table for ml model
    operational_metrics_data.to_excel('..\\output\\operational_metrics\\operational_metrics_for_ml_' + service_name + '.xlsx')

    verification_period = operational_metrics_data[ operational_metrics_data['Date'] >=  verification_start_date].index
    operational_metrics_data.drop(verification_period , inplace=True)

    print('\nNumber of items in the dataset for service {0}: {1}'.format(service_name, operational_metrics_data.shape[0]))
    for column in columns_to_analyze:
        metric_index = operational_metrics_names.index(column)
        correlation_pearson_df.iloc[metric_index, service_index] = operational_metrics_data[column].corr(operational_metrics_data["Danger"], method='pearson')
        correlation_spearman_df.iloc[metric_index, service_index] = operational_metrics_data[column].corr(operational_metrics_data["Danger"], method='spearman')
        std_df.iloc[metric_index, service_index] = operational_metrics_data[column].std()

correlation_pearson_df.columns = service_names_list
correlation_spearman_df.columns = service_names_list
std_df.columns = service_names_list

correlation_pearson_df.to_excel('..\\output\\operational_metrics\\operational_metrics_corr_pearson.xlsx', float_format="%.3f")
correlation_spearman_df.to_excel('..\\output\\operational_metrics\\operational_metrics_corr_spearman.xlsx', float_format="%.3f")
std_df.to_excel('..\\output\\operational_metrics\\operational_metrics_std.xlsx', float_format="%.3f")

print("Pearson correlation", correlation_pearson_df)
print("Spearman correlation", correlation_spearman_df)
print("Std", std_df)