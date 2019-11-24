
# includes functions for analysis of transition matrices

import math
import numpy as np


# Get the euclidean distance between 2 matrices of the same dimensions
def distance(A,B):
	# make the matrices vectors for 
	#more easily calculating distance
	A_vec = A.flatten()
	B_vec = B.flatten()
	return euclid_dist(A_vec,B_vec)

# Get the n-dimensional euclidean distance between 2 vectors of the same length
def euclid_dist(A,B):
	s = 0
	for i in range(len(A[0].T)):
		s += (A[0,i] - B[0,i]) ** 2
	return math.sqrt(s)
		
# get the centroid from a collection of same dimension matrices
def centroid(M):
	s = np.zeros(len(M[0]),len(M[0]))
	m = np.asmatrix(s)
	for mat in M:
		m = numpy.add(m,mat)
	centroid = m/M.len()
	return centroid
		
		
