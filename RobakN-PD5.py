def code_type(inp):
    input = inp.upper()
    dict = {}
    if input == "G":
        dict = {'G': 'A', 'D': 'E', 'R': 'Y', 'P': 'O', 'L': 'U', 'K': 'I'}
    elif input == "P":
        dict = {'P': 'O', 'L': 'I', 'T': 'Y', 'K': 'A', 'R': 'E', 'N': 'U'}
    else:
        for i in range(0, len(input)):
            if i % 2 == 0:
                dict[input[i]] = input[i + 1]
    #print(dict)
    return dict


def find_key(letter, dict):
    for key, value in dict.items():
        if letter == value:
            return key


def translate(word, code):
    dict = code_type(code)
    result = []
    for el in word.upper():
        if el in dict.keys():
            result.append(dict[el])
        elif el in dict.values():
            result.append(find_key(el, dict))
        else:
            result.append(el)
    return ''.join(result)


def find_repetition(code):
    lst = list(code)
    for i in range(0, len(lst) - 1):
        for j in range(len(lst) - 1, 0, -1):
            if lst[i] == lst[j] and i != j:
                return True
    return False


def code_input():
    code = input("Which code do you want to use? Type G for GADERYPOLUKI, \n"
                 "P for POLITYKARENU or type your own code using letters only, \n"
                 "just like in the examples above. ")
    #while (len(code)):
    while (len(code) == 1 and (code.upper() != 'P' and code.upper() != 'G')):
        print("You used wrong letter. ")
        code = input("Try again ")
    while (len(code) != 1 and len(code) % 2 == 1):
        print("Your code is not proper - use even number of letters.")
        code = input("Try again ")
    while (len(code) != 1 and find_repetition(code) == True):
        print("Your code is not proper - repeating letters found.")
        code = input("Try again: ")
    return code


def main():
    code = code_input()
    word = input("Now enter the text you want to translate. ")
    print(translate(word, code))


main()
