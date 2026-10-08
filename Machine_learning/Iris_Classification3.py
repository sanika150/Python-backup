from sklearn.datasets import load_iris


def main():
    print("Iris classification case study")

    Dataset = load_iris()

    #Metadata of dataset
    print("Independent variables are : ")
    print(Dataset.feature_names)
    print("length of independent variables are : ",len(Dataset.feature_names))

    print("Dependent variables are : ")
    print("length of dependent variables is : ",len(Dataset.target_names))
    print(Dataset.target_names)
    
    

    

if __name__ == "__main__":
    main()
