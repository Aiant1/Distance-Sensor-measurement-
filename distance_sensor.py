# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:03:35 2019

@author: Antika
"""
import sys
import pandas as pd
import re
import datetime
import matplotlib.pyplot as plt
import numpy as np
import statistics as st
from scipy.interpolate import UnivariateSpline
from scipy.stats.kde import gaussian_kde
from numpy import linspace
import scipy.stats as stats
import pylab as pl

data_output=[]
data=pd.read_csv("C:\\Users\\ASUS\\Desktop\\DATA_SCIENCE_FOLDER\\Data_Set.csv\\50cm.csv")
#for i in data["output"]:
#    i=str(i)
#    i=i.replace("output = ","")
#    i=int(i)
#
#    data_output.append(i)
absolute_error=[]
data_output=list(data["output"])
data_output2=list(data["output2"])

    
for a_i, b_i in zip(data_output, data_output2):
    absolute_error.append(abs(a_i-b_i))
print ("ABSOLUTE ERROR  =" ,absolute_error)
    
Mean_Absolute_Error=sum(absolute_error) / float(len(absolute_error))
print ("MEAN ABSOLUTE ERROR = ",Mean_Absolute_Error)
am=sum(data_output2) / float(len(data_output2))
Relative_Error=(Mean_Absolute_Error/am)
print ("RELATIVE ERROR = ",Relative_Error)

##average                                           
average=sum(data_output)/len(data_output)
actual_avg=sum(data_output2)/len(data_output2)
print("AVERAGE=",average)
#median
m=st.median(data_output)
print ("MEDIAN=",m)
#variance
variance=np.var(data_output)
print("VARIANCE=",variance)
#stand deviation
stndv=np.std(data_output)
print("STANDARD DAVIATION=",stndv)
print(data_output)

#scatterplot
N=len(data)
x = np.random.rand(N)
plt.scatter(x, data["output"], alpha=0.5)
plt.title('Scatter plot of output')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#Distribution(bar+bell curve)
h = sorted(data_output)
fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed
pl.plot(h,fit,'-o')
plt.title("probability distribution figure 1")
pl.hist(h,normed=True)      #use this to draw histogram of your data
pl.show()          

#bell curve
h1 = data_output
h1.sort()
hmean = np.mean(h1)
hstd = np.std(h1)
pdf = stats.norm.pdf(h1, hmean, hstd)
plt.title("probability distribution figure 2")
plt.plot(h1, pdf) 
print(data_output)


