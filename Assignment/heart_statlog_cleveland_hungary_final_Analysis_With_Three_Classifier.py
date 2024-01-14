

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score
from tabulate import tabulate

df = pd.read_csv("heart_statlog_cleveland_hungary_final.csv")
df

#split x and y seperate
X = df.drop(["target"], axis=1)
y = df["target"]

#train
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=30
)

#K-Nearest Calssifier

clf = KNeighborsClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
y_pred

print("K-Nearest Classifier - Accuracy, Precision, Recall")
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

table = [
    ["Metric", "Score"],
    ["Accuracy", "{:.2f}%".format(accuracy * 100)],
    ["Precision", "{:.2f}%".format(precision * 100)],
    ["Recall", "{:.2f}%".format(recall * 100)],
]

print(tabulate(table, headers="firstrow", tablefmt="grid"))

#Decision Tree Classifier

clf = DecisionTreeClassifier()

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
y_pred

print("Decision Tree Classifier - Accuracy, Precision, Recall")
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

table = [
    ["Metric", "Score"],
    ["Accuracy", "{:.2f}%".format(accuracy * 100)],
    ["Precision", "{:.2f}%".format(precision * 100)],
    ["Recall", "{:.2f}%".format(recall * 100)],
]

print(tabulate(table, headers="firstrow", tablefmt="grid"))

#GaussianNB Classifier

clf = GaussianNB()

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
y_pred

print("GaussianNB Classifier - Accuracy, Precision, Recall")
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

table = [
    ["Metric", "Score"],
    ["Accuracy", "{:.2f}%".format(accuracy * 100)],
    ["Precision", "{:.2f}%".format(precision * 100)],
    ["Recall", "{:.2f}%".format(recall * 100)],
]

print(tabulate(table, headers="firstrow", tablefmt="grid"))
