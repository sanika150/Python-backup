from turtle import distance

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# Load your data into a DataFrame (example with a hypothetical 'df' and 'target_variable')
# df = pd.read_csv('your_data.csv')


def main():
    Border = "-" *50
    print(Border)
    df =pd.read_csv("student_performance_ml.csv")
    
    features =[['G1','G2','G3','studytime','failures','absences']]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster']= kmeans.fit_predict(scaled_features)

    print(df[['G1','G2','G3','Cluster']].head())

    plt.scatter(df['G3'],df['studytime'],c=df['Cluster'])
    plt.xlabel("Final Grade (G3)")
    plt.ylabel("Study Time")
    plt.show()
    
   

    

    
  

if __name__ == "__main__":
    main()