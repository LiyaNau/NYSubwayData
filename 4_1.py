from pandas import *
from ggplot import *

path = 'c:\\Leah\\udacity\\P1\\turnstile_data_master_with_weather.csv'
df = pandas.read_csv(path)
df['DATEd'] = to_datetime(df['DATEn'], format = '%Y-%m-%d')
df['weekday'] = df['DATEd'].dt.weekday
grouped = df.groupby(['weekday'], as_index  = False).mean()
print grouped.head()

#p = ggplot (grouped, aes(x='DATEn')) + geom_bar(aes(weight='ENTRIESn_hourly'),color='black',fill='steelblue')+\
#	scale_x_discrete()
#print (p)