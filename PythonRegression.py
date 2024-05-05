#seperating the dataset.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
datasets = pd.read_csv('Salary_Data.csv')
X = datasets.iloc[:, :-1].values
Y = datasets.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

#Using the machine learning type: Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_Train, Y_Train)

Y_Pred = regressor.predict(X_Test)
print(f"predicted response:\n{Y_Pred}")

#Plotting the training set.
plt.scatter(X_Train, Y_Train, color = 'red')
plt.plot(X_Train, regressor.predict(X_Train), color = 'blue')
plt.title(' Experience vs Salary  (Training Set)')
plt.xlabel(' Experience ')
plt.ylabel('Salary')
plt.show()

#Plotting the test set.
plt.scatter(X_Test, Y_Test, color = 'red')
plt.plot(X_Test, regressor.predict(X_Test), color = 'blue')
plt.title('Experience vs Salary (Test Set)')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()