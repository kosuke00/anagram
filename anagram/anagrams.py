from collections import Counter
import os

module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'words.txt')   #full path to text.
data_file = open(file_path)
hand = data_file.read().split()

def find_anagrams(name):
    """Read name & dictionary file & display all anagrams in name """
    name_letter_map = Counter(name)
    anagrams = []
    w = ""
    for word in hand:
        test = ""
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)

    if len(anagrams) > 0:
        for word in anagrams:
            w += "["+word + "]"+" "
    else:
        w += "no words left"
    return w


def process_choice(name,choice):
    """check user choice for validity, return choice & leftover letters."""
    left_over_list = list(name)
    if choice == "":
        pass
    elif choice == "#":
        sys.exit()
    else:
        candidate = "".join(choice.lower().split())
        for letter in candidate:
            if letter in left_over_list:
                 left_over_list.remove(letter)
        if len(name) - len(left_over_list)  == len(candidate):
            name = "".join(left_over_list)
        else:
            print("wont work! make another choice!", file=sys.stderr)
    name = "".join(left_over_list)
    return choice, name
