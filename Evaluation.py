# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Identify outliers, exclude them and save new file 

#Define path to data
   #open files
   #read files
   
#Sum I for each image
    
#Create pandas dataframe
   #Get statistics with pandas
     #mean
     #variance
     #Identify outliers (define what is an outlier)
   
#Remove/exclude outliers
     
#Save data without outliers to new files 
    
#Use data outliers excluded for further evaluation
   
import numpy as np
import matplotlib.pylab as plt
import math
import pandas as pd
from scipy import stats
from matplotlib import pylab


#Input 1 off

numrun=4
numq=2358
startrun=426

intensities1=np.zeros((numq,numrun*100))
errors1=np.zeros((numq,numrun*100))

for run in range (0,numrun):
    for image in range (1,101):
        data1=np.genfromtxt('/home/bsb-lab/Documents/Maja/SAXS/Hamburg_data/img_%04d_%05d.dat' %(run+startrun,image) , skip_header=2, skip_footer=60)
        intensities1[:,run*100+image-1]=data1[:numq,1]
        q=data1[:numq,0]  
        errors1[:,run*100+image-1]=data1[:numq,2] 




#Input 2 on

numrun=4
numq=2358
startrun=430

intensities2=np.zeros((numq,numrun*100))
errors2=np.zeros((numq,numrun*100))

for run in range (0,numrun):
    for image in range (1,101):
        data2=np.genfromtxt('/home/bsb-lab/Documents/Maja/SAXS/Hamburg_data/img_%04d_%05d.dat' %(run+startrun,image) , skip_header=2, skip_footer=60)
        intensities2[:,run*100+image-1]=data2[:numq,1]
        q=data2[:numq,0]  
        errors2[:,run*100+image-1]=data1[:numq,2] 




#Input 3 on/off

numrun=1
numq=2358
startrun=434

intensities3=np.zeros((numq,numrun*100))
errors3=np.zeros((numq,numrun*100))

for run in range (0,numrun):
    for image in range (1,101):
        data3=np.genfromtxt('/home/bsb-lab/Documents/Maja/SAXS/Hamburg_data/img_%04d_%05d.dat' %(run+startrun,image) , skip_header=2, skip_footer=60)
        intensities3[:,run*100+image-1]=data3[:numq,1]
        q=data3[:numq,0]  
        errors3[:,run*100+image-1]=data1[:numq,2] 




#df1=pd.DataFrame(intensities1)


#dataframe for one image
df1=pd.DataFrame(data1, columns = ['intensities1', 'q', 'errors1'])

#mean
df1['intensities1'].mean()

#standard deviation
df1['intensities1'].std()

#min
df1['intensities1'].min()

#max
df1['intensities1'].max()

#keep only the ones that are within x standard deviations in the column
df1[np.abs(df1-df1.mean())<=(2*df1.std())]

#remove outliers?
#df1[(np.abs(stats.zscore(df1)) < 3).all(axis=1)]

#Only keep those within 95% (2 standard deviations)
#P = np.percentile(df1.intensities1, [5, 95])
#new_df1 = df1[(df1.intensities1 > P[0]) & (df1.intensities1 < P[1])]
#new_df1

#Plot of average intensities for each image
%matplotlib notebook
plt.plot(np.average(intensities1,axis=0),color='g', label='THz off')

plt.title ('Calmodulin')
plt.xlabel ('Image number')
plt.ylabel ('Intensity')

plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.2)
pylab.ylim([45000,50000])

#keep only the ones that are within x standard deviations in the column
df1[np.abs(df1-df1.mean())<=(2*df1.std())]

#Average all intensities1 (from input 1)
df1=pd.DataFrame(np.average(intensities1,axis=0))

#Plot of average intensities for each image, everything outside of 95% excluded (or everything with in 95% included)
%matplotlib
plt.plot(df1[np.abs(df1-df1.mean())<=(2*df1.std())], color = 'g', label='THZ off')

plt.title ('Calmodulin')
plt.xlabel ('Image number')
plt.ylabel ('Intensity')

plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.2)
plt.show()
pylab.ylim([45000,50000])

#How to exclude the images that are outliers from the data and continue?