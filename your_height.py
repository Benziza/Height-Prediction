#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python37-32\python.exe

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
import sklearn
import warnings
import pickle
warnings.filterwarnings("ignore")


data1 = pd.read_csv("Your_height.csv")
data1 = data1.dropna()


reg = linear_model.LinearRegression()

new_df = data1.drop('Height',axis='columns')

height = data1.Height

reg.fit(new_df,height)


pickle.dump(reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))


