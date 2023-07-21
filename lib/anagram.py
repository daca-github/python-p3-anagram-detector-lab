# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = sorted(word.lower())

    def match(self, words):
        return [word for word in words if sorted(word) == self.word]