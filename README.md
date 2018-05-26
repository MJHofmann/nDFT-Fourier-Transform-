# nDFT-Fourier-Transform-
Python script for calculating Cosine and Sine transformation of nonuniformly sampled data (nDFT, nDCT, nDST)
A simple algorithm for calculating numerical non-uniform discrete Fourier transforms
Marius Johannes Hofmann

PLEASE CHECK OUT THE PDF FILE FOR THEORY AND EXAMPLES

	Introduction
In science the problem of calculating Fourier transforms of experimental data numerically, is very common. The cosine and the sine transformation are two such variations:

g_C (ω)=∫f(t)cos(ωt)dt              
g_S (ω)=∫f(t)sin(ωt)dt

Here, f(t) could be a time signal, for instance, and  g_(C,S) (w) the corresponding frequency-domain spectra. 
The physicists definition of angular frequency ω=2πν is chosen. Conventional Discrete Fourier transform (DFT) algorithms 
often implemented in commercially available software products such as Fast Fourier Transform (FFT) often require evenly spaced data points.
However, when data extends over several orders of magnitude, the equidistant spacing is unfavorable and logarithmic spacing is preferred, 
for instance. Another typical case of unevenly spaced data occurs when compiling data recorded with different instruments or measured 
under different conditions. An example is time/frequency – temperature superposition. In such cases, non-uniform DFT (nDFT) is required. 
One simple approach is described here. It is based on the pioneering work of Filon [1] and was further developed by Blochowicz et al. [2] 
and Rivera et al. [3].


	Usage of the Python script
The program calculates the Discrete Fourier Transform of nonuniformly spaced data (nDFT) in terms of the Nonuniform 
Discrete Cosine Transform (nDCT) and the Nonuniform Discrete Sine Transform (nDST). The code is intentionally kept short and simple. 
The only thing needed is a 2-column ASCII file separated by “tab” with the first column containing the x-values t_i and the 
second one the y-values f(t_i ). Remove headers and special symbols (NaN etc.) and copies of data points 
(especially two consecutive t_i with the same value), to avoid division-by-zero. Here is an example:

0.00010375284158180127	0.9999055897634689
0.00010423174293933036	0.9999051540081028
0.00010471285480508996	0.9999047162415895
0.00010519618738232224	0.9999042764546475
0.00010568175092136585	0.9999038346379535
…and so on…



From the Python, side numpy is required. tkinter can be used to Browse through the file system and specify an input file. 
Alternatively, the input file can be specified directly in the script, by uncommenting and changing the line 

filename='C:/… /inputfile.txt'
accordingly. Two new files (ASCII 2-column arrays) will be created by the script in the directory of the input file, containing 
the nDCT and the nDST, respectively.

filename_DCT.pef
filename_DST.pef
As Python is comparatively slow, and given the complexity O(N^2) , computation might take several seconds. 
Using two nested for-loops for computation is unfavorable but computation can be accelerated using parallelization 
(not implemented in this version). In future work, C code will be implemented to accelerate computation.


VI. 	References
[1]	Filon, L. N. Proc. Roy. Soc. Edinburgh 1928, 49, 38-47. 
[2]	Blochowicz, T.  Ph.D. thesis, University of Bayreuth, Germany, 2003.
[3]	Rivera, A.; Blochowicz, T.; Gainaru, C.; Rössler, E. A. J. Appl. Phys. 2004, 96, 5607.

Comments are appreciated,
Thank you!

