import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousAdvertise(DataPath):
    Border = "-"*40
    #----------------------------------------------------------
    # Step 1 : Load dataset
    #----------------------------------------------------------
    print(Border)
    print("step 1 : Load dataset")
    print(Border)
    df = pd.read_csv(DataPath)

    print("Few data from dataset. :")
    print(df.head())

    #----------------------------------------------------------
    # Step 2 : Remove unwanted column
    #----------------------------------------------------------
    print(Border)
    print("step 2 : Remove unwanted column")
    print(Border)

    print("Shape of dataset before removal : ",df.shape)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)

    print("Shape of dataset after removal : ",df.shape)

    print(Border)
    print("Clean dataset is : ")
    print(Border)
    print(df.head())

    #----------------------------------------------------------
    # Step 3 : Check missing Values
    #----------------------------------------------------------
    print(Border)
    print("step 3 : Check missing Values")
    print(Border)

    print("Missing values count : \n",df.isnull().sum())

    #----------------------------------------------------------
    # Step 4 : Display Statistical summary
    #----------------------------------------------------------
    print(Border)
    print("step 4 : Display Statistical summary")
    print(Border)

    print(df.describe())

    #----------------------------------------------------------
    # Step 5 : Correlation between columns
    #----------------------------------------------------------
    print(Border)
    print("step 5 : Correlation between columns")
    print(Border)

    print("Correlation Matrix")
    print(df.corr())

def main():
    MarvellousAdvertise("Advertising.csv")



if __name__ == "__main__":
    main()