# Evaluation-of-SAXS-data

This code will identify and exclude SAXS frames/images with an average intensity which is not within 2 standard deviations from the mean of all averaged intensities. The remaining frames will then be used in further evaluation of the SAXS data. 

Download the files and add the path after data1=np.genfromtxt, the data should be retreive from all the files. In the first plot the mean intensities of all files are displayed. This is to check that they are similar to the overall mean. The next step is to identify and exclude outliers, this is displayed in the next plot where the outliers have been removed and replaced with "none".

The point is to continue with the evaluation of the data after exclusion of the outlier files. So far, not all the plots in the code are functional.
