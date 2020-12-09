import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib as mpl
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from scipy import stats
%matplotlib inline

#Read prepared dataset
master = pd.read_csv("Master_Dataset.csv")

#Manipulate dataset
master_main = pd.get_dummies(data=master, columns =['Location', 'University within local authority', 'Urban/Rural'])
Master_Uni = master_main.drop(['University #1','University #2', 'University #3', 'University #4'], axis=1)

#Drop outliers
Master_Uni['z_score_Av_Lones']=stats.zscore(Master_Uni['Average Loneliness of MSOAs in each LA'])
Master_Uni = Master_Uni.loc[Master_Uni['z_score_Av_Lones'].abs()<=3]

#Multiple regression model
X = Master_Uni[['Best rating (Complete Uni Guide)','Student Migration Score (15-24)','Urban/Rural_Rural', 'Urban/Rural_Urban', 'Median Age compared to England median', 'IMD - Average score']]
Y = Master_Uni['Average Loneliness of MSOAs in each LA']
X = sm.add_constant(X)
model = sm.OLS(Y,X, missing ='drop')
results = model.fit()
results.summary()
