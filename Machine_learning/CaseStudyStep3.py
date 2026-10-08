import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*40
###########################################################
#Step 1: Load the dataset
###########################################################
print(Border)
print("Step 1 : load the dataset")
print(Border)

DatasetPath = "iris.csv"
#store csv data in df
df = pd.read_csv(DatasetPath)

print("Dataset gets loaded successfully...")
print("Intials entries from dataset : ")
print(df.head())

###########################################################
#Step 2: Data Analysis(EDA)
###########################################################
print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of dataset : ",df.shape)
#list of column
print("Column Names : ",list(df.columns))
print("Missing values (Per column)")
print(df.isnull().sum())

print("Class Distribution (Species count)")
print(df["species"].value_counts())

print("Statistical report of dataset :")
print(df.describe())

###########################################################
#Step 3: Decide independent and dependent vatiables
###########################################################
print(Border)
print("Step 3 : Decide independent and dependent vatiables")
print(Border)

# X: Independetn variables or features
# Y: Dependent variables or Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = df[feature_cols]
Y = df["species"]

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)