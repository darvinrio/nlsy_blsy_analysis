import pandas as pd
import numpy as np
#-----------------------------------------------------------------------------------

#load csv to dataframes
NLSy_df = pd.read_csv('../data/aveSigNYSL.csv')
dr14_df = pd.read_csv('../data/properBLSywithMag.csv')
out_df = NLSy_df.copy(deep=True)

#remove unwanted values
dr14_df = dr14_df.drop(['Unnamed: 0','Unnamed: 0.1'],axis = 1)

#add blank columns for matching SDSS id ,RA and DEC
out_df['qSDSS_NAME'] = out_df['SDSS_NAME']
out_df['qRA'] = out_df['RA']
out_df['qDEC'] = out_df['DEC']

#lambda for absoulute
a = lambda x : np.absolute(x)

#print(out_df.head())

for label, row in out_df.iterrows() :

    #extract mag and z value
    mag_val = out_df.iloc[label, 5]
    z_val = out_df.iloc[label, 4]
    try:
        #calculate mag and z difference
        dr14_df['Mag_diff'] = a(dr14_df['Mag']-mag_val)
        dr14_df['z_diff'] = a(dr14_df['z']-z_val)

        #find minimum difference sum , i.e closest match to NLSy
        dr14_df['t_diff'] = dr14_df['Mag_diff'] + dr14_df['z_diff']
        dr14_df.sort_values(by = 't_diff',inplace=True)

        #store first value ( minimum z and mag difference )
        out_df.iloc[label,7] = dr14_df.iloc[0,1] # sdss id
        out_df.iloc[label,8] = dr14_df.iloc[0,2] # ra
        out_df.iloc[label,9] = dr14_df.iloc[0,3] # dec

        #print(mag_val)
        #print(z_val)
        #print(dr14_df)
        #print("#------------------------------------------------------------------")
    except:
        print("exception yo"+str(label))
    #if label == 5:
    #    break
#print(out_df.head())
out_df.to_csv("matched.csv")
print("done")