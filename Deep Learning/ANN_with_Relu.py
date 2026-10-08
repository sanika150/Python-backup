import numpy as np
import matplotlib.pyplot as plt


#Step 1 : Activation Function (ReLU)
#ReLU(Rectified Linear Unit) 
#If value > 0 ->return value
#If value <= 0 -> return 0
def relu(x):
    return max(0,x)

#step 2:Neuron Forward pass function
#This function stimulates a single artificial neuron
#IT performs 
#1.Input X Weighted multiplication
#2.Summation + Bias
#3.Activation function (ReLU)
def MArvellous_neuron_forward(inputs,weights,bias):
    print("\n-----NEURON CALCULATION START-----\n")

    #Display inputd and weights
    print("Inputs(X): ",inputs)
    print("Weights(W): ",weights)
    print("Bias(B): ",bias)

#Step 2.1 :wighted sum(Z) caalculation
#Formula: Z = (x1*W1 + X2*W2 + X3*W3) + bias


    z = sum(w*x for w,x in zip(weights,inputs)) + bias

    print("\nStep1 : Weighted sum calculaton")
    print("z = w.x + b = ",z)

        #Step 2.2 : Activation function 

    y_hat = relu(z)

    print("\nStep 2 : Activation function Applied ")
    print("Activation Function : ReLU")
    print("Output(y^): ",y_hat)

    print("\n-----NEURON CALCULATION END-----\n")

    return z,y_hat

#Step 3 : Plot ReLU Function
def plot_relu():

    #Generaate range of values for z
    z_values = np.linspace(-10,10,100)

    #Apply ReLU on all values
    relu_values = np.maximum(0,z_values)

    #Plot graph
    plt.figure(figsize=(8,5))
    plt.plot(z_values,relu_values,label='ReLU  Function',linewidth=2,color='green')

    #Axes lines
    plt.axhline(y=0,color='black',linewidth=0.5)
    plt.axvline(x=0,color='grey',linewidth=0.5)

    #Labels and title
    plt.title('ReLU Activation Function',fontsize=16)
    plt.xlabel('Input (z)',fontsize=14)
    plt.ylabel('Output ',fontsize=14)

    #show graph
    plt.show()

#Step 4 :Main function
def main():
    print("\n=============Marvellous NEURON DEMO=============\n")

    #Example inputs(features)
    inputs = [1.0,2.0,3.0]

    #Corresponding Weights
    weights = [0.6,0.4,-0.2]

    #Bias Value
    bias = 0.5

    #Perform forward propagation
    z,y_hat = MArvellous_neuron_forward(inputs,weights,bias)

    #Plot ReLU graph
    plot_relu()

if __name__ == "__main__":
        main()