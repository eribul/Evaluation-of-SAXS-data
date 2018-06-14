# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pylab as plt
import math

from scipy import stats
from matplotlib import pylab

#1, Input data, this will use all the files
numrun=1
numq=2358
startrun=426

intensities1=np.zeros((numq,numrun*100))
errors1=np.zeros((numq,numrun*100))

for run in range (0,numrun):
    for image in range (1,101):
        data1=np.genfromtxt('/home/bsb-lab/Documents/Maja/SAXS/Hamburg_data/img_%04d_%05d.dat' %(run+startrun,image) , skip_header=2, skip_footer=60)
        q=data1[:numq,0]
        intensities1[:,run*100+image-1]=data1[:numq,1]
        errors1[:,run*100+image-1]=data1[:numq,2]        



#Check if there are any images in which the mean intensity is more that two standard deviations from the mean intensity of all images
%matplotlib notebook
plt.plot(np.average(intensities1,axis=0),color='g', label='off')
plt.title ('Calmodulin')
plt.xlabel ('Image number')
plt.ylabel ('Mean Intensity')
plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.2)
pylab.ylim([45000,50000])    

#2, Identify and remove the outliers:
mean_image_values = []
filtered_files =[] #Files that will be used for the subsequent analysis, with a mean intesity within 2 standard deviations of the mean

for run in range (0,numrun):
    for image in range (1,101):
        data1=np.genfromtxt('/home/bsb-lab/Documents/Maja/SAXS/Hamburg_data/img_%04d_%05d.dat' %(run+startrun,image) , skip_header=2, skip_footer=60) 
        mean_image_values.append(data1[:numq,1].mean())
        
mean_image_value = np.mean(mean_image_values)
std_image_value = np.std(mean_image_values)

for run in range (0,numrun):
    for image in range (1,101):
        data1=np.genfromtxt('/home/bsb-lab/Documents/Maja/SAXS/Hamburg_data/img_%04d_%05d.dat' %(run+startrun,image) , skip_header=2, skip_footer=60) 
  

 # If mean intensity for image is within 2 standard deviations of mean value of all images.        
        if (abs(mean_image_value-data1[:numq,1].mean())<=(2*std_image_value)):
            q=data1[:numq,0] 
            intensities1[:,run*100+image-1]=data1[:numq,1]
            errors1[:,run*100+image-1]=data1[:numq,2]
            filtered_files.append('/home/bsb-lab/Documents/Maja/SAXS/Hamburg_data/img_%04d_%05d.dat' %(run+startrun,image))
        else:
            q=data1[:numq,0]=None
            intensities1[:,run*100+image-1]=None
            errors1[:,run*100+image-1]=None
      

#Plot of average intensities for each image, check that outliers (image files which are not within 2 standard devations from the mean) are removed 
%matplotlib notebook
plt.plot(np.average(intensities1,axis=0),color='g', label='Off')
plt.title ('Calmodulin')
plt.xlabel ('Image number')
plt.ylabel ('Mean Intensity')
plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.2)
pylab.ylim([45000,50000]) 

#3, Continue with evaluation of data without the outliers:
for file in filtered_files :
    data1=np.genfromtxt('/home/bsb-lab/Documents/Maja/SAXS/Hamburg_data/img_%04d_%05d.dat' %(run+startrun,image) , skip_header=2, skip_footer=60) 
    q=data1[:numq,0]  
    intensities1[:,run*100+image-1]=data1[:numq,1]
    errors1[:,run*100+image-1]=data1[:numq,2]
    
#SAXS Plot, one intensity
%matplotlib notebook
plt.semilogy(data1[:,0],data1[:,1],color='g')
plt.show()

