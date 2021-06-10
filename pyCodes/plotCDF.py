#---------------------------------------------------------------------------#
import matplotlib.pyplot as plot
import csv
import numpy as np
import plotSig as ps #sigma extraction is in plotSig.py
from scipy.stats import ks_2samp
#---------------------------------------------------------------------------#


def plotPDF_CDF(data, c, l, flag): #plot PDF if flag = True , else CDF

    # getting data of the histogram
    count, bins_count = np.histogram(data, bins=10)
  
    # finding the PDF of the histogram using count values
    pdf = count / sum(count)
  
    # using numpy np.cumsum to calculate the CDF
    # We can also find using the PDF values by looping and adding
    cdf = np.cumsum(pdf)
  
    # plotting PDF and CDF
    if(flag):
        plot.plot(bins_count[1:], pdf, color=c, label=l+"-PDF")
    else:
        plot.plot(bins_count[1:], cdf, color=c, label=l+"-CDF",linestyle='dashed')
    plot.legend()

def main():
    #sigma values of NLSY
    #NLSY = ps.returnHist("../aveSigNYSL.csv", 6) 
    #sigma values of BLSY
    BLSY = ps.returnHist("../data/aveSigBLSy.csv", 4) 

    #only 371 sources matched -so
    NLSY = ps.returnHist("../data/aveSigNLSy.csv", 6) 

    flag=False
    #flag=True

    #calling plot functions
    plotPDF_CDF(NLSY, 'r', "NLSy", flag)
    plotPDF_CDF(BLSY, 'b', "BLSy", flag)

    #print KS result
    D, p = ks_2samp(NLSY, BLSY)    
    out = "K-S Test results: \nD-statistic = "+str(D)+"\np value = "+str(p)
    plot.text(-5, 0.6, out)

    #bells and whistles (cosmetics)
    plot.grid(False)
    plot.gca().set(title='Frequency Histogram', ylabel='Normalized Frequency' , xlabel = "log(Sigma)")

    

    #plot.show()
    plot.savefig("../sigCDF371.png")
    #print(ks_2samp(NLSY, BLSY))

main()