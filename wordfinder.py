"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Random WordFinder
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """Read dictionary and show items read."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special WordFinder without blank lines & comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    4 words read

    >>> swf.random() in ["chocolate", "juice", "coffee", "danish"]
    True

    >>> swf.random() in ["chocolate", "juice", "coffee", "danish"]
    True

    >>> swf.random() in ["chocolate", "juice", "coffee", "danish"]
    True

    >>> swf.random() in ["chocolate", "juice", "coffee", "danish"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
    

 
