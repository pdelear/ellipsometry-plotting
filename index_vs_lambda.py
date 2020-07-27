# - PROGRAM       :: index_vs_lambda.py --  Script 			                 
# - AUTHOR        :: Patrick DeLear                              
#                 :: Department of Physics & Astronomy          
#                 :: SF State University                                                                
# - CREATED       :: Spring 2020                                 
# - MODIFIED      :: 03-03-2020                                


import numpy as np
import scipy as sp
import matplotlib
import matplotlib.pyplot as plt

%matplotlib inline

#read in Woollam Ellipsometer model file
lambdavsn = open('tio2_lambda_n_table')
file_ = lambdavsn.readlines()

#initialize lists
wv_val = []
n_val = []
error_val = []

#split table file into float values for n and lambda
for line in file_:
    break_line = line.split()
    wv_val.append(float(break_line[0].replace('n','')[1:-2]))
    n_str, error_str = break_line[1].replace('\xc2','').replace('\xb1',' ').split()
    n, error = float(n_str),float(error_str)
    n_val.append(n)
    error_val.append(error)
    
#plot n vs lambda  
figure = plt.figure(1,figsize=(8,5))    
plt.plot(wv_val,n_val,'k',label='TiO$_2$')
plt.xlim(400,700) #currently set to visible spectrum
plt.ylim(1.5,3.5) #y limit set in accordance with visible spectrum n range
plt.xlabel('Wavelength (nm)')
plt.ylabel('Index of Refraction')
plt.legend()
#plt.savefig('plotname.png')
plt.show()