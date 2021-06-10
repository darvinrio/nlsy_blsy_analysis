import matplotlib.pyplot as plot
import csv
plot.style.use('seaborn-whitegrid')

def savePlot(dataFile):
    x = []
    y = []
    err = []
    with open('../NLSy_source/'+dataFile,'r') as csvfile:
        data = csv.reader(csvfile,delimiter=',')
        next(data, None)
        for row in data:
            x.append(float(row[2]))
            y.append(float(row[9]))
            err.append(float(row[3]))

    plot.scatter(y,x,s=15.0) 
    plot.gca().invert_yaxis()
    plot.errorbar(y,x,yerr=err,elinewidth = 0.5, fmt='.k',visible=0, capsize=2)
    plot.xlabel('MJD')
    plot.ylabel('V-Mag')
    plot.title('SSDS_ID '+dataFile[0:15])
    plot.savefig('lightCurves/'+dataFile[0:15]+'.png')
    plot.clf()

sourcesFile=open('../data/NLSy_sources.txt','r')
sourcesLines=sourcesFile.readlines()
count = 1
for line in sourcesLines :
    tmpFile = line[:len(line)-1]
    savePlot(tmpFile)
    print(count,' --- ',tmpFile,' done')
    count = count+1
print("Done")