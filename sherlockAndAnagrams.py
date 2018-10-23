#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    # word = "hey"
    # print(word[::-1])


    anagrams = 0
    word_dict = {}

    for i in range(len(s)):
        string = s[i]
        while i <= len(s)-1:
            word_dict.setdefault(string, 0)
            word_dict[string]+=1
            i+=1
            if not i > len(s)-1:
                string+=s[i]

    for string in word_dict:
        print(string + ' : ' + str(word_dict[string]))
        temp_dict = {}
        if len(string) == 1 and word_dict[string] > 1:
            temp_dict.setdefault(string, 0)
        else:
            perm_string = string[1:] + string[0]
            while perm_string != string:
                #print(string +' '+ perm_string)
                temp_dict.setdefault(perm_string, 0)
                perm_string = perm_string[1:] + perm_string[0]

        #Go through each permutation and check if its in 's'
        for perm in temp_dict:
            if perm in s:
                anagrams+=1
                #print(perm)





    return anagrams






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
