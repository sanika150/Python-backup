import numpy as np

#Step 1 : Define input features

inputs = np.array([2.0,3.0,4.0])

#Step 2 :Define weights

weights = np.array([0.5,0.3,0.2])

#Step 3 : Define Bias
bias = 1.0

#Step 4 : Calculate wighted sum(Z)
#Formula: Z = (x1*W1 + X2*W2 + X3*W3) + bias
#using numpy dot product for efficient calculation

weighted_sum = np.dot(inputs,weights)+bias

#step 5 :Activaition function
#ReLU(Rectified Linear Unit) 
#If value > 0 ->return value
#If value <= 0 -> return 0

def relu(x):
    return max(0,x)

#step 6 : Final output

output = relu(weighted_sum)

#Step 7 :Display Results
print("Inputs:",inputs)
print("Weights:",weights)
print("Bias:",bias)
print("Weighted Sum (Z):",weighted_sum)
print("Final output : ",output)

