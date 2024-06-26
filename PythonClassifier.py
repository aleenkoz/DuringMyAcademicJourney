import numpy as nm  
import matplotlib.pyplot as mtp  
import pandas as pd
from sklearn.model_selection import train_test_split

#Reading the csv file depends on its path on your computer.
data_set= pd.read_csv('dataclassification.csv') 

#seperating the data where X are features of the data and Y are the labels.
x= data_set.iloc[:, [2,3]].values  
y= data_set.iloc[:, 4].values

#and after, seperating them even further to two training sets and two testing sets.
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=0)

#these sets of data need to be ranged and transformed to improve the quality of the predictions.
from sklearn.preprocessing import StandardScaler  

st_x= StandardScaler()  

x_train= st_x.fit_transform(x_train)    
x_test= st_x.transform(x_test)

#we are going to classify using the KNN algorithem
from sklearn.neighbors import KNeighborsClassifier  

classifier= KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2 )  
classifier.fit(x_train, y_train)
y_pred= classifier.predict(x_test)

#using the confusion matrix to evaluate our model.
from sklearn.metrics import confusion_matrix  
cm= confusion_matrix(y_test, y_pred)
print(cm)

#lastly, visualising the work we have done.
from matplotlib.colors import ListedColormap  
x_set, y_set = x_test, y_test  
x1, x2 = nm.meshgrid(nm.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step  =0.01),  
nm.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))  
mtp.contourf(x1, x2, classifier.predict(nm.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),  
alpha = 0.75, cmap = ListedColormap(('red','green' )))  
mtp.xlim(x1.min(), x1.max())  
mtp.ylim(x2.min(), x2.max())  
for i, j in enumerate(nm.unique(y_set)):  
    mtp.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],  
        c = ListedColormap(('red', 'green'))(i), label = j)  
mtp.title('K-NN algorithm(Test set)')  
mtp.xlabel('Age')  
mtp.ylabel('Estimated Salary')  
mtp.legend()  
mtp.show()
