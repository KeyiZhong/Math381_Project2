# transition matrix for word length

# read a txt file
# should be able to pass in different txt files
file = open("245-0.txt", 'r')
str = file.read()

# to eliminate punctuations
no_punct = ""
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for cha in str:
    if cha not in punctuations:
        no_punct += cha
# then split by white spaces
words = no_punct.split()
# get rid of the first blank
words = words[1:-1]
# dictionary of which key is the word length
# value is another dictionary with kv pairs word length of next word, occurence
row_dic = {}
for i in range(len(words)):
    if not (i == (len(words) - 1)):
        current_word = words[i]
        next_word = words[i+1]
        if len(current_word) in row_dic:
            dic = row_dic.get(len(current_word))
            if len(next_word) in dic:
                dic[len(next_word)] += 1
            else:
                dic[len(next_word)] = 1
        else:
            row_dic[len(current_word)] = {}
            row_dic.get(len(current_word))[len(next_word)] = 1

# sort the dictionary keys and find the max word length
sort_dic = sorted(row_dic.keys())
sort_dic
# 41 for this specific book LIFE IN MISSISSIPPI

# assume the maximum length word not occur at the last position
max_length = max(sort_dic)
max_length

# generate matrix using np array
import numpy as np
temp = []
for i in range(1, max_length + 1):
    if i in row_dic:
        dic = row_dic.get(i)
        cur = []
        for i in range(1, max_length):
            if i in dic:
                cur.append(dic[i])
            else:
                cur.append(0)
        temp.append(cur)
    else:
        # generate 0s
        cur = [0] * max_length
        temp.append(cur)

x = [np.array(i) for i in temp]
matrix = np.asmatrix(x)
