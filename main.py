

#for all the directories
	#for all the files in a directory
		#wordLengthMatrix.py
		#put matrix in a list for the author


#for each author's list of matrices
	#compute centroid
	#put each centroid in a list of centroids

#for each book
	#calculate distance between the book and each of the centroids


import analysis_functions as af
import generateMatrix as gm
import os
import os.path
import numpy as np

authors = ['mark twain', 'charles dickens', 'Jane Austen', 'Leo Tolstoy', 'Virginia Woolf', 'F. Scott Fitzgerald',
          'Lewis Carroll', 'Mary Shelley', 'Herman Melville', 'Oscar Wilde', 'Arthur Conan Doyle']



# return the map with key being name of a book and value is the transition matrix
# param author's name
def savematrices(author):
    directory = author + " done/"
    files = os.listdir(directory)
    matrices = {}
    for file in files:
        if not file == ".DS_Store" and not os.stat(directory+file).st_size == 0:
            matrix = gm.generate(directory+file)
            matrices.update({file: matrix})
    return matrices


# return the centroid of one author,
# param transition matrices of this author
def get_centroid(matrices):
    collection = []
    for key in matrices:
        collection.append(matrices.get(key))
    centroid = af.centroid(collection)
    return centroid


# class book:
#     def __init__(self,transition, centroidDistMap):
#         self.centroid = centroidDistMap
#         self.transition = transition


def main():
    centroids = {}
    transitionM = {}
    for author in authors:
        if not os.path.exists(author):
            os.makedirs(author)
        transition_matrices = savematrices(author)
        for bookName in transition_matrices:
            folder_name = bookName[:-4]
            matrix = transition_matrices.get(bookName)
            transitionM.update({bookName:matrix})
            if not os.path.exists(author + "/" + folder_name):
                os.makedirs(author + "/" + folder_name)
            np.savetxt(author + "/" + folder_name + "/transition_matrix.csv", matrix, delimiter=",")
        centroid = get_centroid(transition_matrices)
        centroids.update({author: centroid})
        np.savetxt(author+"/centroid_matrix.csv", centroid, delimiter=",")
    for author in authors:
        dist_to_centroids = {}
        files = os.listdir(author+"/")
        for file in files:
            if not file == ".DS_Store" and not os.stat(author + "/" + file).st_size == 0 and not file == "centroid_matrix.csv":
                transition_matrix = transitionM.get(file+".txt")
                print(file)
                for key in centroids:
                    dist_to_centroids.update({key:af.distance(np.asmatrix(transition_matrix),centroids.get(key))})
                distances = ""
                for key in dist_to_centroids:
                    distances = distances + key + " " + str(dist_to_centroids.get(key)) + " "
                    print(distances)
                f = open(author+"/"+file+"/distance_to_authors.txt", "w+")
                f.write(distances)
                f.close()


if __name__ == '__main__':
    main()

    print("ok")
