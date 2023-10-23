from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

from shared.constants import verification_start_date

columns_to_analyze = [
"Total Cyclomatic Complexity", "Average Cyclomatic Complexity per file", 
"Total Maintainability Index", "Average Maintainability Index per file",
"Total Halstead Volume", "Average Halstead Volume per file",
"Total Lines of Code (raw analysis)", "Average Lines of Code (raw analysis) per file",
"Total percentage of comments (raw analysis)", "Average percentage of comments (raw analysis) per file",
"Danger"
]

service_df = pd.read_excel('..\\output\\source_code\\source_code_for_ml_S1.xlsx')

verification_period = service_df[ service_df['Date'] >=  verification_start_date].index
service_df.drop(verification_period , inplace=True)

service_to_analyze = service_df[columns_to_analyze]

X = service_to_analyze.iloc[:, :-1]
y = service_to_analyze['Danger']

scaler = StandardScaler()
scaler.fit(X)

X_scaled = scaler.transform(X.values)

X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=0)

logistic_regression = LogisticRegression(max_iter= 300)

logistic_regression.fit(X_train_scaled, y_train)

print(logistic_regression.score(X_test_scaled, y_test).round(3))

