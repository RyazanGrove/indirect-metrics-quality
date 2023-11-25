import pandas as pd
import numpy as np

from shared.defects_calculator import get_defect_dict, get_defect_dict_per_service
from shared.constants import verification_start_date, vpr_start_date, services_metadata, source_code_metrics_path

columns_to_analyze = [
"Total Cyclomatic Complexity", "Average Cyclomatic Complexity per file", 
"Total Maintainability Index", "Average Maintainability Index per file",
"Total Halstead Volume", "Average Halstead Volume per file",
"Total Lines of Code (raw analysis)", "Average Lines of Code (raw analysis) per file",
"Total percentage of comments (raw analysis)", "Average percentage of comments (raw analysis) per file"
]

dimensions_array = np.zeros((len(columns_to_analyze),6))
template_df = pd.DataFrame(dimensions_array)

correlation_pearson_before_vpr_df = template_df.copy()
correlation_spearman_before_vpr_df = template_df.copy()
std_before_vpr_df = template_df.copy()
coefficient_of_variation_before_vpr_df = template_df.copy()

correlation_pearson_after_vpr_df = template_df.copy()
correlation_spearman_after_vpr_df = template_df.copy()
std_after_vpr_df = template_df.copy()
coefficient_of_variation_after_vpr_df = template_df.copy()

service_abr_list = []

for service_index, current_service in enumerate(services_metadata["source_code"]):
    service_abr = current_service["service"]
    service_abr_list.append(service_abr)
    sheet_name = current_service["sheet_name"]
    service_name = current_service["service_name"]
    defect_dict = get_defect_dict_per_service(service_name)

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

    # save the whole data table for review purpose
    source_code_data.to_excel(source_code_metrics_path + 'for_review_' + service_abr + '.xlsx')

    columns_to_analyze_with_danger = columns_to_analyze.copy()
    columns_to_analyze_with_danger.append("Danger")

    # save the data table before validation date
    before_vpr_df = source_code_data.copy()
    vpr_lines = before_vpr_df[before_vpr_df['Date'] >=  vpr_start_date].index
    before_vpr_df = before_vpr_df[columns_to_analyze_with_danger]
    before_vpr_df.drop(vpr_lines, inplace=True)
    before_vpr_df.to_excel(source_code_metrics_path + 'data_before_vpr_'+ service_abr +'.xlsx', float_format="%.3f")

    # save the data table after validation date
    vpr_df = source_code_data.copy()
    before_vpr_lines = vpr_df[vpr_df['Date'] < vpr_start_date].index
    vpr_df = vpr_df[columns_to_analyze_with_danger]
    vpr_df.drop(before_vpr_lines, inplace=True)
    vpr_df.to_excel(source_code_metrics_path + 'data_after_vpr_'+ service_abr +'.xlsx', float_format="%.3f")

    # before vpr
    print('\nNumber of items in the dataset for service before vpr {0}: {1}'.format(service_abr, before_vpr_df.shape[0]))
    for metric_index, column in enumerate(columns_to_analyze):
        correlation_pearson_before_vpr_df.iloc[metric_index, service_index] = before_vpr_df[column].corr(before_vpr_df["Danger"], method='pearson')
        correlation_spearman_before_vpr_df.iloc[metric_index, service_index] = before_vpr_df[column].corr(before_vpr_df["Danger"], method='spearman')
        std_before_vpr_df.iloc[metric_index, service_index] = before_vpr_df[column].std()
        coefficient_of_variation_before_vpr_df.iloc[metric_index, service_index] = before_vpr_df[column].std() / before_vpr_df[column].mean()

    # after vpr
    print('\nNumber of items in the dataset for service after vpr {0}: {1}'.format(service_abr, vpr_df.shape[0]))
    for metric_index, column in enumerate(columns_to_analyze):
        correlation_pearson_after_vpr_df.iloc[metric_index, service_index] = vpr_df[column].corr(vpr_df["Danger"], method='pearson')
        correlation_spearman_after_vpr_df.iloc[metric_index, service_index] = vpr_df[column].corr(vpr_df["Danger"], method='spearman')
        std_after_vpr_df.iloc[metric_index, service_index] = vpr_df[column].std()
        coefficient_of_variation_after_vpr_df.iloc[metric_index, service_index] = vpr_df[column].std() / vpr_df[column].mean()

# before vpr
correlation_pearson_before_vpr_df.columns = service_abr_list
correlation_spearman_before_vpr_df.columns = service_abr_list
std_before_vpr_df.columns = service_abr_list
coefficient_of_variation_before_vpr_df.columns = service_abr_list

correlation_pearson_before_vpr_df.to_excel(source_code_metrics_path +  'before_vpr_corr_pearson.xlsx', float_format="%.3f")
correlation_spearman_before_vpr_df.to_excel(source_code_metrics_path + 'before_vpr_corr_spearman.xlsx', float_format="%.3f")
std_before_vpr_df.to_excel(source_code_metrics_path + 'before_vpr_std.xlsx', float_format="%.3f")
coefficient_of_variation_before_vpr_df.to_excel(source_code_metrics_path + 'before_vpr_cv.xlsx', float_format="%.3f")

print("Pearson correlation before vpr", correlation_pearson_before_vpr_df)
print("Spearman correlation before vpr", correlation_spearman_before_vpr_df)
print("Std before vpr", std_before_vpr_df)
print("Coefficient of variation before vpr", coefficient_of_variation_before_vpr_df)

# after vpr
correlation_pearson_after_vpr_df.columns = service_abr_list
correlation_spearman_after_vpr_df.columns = service_abr_list
std_after_vpr_df.columns = service_abr_list
coefficient_of_variation_after_vpr_df.columns = service_abr_list

correlation_pearson_after_vpr_df.to_excel(source_code_metrics_path + 'after_vpr_corr_pearson.xlsx', float_format="%.3f")
correlation_spearman_after_vpr_df.to_excel(source_code_metrics_path + 'after_vpr_corr_spearman.xlsx', float_format="%.3f")
std_after_vpr_df.to_excel(source_code_metrics_path + 'after_vpr_std.xlsx', float_format="%.3f")
coefficient_of_variation_after_vpr_df.to_excel(source_code_metrics_path + 'after_vpr_cv.xlsx', float_format="%.3f")

print("Pearson correlation after vpr", correlation_pearson_after_vpr_df)
print("Spearman correlation after vpr", correlation_spearman_after_vpr_df)
print("Std after vpr", std_after_vpr_df)
print("Coefficient of variation after vpr", coefficient_of_variation_after_vpr_df)