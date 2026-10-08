import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#-------------------------------------------
#Step 1 : LOad the dataset from CSV file
#-------------------------------------------

print("Step 1 : Loading dataset..\n")

data = pd.read_csv("Placement_data.csv")

print("Complete Dataset:")
print(data)

#-----------------------------------------
#Step 2 : Understand the dataset
#-----------------------------------------
print("\nStep 2 : Basic Information")
print("\nFirst 5 rows:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns)

print("\nStatistical Summary:")
print(data.describe())

print("\nCheck Missing Values:")
print(data.isnull().sum())

#-----------------------------------------
#Step 3 : Separate input and output
#-----------------------------------------
print("\nStep 3 : Splitting input and output")

#X=input features
X = data[["Aptitude","Coding","Communication","Academics","Internship"]]

#Y = target Output
Y = data["Placed"]

print("\nInput Features (X):")
print(X.head())

print("\nTarget Output (Y):")
print(Y.head())

#-----------------------------------------
#Step 4:Train test split
#-----------------------------------------
print("\nStep 4 : Splitting into Training and testing data")
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=42)

print("\nTraining Input Shape:",X_train.shape)
print("Testing Input Shape:",X_test.shape)
print("Training Output Shape:",Y_train.shape)
print("Testing Output Shape:",Y_test.shape)

#-----------------------------------------
#Step 5 Feature Scaling
#Neural network usually perform better when inputs are scaled
#-----------------------------------------
print("\nStep 5 :caling the input features")

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nScaled Training Data Sample:")
print(X_train_scaled[:5])

#-----------------------------------------
#Step 6 : Create Feedforward Neural Network model
#hidden_layer_size=(8,4)
#means:
#first hidden layer -> 8 neurons
#second hidden layer -> 4 neurons
#activation = 'relu' means ReLU will be used
#max_iter = 1000 means the model can train up to 1000 iterations
#------------------------------------------
print("\nStep 6 : Creating FNN model")

model=MLPRegressor(
    hidden_layer_sizes=(8,4), 
    activation='relu', 
    solver='adam',
    max_iter=1000, 
    random_state=42)

print(model)

#-----------------------------------------
#Step 7 : Train the model
#-----------------------------------------
print("\nStep 7 :Training the model")

model.fit(X_train_scaled,Y_train)

print("\nModel training completed.")

#-----------------------------------------
#Step 8 : Make predictions on testing data
#-----------------------------------------
print("\nStep 8: Make prediction on testing data")
#---------------------------------------------------------
print("\nStep 8 : Making predictions")

y_pred = model.predict(X_test_scaled)


print("\nActual Output:")
print(Y_test.values)

print("\nPredicted Output:")
print(y_pred)

#-----------------------------------------
#Step 9 : Evaluate model performance
#-----------------------------------------
print("\nStep 9 : model evaluation")
y_pred_binary = (y_pred > 0.5).astype(int)
accuracy = accuracy_score(Y_test,y_pred_binary)
print("\nAccuracy:", accuracy)

cm = confusion_matrix(Y_test,y_pred_binary)
print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(Y_test,y_pred_binary))

#-----------------------------------------
#Step 10 :Predict probability
#-----------------------------------------
print("\nStep 10: Predicting probabilities")

y_prob = model.predict_proba(X_test_scaled)
print("\nPredicted Probabilities:")
print(y_prob[:5])

#-----------------------------------------
#Step 11 : Saving model and scaler
#This is called model preservation
#-----------------------------------------
print("\nStep 11 : Saving model and scaler")

joblib.dump(model, "placement_fnn_model.pkl")
joblib.dump(scaler, "placement_scaler.pkl")

print("\nModel saved as:placement_fnn_model.pkl")
print("Scaler saved as:placement_scaler.pkl")

#-----------------------------------------
#Step 12 : Load model and scaler again
#-----------------------------------------
print("\nStep 12 : Load model and scaler again")
#-----------------------------------------------
print("\nStep 12 : Loading saved model and scaler")

loaded_model = joblib.load("placement_fnn_model.pkl")
loaded_scaler = joblib.load("placement_scaler.pkl")

print("\nSaved model and scaler loaded successfully.")

#-----------------------------------------
#Step 13 : Predict for a new student
#Example:
#Aptitude=70, Coding=72, Communication=75, Academics=74, Internship=1
#-----------------------------------------
print("\nStep 13 : Predicting for a new student")

new_student = pd.DataFrame([[70, 72, 75, 74, 1]],
                            columns=['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_student_scaled = loaded_scaler.transform(new_student)

new_prediction = loaded_model.predict(new_student_scaled)
new_probability = loaded_model.predict_proba(new_student_scaled)

print("\nNew Student Data:")
print(new_student)

if new_prediction[0] == 1:
    print("\nPrediction: Placed")
else:
    print("\nPrediction: Not Placed")

print("Prediction Probability:", new_probability)

#-----------------------------------------
#Step 14 : Graph 1 - Placement count
#-----------------------------------------

placement_counts = data['Placed'].value_counts()

plt.figure(figsize=(7, 5))
plt.bar(["Not Placed", "Placed"], placement_counts.values)
plt.title("Placement Class Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.grid(True)
plt.show()

#-----------------------------------------
#Step 15 : Graph 2 -Aptitude vs Coding (colored by placement)
#-----------------------------------------
plt.figure(figsize=(8, 6))

for i in range(len(data)):
    if data['Placed'][i] == 0:
        plt.scatter(data['Aptitude'][i], data['Coding'][i], marker='o', label='Placed' if i == 4 else "")
    else:
        plt.scatter(data['Aptitude'][i], data['Coding'][i], marker='x', label='Not Placed' if i == 0 else "")

plt.title("Aptitude vs Coding")
plt.xlabel("Aptitude Score")
plt.ylabel("Coding Score")
plt.legend()
plt.grid(True)
plt.show()

#-----------------------------------------
#Step 16 : Graph 3 - Training Loss Curve
#loss_curve_stores the loss value after each iteration
#-----------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(model.loss_curve_)
plt.title("Training Loss Curve")
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

#---------------------------------------------------------
#Step 17 : Graph 4 - Actual vs Predicted
#---------------------------------------------------------
comparison = pd.DataFrame({'Actual': Y_test.values, 'Predicted': y_pred})

plt.figure(figsize=(8, 5))
plt.plot(comparison['Actual'].values, marker='o', label='Actual')
plt.plot(comparison['Predicted'].values, marker='s', label='Predicted')
plt.title("Actual vs Predicted")
plt.xlabel("Test Sample Index")
plt.ylabel("Class")
plt.legend()
plt.grid(True)
plt.show()

print("\nProject execution completed successfully.")