import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
%matplotlib inline

lonely = pd.read_csv('msoa_loneliness.csv')
lonely['msoa11nm'] = lonely['msoa11nm'].str[:-4]
lonely_count = lonely.groupby(['msoa11nm']).count()
lonely_main = lonely.groupby(['msoa11nm']).sum()
lonely_main['Average'] = lonely_main['loneills_2018']/lonely_count['objectid']
lonely_main.to_csv('loneliness_average.csv', index=True)
