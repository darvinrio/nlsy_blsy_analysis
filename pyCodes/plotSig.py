#---------------------------------------------------------------------------#
import matplotlib.pyplot as plot
import csv
import numpy as np
plot.style.use('seaborn-whitegrid')
#---------------------------------------------------------------------------#


def returnHist(file , column): #params = filename , column number , colorOfPlot , label
    x = [] #storing values
    
    #Read Data to be plotted
    with open (file ,'r') as csvfile:
        data = csv.reader(csvfile,delimiter=',')
        next(data, None) #skip header

        for row in data:
            try:
                val = float(row[column]) #extract sigma

                if val != 0 : #log(zero) error
                    x.append(np.log(val)) # store log(sigma)

            except:
                print("shit happens")
    
    return x
    #plot.gca().set(title='Frequency Histogram', ylabel='Frequency')
    #plot.show()

def main():

    #sigma values of NLSY
    #NLSY = returnHist("../aveSigNYSL.csv", 6)
    #sigma values of BLSY
    BLSY = returnHist("../data/aveSigBLSy.csv", 4) 

    #compared NLSY - 371 sources
    NLSY = returnHist('../data/aveSigNLSy.csv',6)

    plot.hist(NLSY, bins=50, alpha=0.5, color='r', density=True, stacked=True , label='NLSY')
    plot.hist(BLSY, bins=50, alpha=0.5, color='b', density=True, stacked=True , label='BLSY')

    plot.gca().set(title='Frequency Histogram', ylabel='Normalized Frequency' , xlabel = "log(Sigma)")
    plot.legend()
    #plot.show()
    plot.savefig("../sigComp371.png")

#main()