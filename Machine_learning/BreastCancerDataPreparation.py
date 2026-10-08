import pandas as pd
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

df = pd.DataFrame(data.data,columns = data.feature_names)
df["target"] = data.target
df.to_csv("Breast_cancer.csv",index = False)

print("Breat_cancer.csv file gets created sucessfully")