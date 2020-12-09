import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from scipy import stats
from pylab import savefig
from sklearn.tree import DecisionTreeRegressor
from sklearn import datasets
from IPython.display import Image  
from sklearn import tree
from os import system
%matplotlib inline

#Read dataset
Master = pd.read_csv("Master_Dataset.csv")

#Manipulate dataset
master_main = pd.get_dummies(data=Master, columns =['Location', 'University within local authority', 'Urban/Rural'])
Master_Uni = master_main.drop(['University #1','University #2', 'University #3', 'University #4'], axis=1)

#Drop outliers
Master_Uni['z_score_Av_Lones']=stats.zscore(Master_Uni['Average Loneliness of MSOAs in each LA'])
Master_Uni = Master_Uni.loc[Master_Uni['z_score_Av_Lones'].abs()<=3]

#Sort X and Y for fitting
X = Master_Uni[['Best rating (Complete Uni Guide)','Student Migration Score (15-24)','Urban/Rural_Rural', 'Urban/Rural_Urban', 'Median Age compared to England median', 'IMD - Average score']]
Y = Master_Uni[['Average Loneliness of MSOAs in each LA']]

#Fit data in a decision tree
clf = DecisionTreeRegressor(random_state=0, max_depth = 2, min_samples_split=10)
clf.fit(X,Y)

#Visualise decision tree to observe how it fits the respective data
fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(clf, 
                   feature_names=X.columns,  
                   class_names=Y.columns, impurity=False,
                   filled=True)
