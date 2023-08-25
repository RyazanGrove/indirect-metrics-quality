from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler

service1 = pd.read_excel('out\\test.xlsx')

X = service1.iloc[:, :-1] #service1.columns != 'Danger'
y = service1['Danger']

scaler = StandardScaler()
scaler.fit(X)

X_scaled = scaler.transform(X.values)

X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=0)
#print(y_test.describe())
#print(y_test.info())
print(X_train_scaled.shape, X_test_scaled.shape, y_train.shape, y_test.shape)
#columns = X_train.columns

logistic_regression = LogisticRegression(max_iter= 300)
#svm = SVC()

logistic_regression.fit(X_train_scaled, y_train)
#svm.fit(X_train, y_train.values.ravel())

log_reg_preds = logistic_regression.predict(X_test_scaled)
#svm_preds = svm.predict(X_test)

from sklearn.metrics import classification_report
print("=======================")
print(classification_report(y_test, log_reg_preds))
print(logistic_regression.score(X_test_scaled, y_test))
#print(classification_report(y_test, svm_preds))

#print(service1.describe())
