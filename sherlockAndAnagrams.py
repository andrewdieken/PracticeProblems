import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    word_dict = {}

    for i in range(len(s)):
        string = s[i]
        while i <= len(s)-1:
            word_dict.setdefault(string, 0)
            i+=1
            if not i > len(s)-1:
                string+=s[i]

    for item in word_dict:
        print(item)






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
