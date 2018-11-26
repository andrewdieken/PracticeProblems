#===========================================================================
# Project: Interactive Dictionary
# Author: Andrew Dieken
# Date: 11/25/18
#===========================================================================

# Import json library
import json
import time
import difflib
from difflib import get_close_matches

# Function for retriving definition
def retriveDefinition(word):
    #convert word to all lower case
    word = word.lower()

    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean '{}' instead? [yes or no]: ".format(get_close_matches(word, data.keys())[0]))
        if action.lower() == 'yes':
            return data[get_close_matches(word, data.keys())[0]]
        elif action.lower() == 'no':
            return("The word '{}' doesn't exist, please double check it.".format(word))
    else:
        return("Sorry, we don't understand")

def formatOutput(output):
    if type(output) == list:
        for item in output:
            print('-',item)
    else:
        print('-',output)


# Main
if __name__ == '__main__':

    # Load the json dictionary named 'dictionary.json' into variable named 'data'
    print('Loading library...')
    time.sleep(1)
    data = json.load(open('dictionary.json'))
    print('Load complete')

    word_user = input('Enter a word: ')
    output = retriveDefinition(word_user)
    print(formatOutput(output))
