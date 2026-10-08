import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib as plt

def MarvellousClassifier(DataPath):
    Border = "-"*40

    #Step 1:Load the dataset from CSV file
    print(Border)
    print("Step 1:Load the dataset from CSV file")
    print(Border)

    df=pd.read_csv(DataPath)
    print(Border)
    print("Some entries from dataset")
    print(df.head())
    print(Border)

    #step 2:clean the dataset by removing empty rows
    print(Border)
    print("step 2:clean the dataset by removing empty rows")
    print(Border)

    df.dropna(inplace=True)
    print("Total records : ",df.shape[0])
    print("TOtal columns : ",df.shape[1])
    print(Border)




def main():
    Border = "-"*40
    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")




if __name__ == "__main__":
    main()
