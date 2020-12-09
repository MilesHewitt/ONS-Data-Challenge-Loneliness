import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
%matplotlib inline

#Read and manipulate data for use
migration = pd.read_csv("Migrations.csv")
migration_main = migration.drop(['LA code'], axis=1)

#Group MSOAs
years = ['15-19','19-24']
migration_main = migration_main[migration_main['Age'].isin(years)]
migration_main = migration_main.groupby(['LA name']).sum()

#Make total flow as net flow does not represent changing population
migration_main['Total_Flow']=migration_main['Inflow'] + migration_main['Outflow']

#Save to a csv file to copy over to master dataset 
migration_main.to_csv('migration_main_15_24.csv', index=True)
