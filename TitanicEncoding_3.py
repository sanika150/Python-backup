import pandas as pd
import numpy as np
import joblib #store model on harddisk

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

#------------------------------------------------------------------------
#   Function name : DisplayInfo
#   Description : It displays the formated title
#   Parameter : title(str)
#   Return : None
#   Date : 14/03/2026
#   Author : Sanika Dhamnakar
#------------------------------------------------------------------------
def DisplayInfo(Title):
    print("\n"+"="*70)
    print(Title)
    print("="*70)

#------------------------------------------------------------------------
#   Function name : ShowData
#   Description : It shows the basic  information about dataset  
#   Parameter : df
#               df-> Pandas datafrane object
#               message
#               message-> Heading text to display
#   Return : None
#   Date : 14/03/2026
#   Author : Sanika Dhamnakar
#------------------------------------------------------------------------

def ShowData(df,message):
    DisplayInfo(message)

    print("\nFirst five rows of dataset")
    print(df.head())

    print("\nShape of dataset")
    print(df.shape)

    print("\nColumn names")
    print(df.columns.tolist())

    print("\nMissing values in each column")
    print(df.isnull().sum())

#------------------------------------------------------------------------
#   Function name : CleanTitanicData
#   Description : It does preprocessing
#                 It removes unnecessary columns
#                 It handles  missing vlues
#                 It converts text data to numeric format
#                 It does encoding to categorical columns
#   Parameter : df
#               df-> Pandas datafrane object
#               
#   Return : df-> Clean Pandas dataframe
#   Date : 14/03/2026
#   Author : Sanika Dhamnakar
#------------------------------------------------------------------------

def CleanTitanicData(df):
    DisplayInfo("Step 2 : Original data")
    print(df.head())

    #Remove unneccessarary columns
    drop_columns = ["Passengerid","zero","Name","Cabin"]
    existing_columns = [col for col in drop_columns if col in df.columns]

    print("\n Columns to be droped : ")
    print(existing_columns)
    #drop the unwanted columns
    df=df.drop(columns = existing_columns)

    DisplayInfo("Step 2 : Data after column removal")
    print(df.head())

    #handle age column
    if "Age" in df.columns:
        print("Age column before filling missing values")
        print(df["Age"].head(10))

        #Coerce-invalid value gets converted as NaN
        df["Age"] = pd.to_numeric(df["Age"],errors = "coerce")

        age_median = df["Age"].median()

        #replace misssing value with median
        df["Age"] = df["Age"].fillna(age_median)
        print("\nAge column after preprocessing :")
        print(df["Age"].head(10))

    #Handle fare column
    if "Fare" in df.columns:
        print("\nFare column before preprocessing : ")
        print(df["Fare"].head(10))

        df["Fare"] = pd.to_numeric(df["Fare"],errors = "coerce")

        fare_median = df["Fare"].median()

        print("MEdian of fare column : ",fare_median)

        #replace misssing value with median
        df["Fare"] = df["Fare"].fillna(fare_median)
        print("\nFare column after preprocessing :")
        print(df["Fare"].head(10))
         
    #Handle Embarked column
    if "Embarked" in df.columns:
        print("\nEmbarked column before preprocessing : ")
        print(df["Embarked"].head(10))

        #Convert the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()

        #remove missing value

        df["Embarked"] = df["Embarked"].replace(['nan','None',''],np.nan)

        #Get most frequent value
        embarked_mode = df["Embarked"].mode()[0]
        print("mode of embarked column : ",embarked_mode)
        df["Embarked"]= df["Embarked"].fillna(embarked_mode)

        print("\nEmbarked column after preprocessing : ")
        print(df["Embarked"].head(10))

    #Handle sex column
    if "Sex" in df.columns:
        print("\nSex column before preprocessing : ")
        print(df["Sex"].head(10))

        df["Sex"] = pd.to_numeric(df["Sex"],errors = "coerce")


        print("\nSex column after preprocessing : ")
        print(df["Sex"].head(10))

    DisplayInfo("Data after preprocessing")
    print(df.head())

    print("\nMissing values after preprocessing")
    print(df.isnull().sum())

    #Encode Embarked column
    #getdummies-onehotcoding
    df = pd.get_dummies(df,columns = ["Embarked"],drop_first=True)
    print("\n Data after encoding")

    print(df.head())
    print("Shape of dataset : ",df.shape)

    #Convert boolean columns into integer
    for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)

    print("\n Data after encoding")

    print(df.head())
    
    return df
#------------------------------------------------------------------------
#   Function name : MarvellousTitanicLogistic
#   Description : This is main pipeline controller
#                 It loads the dataset, shows row data
#                 It prprocess the dataset and train the model    
#   Parameter : DataPath of dataset file
#   Return : None
#   Date : 14/03/2026
#   Author : Sanika Dhamnakar
#------------------------------------------------------------------------
def MarvellousTitanicLogistic(DataPath):
    DisplayInfo("Step 1 : Loading the dataset")
    df = pd.read_csv(DataPath)

    ShowData(df,"Initial dataset ")

    df  = CleanTitanicData(df)




#------------------------------------------------------------------------
#   Function name : main
#   Description : starting point of the application
#   Parameter : None
#   Return : None
#   Date : 14/03/2026
#   Author : Sanika Dhamnakar
#------------------------------------------------------------------------
def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()
