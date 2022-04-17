# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 21:33:58 2021

@author: tales
"""
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.naive_bayes import GaussianNB

url = "Tabelas ML/Data Set Treino/Feminino/Treino Desbalanceado F.csv"

url2 = "Tabelas ML/Data Set Teste/Feminino/Teste Desbalanceado F.csv"

dataset = pd.read_csv(url, delimiter=';')

dataset_test = pd.read_csv(url2, delimiter=';')

X_train, y_train = dataset.iloc[:, 0:-1].values, dataset.iloc[:, 22].values

X_test, y_test = dataset_test.iloc[:, 0:-1].values, dataset_test.iloc[:, 22].values

gnb = GaussianNB()

y_pred = gnb.fit(X_train, y_train).predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

output = open("Modelo Naive Bayes Feminino Desbalanceado","wb")
pickle.dump(gnb, output)
output.close()