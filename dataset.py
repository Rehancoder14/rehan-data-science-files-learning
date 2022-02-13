import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
dataset = pd.read_csv("D:\datasets\chess_games.csv")
x = dataset.iloc[:,3:13].values
y = dataset.iloc[:,13].values
lab_X_1 = LabelEncoder()
x[:,1] = lab_X_1.fit_transform(x[:,1])
lab_X_2 =  LabelEncoder()
x[:,2] = lab_X_2.fit_transform(x[:,2])


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(x , y, test_size = 0.2, random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)