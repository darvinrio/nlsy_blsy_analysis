#import numpy as np
#import matplotlib.pyplot as plot
import csv

def sigmaCalc(dataFile):
    mag = []
    err = []
    #dataFile = "0266-51630-0208.csv"

    with open(dataFile,'r') as csvfile:
        data = csv.reader(csvfile,delimiter=',')
        next(data,None)
        for row in data : 
            mag.append(float(row[2]))
            err.append(float(row[3]))

    sum = 0
    for i in mag:
        sum+=i
    if len(mag) == 0 :
        avg = 0
    else :
        avg = sum/len(mag)

    errSumSqr = 0
    for i in err:
        errSumSqr+=(i*i)

    errAvgSqr=0

    if len(err) == 0 :
        avg = 0
    else :
        errAvgSqr = errSumSqr/len(err)
     

    sigmasum = 0
    for i in mag:
        sigmasum+= (i-avg)**2

    sigmasum = sigmasum/(len(mag)-1)

    #sigmasum = sigmasum**(1/2)

    if sigmasum > errAvgSqr : 
        sigma = (sigmasum - errAvgSqr)**(1/2)
    else:
        sigma = 0
    return sigma


#sourcesFile=open('/home/darvinrio/Documents/research/sources.txt','r')
#sourcesLines=sourcesFile.readlines()
#for line in sourcesLines :
#    sigmaCalc('/home/darvinrio/Documents/research/source/'+line[0:len(line)-1])
#print("Done")