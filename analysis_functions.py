
# includes functions for analysis of transition matrices

import math
import numpy as np


# Get the euclidean distance between 2 matrices of the same dimensions
def distance(A,B):
	# make the matrices vectors for 
	#more easily calculating distance
	A_vec = A.flatten()
	B_vec = B.flatten()
	A_list = A_vec.tolist()
	B_list = B_vec.tolist()
	return euclid_dist(A_list,B_list)

# Get the n-dimensional euclidean distance between 2 lists of the same length
def euclid_dist(A,B)
	sum = 0
	for (i in range(A.len)):
		sum += (A[i] - B[i]) ** 2
	return math.sqrt(sum)
		
# get the centroid from a collection of same dimension matrices
def centroid(M)
	sum = np.zeros(10,10);
	sum = np.asmatrix(sum)
	for(mat in M):
		sum = numpy.add(sum,mat)
	centroid = sum/M.len()
	return centroid
		
		
