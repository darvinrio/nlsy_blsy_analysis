from scipy.stats import spearmanr, kendalltau
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style("white")

def nlsyCorr():
    df = pd.read_csv('../data/aveSigNLSy.csv')
    
    # get z values, cause aveSig file doesnt have z
    df = df[df['Sigma'] != 0]
    
    sigmaCol = pd.DataFrame(df['Sigma'])
    zCol = pd.DataFrame(df['Z'])

    sigma = ((sigmaCol.to_numpy()).transpose())[0]
    z = ((zCol.to_numpy()).transpose())[0]

    c,cp = spearmanr(sigma, z)
    
    k,kp = kendalltau(sigma,z)

    print(len(sigma))

    logSig = np.log(sigma)

    out = "Correlation test 1: \nSpearman's rank coeffcient = "+str(c)+"\np value = "+str(cp)
    plt.text(0.6, -4.5, out)

    out = "Correlation test 2: \nKendall correlation coeffcient = "+str(k)+"\np value = "+str(kp)
    plt.text(0.6, -6, out)

    sns.kdeplot(x=z, y=logSig, cmap="Reds", shade=True)
    sns.kdeplot(x=z, y=logSig, levels=[0.68, 0.95], color='lime')
    plt.xlabel('z')
    plt.ylabel('log(sigma)')

    

if __name__ == "__main__":
    nlsyCorr()

    plt.savefig('../sigVsZ.png')
