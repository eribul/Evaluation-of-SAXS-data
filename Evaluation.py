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

from scipy import stats
from matplotlib import pylab


#Input 1 off

numrun=4
numq=2358
startrun=426

intensities1=np.zeros((numq,numrun*100))
errors1=np.zeros((numq,numrun*100))

# Define the values of each column
mean_image_values = []
filtered_files =[] #Files within 2 standard deviations of the mean

for run in range (0,numrun):
    for image in range (1,101):
        data1=np.genfromtxt('/home/bsb-lab/Documents/Maja/SAXS/Hamburg_data/img_%04d_%05d.dat' %(run+startrun,image) , skip_header=2, skip_footer=60) 
        mean_image_values.append(data1[:numq,1].mean())
        
mean_image_value = np.mean(mean_image_values)
std_image_value = np.std(mean_image_values)

for run in range (0,numrun):
    for image in range (1,101):
        data1=np.genfromtxt('/home/bsb-lab/Documents/Maja/SAXS/Hamburg_data/img_%04d_%05d.dat' %(run+startrun,image) , skip_header=2, skip_footer=60) 
  

 #   for image in range (1,101):
  #      data1=np.genfromtxt('/home/bsb-lab/Documents/Maja/SAXS/Hamburg_data/img_%04d_%05d.dat' %(run+startrun,image) , skip_header=2, skip_footer=60) 
 #       print(data1[:numq,1].mean()<=(2*std_image_value))
        
        if (abs(mean_image_value-data1[:numq,1].mean())<=(2*std_image_value)):
            intensities1[:,run*100+image-1]=data1[:numq,1]
            errors1[:,run*100+image-1]=data1[:numq,2]
            filtered_files.append('/home/bsb-lab/Documents/Maja/SAXS/Hamburg_data/img_%04d_%05d.dat' %(run+startrun,image))
        else:
            intensities1[:,run*100+image-1]=None
            errors1[:,run*100+image-1]=None
           # print(run, image) prints the run and image which are outliers
            # Print the names of the failed files
 #           print('/home/bsb-lab/Documents/Maja/SAXS/Hamburg_data/img_%04d_%05d.dat' %(run+startrun,image))

#print(filtered_files)            
            
        # If mean intensity for image is within 2 standard deviations of mean value of all images.
        # if the  intenstities in data1 are within 2 standard deviations from the mean= fulfils the condition (intensities1-intensities1.mean()<=(2*intensities1.std())) continue with the evaluation, if not disregard the data in that file.
#Use filtered files and make a new loop with them: for file in filtered files....pick up intensities, q and error from those       

#            
    #        if not (val-data1[:numq,1].mean()<=(2*data1[:numq,1].std())): 
    #            no_outlier = False
     #           print(no_outlier)
      #      if no_outlier:
       #         intensities1[:,run*100+image-1]=data1[:numq,1]
        #        q=data1[:numq,0]  
         #       errors1[:,run*100+image-1]=data1[:numq,2]
             
        #If any intensities are not within 2 standard deviations from the mean
 #       if np.any(intensities1-intensities1.mean()!=(2*intensities1.std())): 
 #           print("I found an outlier!")
  #      else:
   #         print("I found no outliers!")
#        while np.any(intensities1-intensities1.mean()<=(2*intensities1.std())):
            
  #When this is true I want to use the files in the evaluation of the data, when not true I want to exclude them from the following evaluation. Maybe create a new dataframe? How? The problem is that it is the entire file I want to remove. 


 #Plot of average intensities for each image
%matplotlib notebook
plt.plot(np.average(intensities1,axis=0),color='g', label='off')
plt.title ('Calmodulin')
plt.xlabel ('Image number')
plt.ylabel ('Mean Intensity')
plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.2)
pylab.ylim([45000,50000])       
                            
  

#df1=pd.DataFrame(intensities1)



#dataframe for one image
df1=pd.DataFrame(data1, columns = ['intensities1', 'q', 'errors1'])
df1
#mean
df1['intensities1'].mean()

#standard deviation
df1['intensities1'].std()

#min
df1['intensities1'].min()

#max
df1['intensities1'].max()

#keep only the ones that are within x standard deviations in the column, this is wrong since I only want to do this with intensities
df1[np.abs(df1-df1.mean())<=(2*df1.std())]

#remove outliers?
#df1[(np.abs(stats.zscore(df1)) < 3).all(axis=1)]

#Only keep those within 95% (2 standard deviations)
P = np.percentile(df1.intensities1, [5, 95])
new_df1 = df1[(df1.intensities1 > P[0]) & (df1.intensities1 < P[1])]
new_df1

%matplotlib
plt.plot(new_df1)
plt.show()


#Plot of average intensities for each image
%matplotlib notebook
plt.plot(np.average(intensities1,axis=0),color='g', label='THz off')
plt.title ('Calmodulin')
plt.xlabel ('Image number')
plt.ylabel ('Mean Intensity')
plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.2)
pylab.ylim([45000,50000])

#keep only the ones that are within x standard deviations in the column
df1[np.abs(df1-df1.mean())<=(2*df1.std())]

#Average all intensities1 (from input 1), for each image?
df1=pd.DataFrame(np.average(intensities1,axis=0))
df1

#Plot of average intensities for each image, everything outside of 95% excluded (or everything with in 95% included)
%matplotlib
plt.plot(df1[np.abs(df1-df1.mean())<=(2*df1.std())], color = 'g', label='THZ off')
plt.title ('Calmodulin')
plt.xlabel ('Image number')
plt.ylabel ('Mean Intensity')
plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.2)
plt.show()
pylab.ylim([45000,50000])

#SAXS Plot, I want to do this but without the images that were not within 2 standard deviations
%matplotlib
plt.semilogy(q,np.average(intensities1,axis=1),color='g', label='THz off')
plt.title ('Calmodulin')
plt.xlabel ('q (nm-1)')
plt.ylabel ('Log I (q)')
plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.2)
plt.show()

#SAXS Plot without outliers

#Average all intensities1 (from input 1)
df1=pd.DataFrame(data1, columns = ['intensities1', 'q', 'errors1'])
df1

%matplotlib
plt.plot(q, np.average(intensities1, axis=1))
plt.show()
#How to exclude the images that are outliers from the data and continue?
