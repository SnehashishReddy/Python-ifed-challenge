import pandas as pd
df = pd.read_csv('matches.csv', sep=',')
df.set_index('id',inplace=True)
df.drop('umpire3',axis=1,inplace=True)
df.head()

labels = list(df.columns)
for x in range(0,10):
    labels[x] = labels[x].replace(' ','_')
df.columns = labels
df.head()
print(labels)