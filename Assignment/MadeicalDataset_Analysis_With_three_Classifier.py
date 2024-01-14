
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Medicaldataset.csv")

#make categorical output into binary output, as this data target variable is categorical (Positive and Negative)
for column in df.columns:
  if( df[column].dtype == "object"):
    grp1 = LabelEncoder()
    grp1.fit( df[column] )
    df[column] = grp1.transform( df[column])
df

#x and y seperate
X = df.drop(["Result"], axis=1)
y = df["Result"]

#seperate train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=30
)

#1st Classifier SVM

from sklearn import svm
#svm instance
clf = svm.SVC()
#train
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
y_pred

from sklearn.metrics import accuracy_score, precision_score, recall_score

print("SVM - Accuracy :" , accuracy_score(y_test, y_pred)*100, "%")
print("SVM - Precision: ", precision_score(y_test, y_pred)*100, "%")
print("SVM - Recall: ", recall_score(y_test, y_pred)*100, "%")

#2nd- Decision Tree

from sklearn.tree import DecisionTreeClassifier

#DecisionTree instance
clf = DecisionTreeClassifier()

#Train
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
y_pred

from sklearn.metrics import accuracy_score, precision_score, recall_score

print("Decision Tree - Accuracy :" , accuracy_score(y_test, y_pred)*100, "%")
print("Decision Tree - Precision: ", precision_score(y_test, y_pred)*100, "%")
print("Decision Tree - Recall: ", recall_score(y_test, y_pred)*100, "%")

#3rd- Random Forest

from sklearn.ensemble import RandomForestClassifier

#RandomForestClassifier instance
clf = RandomForestClassifier()

#Train
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
y_pred

from sklearn.metrics import accuracy_score, precision_score, recall_score

print("Random Forest - Accuracy :" , accuracy_score(y_test, y_pred)*100, "%")
print("Random Forest - Precision: ", precision_score(y_test, y_pred)*100, "%")
print("Random Forest - Recall: ", recall_score(y_test, y_pred)*100, "%")
