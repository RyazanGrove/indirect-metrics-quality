from shared.constants import operational_metrics_per_service, verification_start_date
from shared.defects_calculator import get_defect_dict

import pandas as pd

defect_dict = get_defect_dict()

columns_to_analyze = operational_metrics_per_service["S1"]
operational_metrics_data = pd.read_excel('..\\data\\Masters thesis final.xlsx', sheet_name="1 rt-orchestration-service")

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

verification_period = operational_metrics_data[ operational_metrics_data['Date'] >=  verification_start_date].index
operational_metrics_data.drop(verification_period , inplace=True)

for column in columns_to_analyze:
    print('{0} correlation = {1}'.format(column, operational_metrics_data[column].corr(operational_metrics_data["Danger"])))