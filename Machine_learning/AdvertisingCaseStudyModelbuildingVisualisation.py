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

    #----------------------------------------------------------
    # Step 6 : Split dataset into Independent and Dependent variables
    #----------------------------------------------------------
    print(Border)
    print("step 6 : Split dataset into Independent and Dependent variables")
    print(Border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Independent variables : ",X.shape)
    print("Dependent variables : ",Y.shape)

    #----------------------------------------------------------
    # Step 7 : Split dataset for training and testing
    #----------------------------------------------------------
    print(Border)
    print("step 7 : Split dataset for training and testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    #----------------------------------------------------------
    # Step 8 : Create and train the model
    #----------------------------------------------------------
    print(Border)
    print("step 8 : Create and train the model")
    print(Border)

    model = LinearRegression()
    model.fit(X_train,Y_train)

    #----------------------------------------------------------
    # Step 9 : Test the model
    #----------------------------------------------------------
    print(Border)
    print("step 9 : Test the model")
    print(Border)

    Y_pred = model.predict(X_test)

    #----------------------------------------------------------
    # Step 10 : Evaluate the model
    #----------------------------------------------------------
    print(Border)
    print("step 10 : Evaluate the model")
    print(Border)

    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,Y_pred)

    print("Mean Squared Error : ",MSE)
    print("Root Means Squared Error : ",RMSE)
    print("R Square Value : ",R2)

    #----------------------------------------------------------
    # Step 11 : Calculate model coefficient
    #----------------------------------------------------------
    print(Border)
    print("step 11 : Calculate model coefficient")
    print(Border)

    for column,value in zip(X.columns,model.coef_):
        print(f"{column}:{value}")

    print("Intercept : ",model.intercept_)

    #----------------------------------------------------------
    # Step 12 : Compare the actual and predicted values
    #----------------------------------------------------------
    print(Border)
    print("step 12 : Compare the actual and predicted values")
    print(Border)

    result = pd.DataFrame({'Actual sale' : Y_test.values,
                           'Predicted sale' : Y_pred
                        })
    
    print(result.head(10))

    #----------------------------------------------------------
    # Step 13 : Plot actual vs predicted
    #----------------------------------------------------------
    print(Border)
    print("step 13 : Plot actual vs predicted")
    print(Border)

    
    plt.figure(figsize =(8,5))
    plt.scatter(Y_test,Y_pred)
    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sales")
    plt.title("Actual sales VS Predicted sales")
    plt.grid(True)
    plt.show()

def main():
    MarvellousAdvertise("Advertising.csv")



if __name__ == "__main__":
    main()