import pandas

#import the data and read as df
df = pandas.read_csv("SP500.csv")   

df = df.drop(['Adj Close'], axis = 1)

#drop unnecessary observations since we only look at 2018's data
df = df[4528:4779].reset_index()  
