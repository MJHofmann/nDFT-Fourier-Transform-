
#nDFT v1.py
#by Marius Johannes Hofmann
#05/2018
#
#based on the thesis of Thomas Blochowicz (PhD thesis, University of Bayreuth, Germany 2003)
#
#please also check the documentation and the examples given therein
#
#The program calculates the Discrete Fourier Transform of nonuniformly spaced data (nDFT) in terms of the
#Nonuniform Discrete Cosine Transform (nDCT) and the
#Nonuniform Discrete Sine Transform (nDST)
#The code is intentionally kept short and simple.
#
#INPUT:  requires a two column array (t, f(t)) with the columns separated by tab
#        -1st column is termed t and represents the abscissa (x-values, (time, for instance))
#        -2nd column is termed f(t) and represents the ordinate (y-values, (voltage, for instance))
#
#OUTPUT: generates two new files with the cosine and the sine transformations g_c(w) and g_s(w)
#        in the same folder where the input file is located. those files are named
#        -"filename_DCT.pef" and
#        -"filename_DST.pef"
#
#Some comments:
#        -The complexity is O(N^2) where N is the number if input points
#        -applying the transformations twice, i.e. nDFT^2, nDST^2, yields the original function times Sqrt[2]
#        -the two nested for-loops are unfavorable (slow) but computation can be accelerated  
#         using parallelization (not implemented in this version)
#--------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------#
import math as m    # math package
import numpy as np   # numpy package
import tkinter.filedialog   # provides a dialog in windows for opening an ascii file; may be removed
from timeit import default_timer as timer # used for calculation of computing time; may be removed
#--------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------#
#FUNCTION DEFINITION
#nDCT
#w is the sampling vector in Fourier space, t are the x-values and f are the y-values of the input array
def nDCT(w,t,f):
   smp=[]
   
   for j in range(len(w)): #loops through all sampling points w_i
       ft=0         
       for i in range(len(f)-1): # Fourier integral 
        ft+=(
            ((f[i+1]-f[i])/(t[i+1]-t[i])*(-2)*m.sin(0.5*w[j]*(t[i+1]+t[i]))*m.sin(0.5*w[j]*(t[i+1]-t[i]))/(w[j]*w[j])) 
                  )
        
       smp.append(ft
                  +(1*f[-1]*m.sin(w[j]*t[-1])/w[j]) #last point
                  -(1*f[0]*m.sin(t[0]*w[j])/w[j]) #first point
                  )
       
       
   dctvec=np.column_stack((w, smp))
   return dctvec

#--------------------------#
#--------------------------#
#nDCT
#w is the sampling vector in Fourier space, t are the x-values and f are the y-values of the input array
def nDST(w,t,f):
   smp=[]
   
   for j in range(len(w)): #loops through all sampling points w_i
       ft=0         
       for i in range(len(f)-1): # Fourier integral 
        ft+=(
            ((f[i+1]-f[i])/(t[i+1]-t[i])*(2)*m.cos(0.5*w[j]*(t[i+1]+t[i]))*m.sin(0.5*w[j]*(t[i+1]-t[i]))/(w[j]*w[j])) 
                  )
        
       smp.append(ft
                  -(1*f[-1]*m.cos(w[j]*t[-1])/w[j]) #last point
                  +(1*f[0]*m.cos(w[j]*t[0])/w[j]) #first point
                  )
       
       
   dstvec=np.column_stack((w, smp))
   return dstvec

#--------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------#
# Select and Import file
#Either, tkinter is used to open a dialog to specify the input file (2-column ascii) or
#the filename is manually specified (e.g. 'C:/Users/.../myfile.txt'). in the latter case, "tkinter.filedialog" is not required  

fileopt = [('SF','*.txt')] #define the file extension
filename = tkinter.filedialog.askopenfilename(filetypes=fileopt)    # opens a windows dialog to select and open an ascii file

#filename='C:/Users/Mayo/Desktop/Programme/Github/Filon FT/threesines.txt'
print(filename) # prints filename and directory of input file

with open(filename) as finp: #read input file
    content = finp.read().splitlines() # line-by-line reading with \n removed

#--------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------#
#Arrange the imported data 
tval=[];
fval=[];

for i in range(len(content)):
   (tval.append(content[i].split('\t')[0].replace(" ","")))
   (fval.append(content[i].split('\t')[1].replace(" ","")))
   
t=[float(i) for i in tval]; #converts string to float
f=[float(i) for i in fval]; #converts string to float

#create freq axis w_i=(t_i)^-1
w=[];
for i in range(len(t)):
   w.append(1/t[i]) #calculate the inverse of the times
   
w=w[::-1]   #reverse the list of frequencies

#--------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------#
#nDCT and nDST are computed for the frequencies w_i
start = timer() 
nDCT=nDCT(w,t,f)
nDST=nDST(w,t,f)
#--------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------#
#Write to file      
fsdct = open(filename[0:-4]+"_DCT.pef",'w') #create file for DCT
fsdst = open(filename[0:-4]+"_DST.pef",'w') #create file for DCT

for i in range(len(nDCT)): #write g(w) to files
            fsdct.write(str(nDCT[i,0]) + '\t' + str(nDCT[i,1])+ '\n')
            fsdst.write(str(nDST[i,0]) + '\t' + str(nDST[i,1])+ '\n')
            
#close files            
fsdct.close() 
fsdst.close() 
#--------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------#  
end = timer()
print('nDFT was successful. elapsed time: '+str(round(end - start,3))+'s')
