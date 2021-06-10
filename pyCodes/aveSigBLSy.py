import numpy as np
#import matplotlib.pyplot as plot
import csv
from sigma import * #sigma calculation is in another file

def aveCalc(dataFile):
    mag = [] #store all mag values
    err = [] #store all mag errors

    with open(dataFile,'r') as csvfile: #open csv file
        data = csv.reader(csvfile,delimiter=',') 
        next(data,None)

        for row in data : #appending data to storage
            mag.append(float(row[2]))
            err.append(float(row[3]))

    sum = 0

    for i in mag: #add all mag
        sum+=i

    if len(mag) == 0 :
        avg = 0        
    else :
        avg = sum/len(mag) #average calculation
    
    return avg

rows = [] #empty array to store output rows
ave = 0.0
sig = 0.0

with open('../data/matched.csv','r') as csvfile:
    data = csv.reader(csvfile)

    for row in data:
        fileCsv = str(row[8] + ".csv")
        tempRow = [row[8], row[9], row[10]]

        try:
            #calculate V mag average
            ave = aveCalc('../BLSy_source/'+fileCsv)
        except:
            #return 0 if file empty 
            ave = 0 

        tempRow.append(str(ave)) #add average to row

        try: 
            #calculate sigma (amp of variability)   
            sig = sigmaCalc('../BLSy_source/'+fileCsv)
        except:
            #return 0 if file empty
            sig = 0 

        tempRow.append(str(sig)) #add sigma to row

        #print(row)
        rows.append(tempRow) #add the row to output rows

#CSV file output

fields = ['SDSS_NAME','RA','DEC','MagAve','Sigma']
filename = "../data/aveSigBLSy.csv"
  
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
      
    # writing the fields
    csvwriter.writerow(fields)
      
    # writing the data rows
    csvwriter.writerows(rows)