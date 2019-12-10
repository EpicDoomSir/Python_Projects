class AnagramChecker:
    def __init__(self, word):
        self.word = word.upper()
        self.anagrams = []
        with open('word_list.txt', 'r') as list:
            self.word_list = list.read().splitlines()

    def is_anagram(self, other_word):
        if self.word == other_word or len(self.word)!= len(other_word):
            return False
        letters = list(other_word)
        try:
            for letter in self.word:
                letters.remove(letter)
            return True
        except ValueError:
            return False

    def get_anagrams(self):
        for word in self.word_list:
            if self.is_anagram(word):
                self.anagrams.append(word)
