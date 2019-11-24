# USE THIS FUNCTION INSTEAD
import numpy as np
# f should be a txt file
# return a np array 15 by 15
# as Dr.Conroy's suggestion, care only about word length that's less than 15
# so that the matrix won't be that sparse
def generate(f):
    file = open(f, "r")
    str = file.read()

    #substitute punctuations with space
    no_punct = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for cha in str:
        if cha not in punctuations:
            no_punct += cha
        else:
            no_punct += " "

    #split by white spaces
    words = no_punct.split()
    words = words[1:-1] # get rid of the first white space

    # dictionary of which key is the word length
    # value is another dictionary with kv pairs word length of next word, occurence
    row_dic = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i+1]
        cur_len = min(15, len(current_word))
        next_len = min(15, len(next_word))

        if cur_len in row_dic:
            dic = row_dic.get(cur_len)
            if next_len in dic:
                dic[next_len] += 1
            else:
                dic[next_len] = 1
        else:
            row_dic[cur_len] = {}
            row_dic.get(cur_len)[next_len] = 1
    # get the max length
    #print(row_dic)
    max_length = 15

    temp = []
    for i in range(1, max_length + 1):
        if i in row_dic:
            dic = row_dic.get(i)
            cur = []
            for i in range(1, max_length + 1):
                if i in dic:
                    cur.append(dic[i])
                else:
                    cur.append(0)
            temp.append(cur)
        else:
            # generate 0s
            cur = [0] * max_length
            temp.append(cur)

    # convert to prbabilities
    temp2 = []
    for i in range(len(temp)):
        lst = temp[i]
        total = sum(lst)
        lst2 = []
        if not(total == 0):
            for j in lst:
                lst2.append(j / total)
            temp2.append(lst2)
        else:
            cur = [0.0] * 15
            temp2.append(cur)
    x = [np.array(i) for i in temp2]
    return x

if __name__ == '__main__':
    generate("mark twain done/Those_Extraordinary_Twins_by_Mark_Twain.txt")
    print("ok")