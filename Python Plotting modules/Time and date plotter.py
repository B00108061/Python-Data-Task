#SO after much research and testing this code works well
#with time and dat mixed with data
#https://blog.mafr.de/2012/03/11/time-series-data-with-matplotlib/
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# http://stackoverflow.com/questions/16496017/typeerror-when-using-matplotlibs-strpdate2num-with-python-3-2
def bytedate2num(fmt):
    def converter(b):
        return mdates.strpdate2num(fmt)(b.decode('ascii'))
    return converter

date_converter = bytedate2num("%Y-%m-%d")

csvData = np.loadtxt("time and date with data.csv", unpack=False,
        converters={ 0 : date_converter})

#http://stackoverflow.com/questions/4455076/numpy-access-an-array-by-column
days = csvData[:,0]
impressions = csvData[:,1]

plt.plot_date(x=days, y=impressions, fmt="r-")
plt.title("The Graph has the time stamp")
plt.ylabel("Temperature V Time")
plt.grid(True)
plt.show()
