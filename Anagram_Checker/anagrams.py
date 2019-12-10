import sys

from anagram_checker import AnagramChecker


def menu():
    print("y) input a word")
    print("n) exit")
    choice = input("y/n? ").lower()
    if choice == 'n':
        print('Goodbye Son')
        sys.exit('too good for this world')
    elif choice == 'y':
        return valid_input(pick_word())


def pick_word():
    word = input('Please input one word now: ')
    return word


def valid_input(inputed_word):
    word = inputed_word.strip()
    with open('word_list.txt', 'r') as list:
        word_list = list.read().splitlines()
    if word.upper() in word_list and word.isalpha():
        return word
    else:
        print("please enter one valid word")
        menu()

def nice_display(word):
    print(f"Your word is: {word.word.upper()}")
    print("it was a valid entry")
    word.get_anagrams()
    print(f"The anagrams for your word are: {word.anagrams}")

if __name__ == '__main__':
     word = menu()
     word = AnagramChecker(word)
     nice_display(word)
