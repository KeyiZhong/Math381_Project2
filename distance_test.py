

#for all the directories
	#for all the files in a directory
		#wordLengthMatrix.py
		#put matrix in a list for the author


#for each author's list of matrices
	#compute centroid
	#put each centroid in a list of centroids

#for each book
	#calculate distance between the book and each of the centroids

import numpy as np
import analysis_functions as af

A = np.array([[1,2],[3,4]])
B = np.array([[0,1],[3,5]])
C = np.array([[1,3],[6,10]])

print(af.distance(np.asmatrix(A),np.asmatrix(C)))
#print(af.centroid([np.asmatrix(A),np.asmatrix(B),np.asmatrix(C)]))
