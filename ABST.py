# MIT JJust Words
# https://www.mit.edu/~ecprice/wordlist.10000
from BST import BST

class Word ():
    def __init__(self, w):
        self.word = w

    # Less than
    def __lt__ (self, other):
        if (isinstance(other, Word)):
            return self.word < other.word

    # Greater than
    def __gt__ (self, other):
        if (isinstance(other, Word)):
            return self.word > other.word

    def __str__ (self):
        return self.word

# Alphabetical Binary Search Tree
class ABST (BST):
    def __init__(self):
        super().__init__()
        self.words = self.load_dictionary()
        print (f"Loaded {len(self.words)} words")
        for w in self.words:
            self.add (w)

        
    def load_dictionary (self):
        f = open('words.txt').read().split()
        l = []
        for word in f:
            if (word[0] == 'a'):
                l.append(Word(word))
        return l

    def check_word (self, w):
        return self.add (Word(w))
        # REMOVE TEMPORARY NODE

tree = ABST()
print (tree.check_word('apble'))
print (tree.someOrder())