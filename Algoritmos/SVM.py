# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 00:18:22 2021

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

url = "/Users/tales/Desktop/Projeto_PIBIC/Tabelas ML - Cohn-Kanade + FEEDTUM (Com corte)/Data Set Treino/Feminino/Treino Desbalanceado F2.csv"

url2 = "/Users/tales/Desktop/Projeto_PIBIC/Tabelas ML - Cohn-Kanade + FEEDTUM (Com corte)/Data Set Teste/Feminino/Teste Desbalanceado F2.csv"

dataset = pd.read_csv(url, delimiter=';')

dataset_test = pd.read_csv(url2, delimiter=';')

X_train, y_train = dataset.iloc[:, 0:-1].values, dataset.iloc[:, 22].values
X_test, y_test = dataset_test.iloc[:, 0:-1].values, dataset_test.iloc[:, 22].values
scaler = StandardScaler()


scaler.fit(X_train)

X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)

print(y_test)

from sklearn.svm import SVC
svclassifier = SVC(kernel='poly', degree=3)
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

output = open("Modelo SVM Feminino Cohn-Kanade e FEEDTUM Desbalanceado","wb")
pickle.dump(svclassifier, output)
output.close()