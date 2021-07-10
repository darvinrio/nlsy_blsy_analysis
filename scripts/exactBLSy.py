import pandas as pd 

df = pd.read_csv('../data/aveSigBLSy.csv')

df.drop_duplicates(subset=['SDSS_NAME'], inplace=True)

print(df.head(10))
print(df.shape[0])

df.to_csv('../data/exactBLSy')