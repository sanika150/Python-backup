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
#   Function name : MarvellousTitanicLogistic
#   Description : This is main pipeline controller
#                 It loads the dataset, shows row data
#                 It prprocess the dataset and train the model    
#   Parameter : DataPath of dataset file
#   Return : None
#   Date : 14/03/2026
#   Author : Sanika Dhamnaskar
#------------------------------------------------------------------------
def MarvellousTitanicLogistic(DataPath):
    DisplayInfo("Step 1 : Loading the dataset")
    df = pd.read_csv(DataPath)

    ShowData(df,"Initial dataset ")




#------------------------------------------------------------------------
#   Function name : main
#   Description : starting point of the application
#   Parameter : None
#   Return : None
#   Date : 14/03/2026
#   Author : Sanika Dhamnaskar
#------------------------------------------------------------------------
def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()
