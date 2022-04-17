# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 18:07:25 2021

@author: tales
"""
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

url = "Tabelas ML/Data Set Treino/Feminino/Treino Desbalanceado F.csv"

url2 = "Tabelas ML/Data Set Teste/Feminino/Teste Desbalanceado F.csv"

dataset = pd.read_csv(url, delimiter=';')

dataset_test = pd.read_csv(url2, delimiter=';')

X_train, y_train = dataset.iloc[:, 0:-1].values, dataset.iloc[:, 22].values
X_test, y_test = dataset_test.iloc[:, 0:-1].values, dataset_test.iloc[:, 22].values
scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)

print(X_test)

classifier = KNeighborsClassifier(n_neighbors=7)

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

output = open("Modelo KNN Feminino Desbalanceado","wb")
pickle.dump(classifier, output)
output.close()






