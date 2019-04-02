# LINK TO PROBLEM: https://www.hackerrank.com/challenges/kmp-problem/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign


#!/bin/python3

import os
import sys
import string

#
# Complete the kmp function below.
#
def kmp(x):
    returnString = ""
    alphabet = list(string.ascii_lowercase)
    for i in range(len(x)):
        for loop in range(x[i]):
            returnString += alphabet[i]

    kmp[1] = 0;
    for (i = 2; i <= len(returnString); i = i + 1){
        l = kmp[i - 1];
        while (l > 0 && returnString[i] != returnString[l + 1]){
            l = kmp[l];
        }
        if (returnString[i] == returnString[l + 1]){
            kmp[i] = l + 1;
        }
        else{
            kmp[i] = 0;
        }
    }
    print(len(kmp))
    return returnString

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = list(map(int, input().rstrip().split()))

    result = kmp(x)

    fptr.write(result + '\n')

    fptr.close()
