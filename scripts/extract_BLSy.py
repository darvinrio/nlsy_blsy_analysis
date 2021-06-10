import pandas as pd
#---------------------------------------------------------
#extract Seyfert galaxies alone

#df = pd.read_csv('../data/seyfertList.csv')

#print(df.isnull().sum())

#df.dropna(inplace=True)

#print(df.isnull().sum())

#df.to_csv("../data/properSeyfert.csv")

#print(df.head())
 
#---------------------------------------------------------- 

#extract BLSys

df = pd.read_csv('../data/properSeyfert.csv')

BLSy = df[df['FWHMHb-BR'] > 2000]

#print(BLSy.head(100))

BLSy.to_csv("../data/properBLSy.csv")