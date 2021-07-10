import pandas as pd 
import multiprocessing as mp

cpu = mp.cpu_count()

data = pd.read_csv('../data/aveSigBLSy.csv')

dr14 = pd.read_csv('../data/dr14.csv')
dr14.set_index('SDSS_NAME', inplace=True)

def findZ(name):
   temp = dr14.loc[name]
   return temp['Z']

if __name__ == "__main__":
    sdssName = data['SDSS_NAME']

    with mp.Pool(cpu) as pool:
        out = pool.map(findZ, sdssName)

    data['Z'] = out

    print(data.head())

    data.to_csv('../data/BLSySigZ')