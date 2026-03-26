#test case 1
import pandas as pd

data=pd.read_csv("covid _data.csv")
                 
print("first 5")
print(data.head())

#test case 2
import pandas as pd
data=pd.read_csv("covid _data.csv")
print ("data informations")
print(data.info())
print("statistics data")
print(data.describe())