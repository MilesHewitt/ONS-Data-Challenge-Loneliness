import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
%matplotlib inline

#Read data
Pop = pd.read_csv('Total_Pop_2018.csv', error_bad_lines=False)

#Select all ages for data to find total population in local authorities
Pop_All_Age = Pop[Pop['AGE_GROUP']=='All ages']

#Select only the local authorities and not other regions
Pop_All_Age = Pop_All_Age[Pop_All_Age['AREA_CODE'].str[:-7]=='E0']

#Save file to copy over to master dataset
Pop_All_Age.to_csv('Pop_All_Age.csv')
