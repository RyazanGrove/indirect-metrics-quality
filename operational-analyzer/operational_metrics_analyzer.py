from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import pandas as pd
import numpy as np
from shared.constants import verification_start_date, services_metadata

dimensions_array = np.zeros((15,15))
accuracy_df = pd.DataFrame(dimensions_array)
service_names_list = []

#for service_index, current_service in enumerate(services_metadata["operational"]):
service_index = 0
current_service = services_metadata["operational"][0]
service_name = current_service["service"]
service_names_list.append(service_name)
columns_to_analyze = current_service["metrics"]
#print(service_names_list)


service_raw_data_df = pd.read_excel('..\\output\\operational_metrics\\operational_metrics_for_ml_' + service_name + '.xlsx')
for column in columns_to_analyze:
    if column == "Pipeline Pass Rate":
        service_raw_data_df = service_raw_data_df.loc[service_raw_data_df[column].notna()]

columns_to_analyze.append('Danger')
columns_to_analyze.remove('Test Pass Rate')

service_df = service_raw_data_df.fillna(0)

# create scaler
scaler = StandardScaler()
scaling_data = service_df[columns_to_analyze].iloc[:, :-1]
scaler.fit(scaling_data)

# verification data preparation
verification_data_lines = service_df[(service_df['Date'] >=  verification_start_date)]
verification_data_df = verification_data_lines[columns_to_analyze]
X_ver = verification_data_df.iloc[:, :-1]
y_ver = verification_data_df['Danger']
print('Service: {0} items: {1}'.format(service_name, X_ver.shape[0]))

X_ver_scaled = scaler.transform(X_ver.values)

# model data preparation
data_to_analyze_lines = service_df[service_df['Date'] >=  verification_start_date].index
service_df.drop(data_to_analyze_lines, inplace=True)
data_to_analyze_df = service_df[columns_to_analyze]
X = data_to_analyze_df.iloc[:, :-1]
y = data_to_analyze_df['Danger']
X_scaled = scaler.transform(X.values)

# split data to study and test 
X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=0)

# create model
logistic_regression = LogisticRegression(max_iter= 300)
logistic_regression.fit(X_train_scaled, y_train)
#print('Model accuracy: {}%'.format(round(logistic_regression.score(X_test_scaled, y_test)*100)))

# verify the predicted results
log_reg_preds = logistic_regression.predict(X_ver_scaled)

accuracy_df.iloc[0, service_index] = round(logistic_regression.score(X_test_scaled, y_test)*100)
accuracy_df.iloc[1, service_index] = metrics.mean_absolute_error(y_ver, log_reg_preds)
accuracy_df.iloc[2, service_index] = metrics.mean_squared_error(y_ver, log_reg_preds)
accuracy_df.iloc[3, service_index] = np.sqrt(metrics.mean_squared_error(y_ver, log_reg_preds))


#accuracy_df.columns = service_names_list
#accuracy_df.to_excel('..\\output\\source_code\\source_code_accuracy.xlsx', float_format="%.3f")
print(accuracy_df)