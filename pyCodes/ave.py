import numpy as np
import matplotlib.pyplot as plot
import csv
from sigma import *

def aveCalc(dataFile):
    mag = []
    err = []

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
    
    return avg

# sourcesFile=open('/home/darvinrio/Documents/research/sources.txt','r')
# sourcesLines=sourcesFile.readlines()
# for line in sourcesLines :
#    line = line[0:len(line)-1]
#    a=aveCalc('/home/darvinrio/Documents/research/source/'+line)
#    s=sigmaCalc('/home/darvinrio/Documents/research/source/'+line)
#    print(line,",",a,",",s)
