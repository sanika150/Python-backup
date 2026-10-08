import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

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

    #step 3:Separate independent and dependent variables
    print(Border)
    print("step 3:Separate independent and dependent variables")
    print(Border)

    X = df.drop(columns = ['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(Border)
    print("Input columns : ",X.columns.to_list())
    print("Output column : Class")

    #step 4:Split the data set for training and testing
    print(Border)
    print("step 4:Split the data set for training and testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(Border)
    print("Information of training and testing data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)
    print(Border)

    #step 5:Feature scaling
    print(Border)
    print("step 5:Feature scaling")
    print(Border)

    #independent variable scaling
    scalar = StandardScaler()
    X_train_scaled= scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("Feature scaling is done")

    #step 6:Explore the multiple values of K 
    #Hyper parameter tunning(K)
    print(Border)
    print("step 6:Explore the multiple values of K ")
    print(Border)

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled,Y_train)
        Y_Pred= model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_Pred)
        accuracy_scores.append(accuracy)

    print(Border)
    print("Accuracy report of ll K values from 1 to 20")
    for value in accuracy_scores:
        print(value)

    print(Border)

    #step 7:Plot graph of K vs Accuracy
    print(Border)
    print("step 7:Plot graph of K vs Accuracy")
    print(Border)

   # plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker = 'o')
    plt.title("K value vs accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()

def main():
    Border = "-"*40
    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")




if __name__ == "__main__":
    main()
