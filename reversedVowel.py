#==================================================
# Name: isVowel
# Parameters:
# - c -> character
# Return: True if parameter is an element in {a, e, i, o, u}, False else
#==================================================
def isVowel(c):
    return (c == 'a') or (c == 'e') or (c == 'i') or (c == 'o') or (c == 'u')

#==================================================
# Name: swap
# Parameters:
# - string -> string
# - left_pos -> int
# - right_pos -> int
# Return: string parameter with characters at left_pos and right_pos swaped
#==================================================
def swap(string, left_pos, right_pos):
    arr = []
    return_string = ''
    for i in range(len(string)):
        arr.append(string[i])
    arr[left_pos], arr[right_pos] = arr[right_pos], arr[left_pos]
    for item in arr:
        return_string+=item
    return return_string

#==================================================
# Name: reversed
# Parameters:
# - string -> string
# Return: string parameter with vowels swapped
#==================================================
def reversed(string):
    left = 0
    right = len(string)-1
    found_left = False
    found_right = False
    while left < right:
        while left < right and not isVowel(string[left]):
            left+=1
        if left != right:
            found_left = True
        while left < right and not isVowel(string[right]):
            right-=1
        if left != right:
            found_right = True
        # if isVowel(string[left]) and isVowel(string[right]):
        #     string = swap(string, left, right)
        if found_left and found_right:
            string = swap(string, left, right)
        left+=1
        right-=1
    return string


#==================================================
# Main
#==================================================
if __name__ == '__main__':
    string = 'apple'
    print(string)
    new_string = reversed(string)
    print(new_string)
