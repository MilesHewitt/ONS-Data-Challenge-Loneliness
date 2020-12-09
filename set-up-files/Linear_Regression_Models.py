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
%matplotlib inline

#Read in csv file
master = pd.read_csv("Master_Dataset.csv")

#Manipulate data and drop influential outliers
Master_Uni = master.drop(['University #2', 'University #3', 'University #4'], axis=1)
Master_Uni['z_score_Av_Lones']=stats.zscore(Master_Uni['Average Loneliness of MSOAs in each LA'])
Master_Uni = Master_Uni.loc[Master_Uni['z_score_Av_Lones'].abs()<=3]

#Drop every local authority without a university and make secondary dataset
Master_Uni_Only = Master_Uni[Master_Uni['Best rating (Complete Uni Guide)'] != 0]

#Plot grid of graphs comparing average loneliness and other factors and save using secondary dataset
Master_Uni_Pairplot = Master_Uni_Only[['Student Migration Score (15-24)', 'Average Loneliness of MSOAs in each LA', 'Best rating (Complete Uni Guide)']]
grid_plot = sns.pairplot(Master_Uni_Pairplot, aspect =2, height = 3, kind='reg')
grid_plot.savefig('Pairplot_Universities.png', dpi=400)

#Observing relationships for linear regression in primary dataset
Y = Master_Uni[['Average Loneliness of MSOAs in each LA']]
X = Master_Uni[['Student Migration Score (15-24)']]
X = sm.add_constant(X)
model = sm.OLS(Y,X, missing = 'drop')
results = model.fit()
results.summary()

#Boxplot of Urban/Rural vs Loneliness and saving figure
catplot = sns.catplot(x="Urban/Rural", y="Average Loneliness of MSOAs in each LA", kind = "box", data=Master_Uni, height = 4, aspect = 1)
sns.set_style("darkgrid")
catplot.savefig('Loneliness_UrbanRural', dpi=800)

#Scatterplot of IMD vs Loneliness and saving figure
IMD_Lonely = sns.lmplot('IMD - Average score', 'Average Loneliness of MSOAs in each LA', data=Master_Uni)
IMD_Lonely.savefig('IMD_Lonely.png', dpi=800)
