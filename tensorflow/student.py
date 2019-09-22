import sklearn
from sklearn import linear_model
import numpy as np
import pandas as pd


data = pd.read_csv("/student/student-mat.csv", sep=";")[["G1", "G2", "G3", "studytime", "failures", "absences"]]
predict = "G3"

G3 = np.array(data[predict])                # only "G3"
other = np.array(data.drop([predict], 1))   # data without "G3"

other_train, other_test, G3_train, G3_test = sklearn.model_selection.train_test_split(other, G3, test_size=0.1)

linear = linear_model.LinearRegression()
linear.fit(other_train, G3_train)

print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

predictions = linear.predict(other_test)

for i in range(len(predictions)):
    print(predictions[i], other_test[i], G3_test[i])
