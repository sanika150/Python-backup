def main():
    from sklearn.metrics import confusion_matrix
    #1 : postive
    #0 : Negative
    Actual = [1,0,1,1,1,0,1,0,0,1]
    Predicted = [1,0,0,1,1,1,1,1,0,1]

    print("Actual data : ",Actual)
    print("Predicted Data : ",Predicted)

    con_mat = confusion_matrix(Actual,Predicted)

    print(con_mat)
    

    

if __name__ == "__main__":
    main()
