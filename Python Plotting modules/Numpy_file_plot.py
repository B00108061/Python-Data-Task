
#import urllib.request # library for URL http interfacing
#import time
import numpy as np # library for number analysis and manipulation
import matplotlib.pyplot as plt  # library for plotting data
#import drawnow 
#from drawnow import *
#import csv


x, y = np.loadtxt('CSV with time and temp.txt', delimiter=',', unpack=True)

plt.plot(x,y, label='Loaded from file')

plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Graphing from a CSV file using Python')
plt.legend()
plt.show()
