import pandas as pd 
#----------------------------------------

dr14_df = pd.read_csv('../data/dr14.csv')

#prep dr14
dr14_df = dr14_df.drop(['RA','DEC','PSFMAG U','PSFMAG G','PSFMAG R','PSFMAG I','PSFMAG Z','Z','Z_ERR','MagAve1'],axis = 1)


BLSy = pd.read_csv('../data/properBLSy.csv')

BLSy['Mag'] = BLSy['z']  

SDSS_name = BLSy.iloc[0, 2]

SDSS_Filt = dr14_df[dr14_df['SDSS_NAME'] == SDSS_name ]

#print(SDSS_Filt)

for label, row in BLSy.iterrows():
    try:
        SDSS_name = BLSy.iloc[label, 2]
        SDSS_Filt = dr14_df[dr14_df['SDSS_NAME'] == SDSS_name ]
        #print(SDSS_name)
        #print(SDSS_Filt)
        BLSy.iloc[label, 8] = SDSS_Filt.iloc[0, 1]
        print(label)
    except:
        print(" > "+ str(label) + "nope")


BLSy.to_csv("../data/properBLSywithMag.csv")