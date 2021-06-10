import pandas as pd 
import requests 
import urllib.request as durl
import re
import multiprocessing as mp
import sys
#-----------------------------------------------------------------
err = []

cpu = mp.cpu_count()

link = r"(http://nunuku.caltech.edu/DataRelease/upload/result_web_.+\.csv)"

Folder = "<download path>/BLSy_source/"

url = "http://nunuku.caltech.edu/cgi-bin/getcssconedb_release_img.cgi"

data = pd.read_csv("../data/matched.csv", ",").dropna()

def printThis(row):
    print(row)

def download(row):
    indata = {
        'RA': row[10],
        'Dec': row[11],
        'DB': 'Photocat',
        'SHORT': 'long',
        'OUT': 'csv',
        '.submit': 'Submit'
    }
    rurl = requests.post("http://nunuku.caltech.edu/cgi-bin/getcssconedb_release_img.cgi", data = indata)
    try:
        alink = alink = re.findall(link, rurl.text)[-1]
    except:
        e = sys.exc_info()[0]
        print("exception"+str(e)+str(row[0]))
        err.append(row[1])
        print("ra-"+str(row[9])+' dec-'+str(row[10]))
        return
    durl.urlretrieve(alink, Folder + row[9] + ".csv")
    print(row[9]+ ".csv")

with mp.Pool(cpu) as pool:
    #result = 
    pool.map(download, data.itertuples(name=None))

print("Done")
print("Error files : ")
print(err)

outputFile = open('outMu.txt','a')
outputFile.write(str(err))