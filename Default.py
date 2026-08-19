def EmployeeInfo(Name,Age,Salary,City="Pune"):
    print("Name: ",Name)
    print("Age: ",Age)
    print("Salary: ",Salary)
    print("City: ",City)

def main():
   #Default Argument
    EmployeeInfo("Rahul",26,2000.50) # Correct
    EmployeeInfo("Rahul",26,2000.50,"Mumbai")
if __name__ == "__main__":
    main()