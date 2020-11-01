import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt

dataset = pd.read_csv("C:\\Users\\HP\\Desktop\\simple-Linear-Regression-master\\salary_data.csv")
print(dataset)

#  seprating the data set in x independent variable and y is dependent variable
x = dataset.iloc[:, :-1]
print(x)
y = dataset.iloc[:,1]
print(y)

from sklearn.model_selection import train_test_split
x_train , x_test, y_train, y_test = train_test_split(x, y ,test_size = 1/3 , random_state =0)
#
# print(x_train)
# print(y_train)
# print(x_test)

#feature scaling
"""from sklearn.preprocessing import StandardScaler
 sc_x = StandardScaler()
 x_train = sc_x.fit_transform(x_train)
 x_test= sc_x.transform(x_test)
 sc_y = StandardScaler()
 y_train = sc_y.fit_transform(y_train)"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)
print(y_pred)

plt.scatter(x_train, y_train, color= 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.show()