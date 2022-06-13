"""var7, task1"""

class First:
    """Class to represent work with word.

    Attributes:
    ------------
        word: str
            word to work with
        consonants: list
            list of constants
        vowels: list
            list of vowels
    """

    def __init__(self, word):
        self.word = word
        self.consonants = self._make_vowels_consonants(self.word)[1]
        self.vowels = self._make_vowels_consonants(self.word)[0]

    def __eq__(self, other):
        for symbol in self.consonants:
            if self.consonants.count(symbol) != 1:
                return False
        return True

    def __ne__(self, other):
        if not self == other:
            return True
        return False

    def __str__(self):
        string = f"First(consonants={self.consonants}, vowels={self.vowels})"
        return string

    # destructive
    def clear_vowels(self):
        """Delete all vowels from word."""
        new_word = []
        for symbol in self.word:
            if symbol not in self.vowels:
                new_word.append(symbol)
        self.vowels.clear()
        self.word = new_word

    # non-destructive
    def cleared_vowels(self):
        """Create new First from old word without vowels."""
        new_word = []
        for symbol in self.word:
            if symbol not in self.vowels:
                new_word.append(symbol)
        return First("".join(new_word))

    def _make_vowels_consonants(self, word):
        """Create two lists: vowels and constants."""
        vowels_list = ["a", "e", "i", "o", "u", "y"]
        vowels = []
        consonants = []
        for symbol in word:
            if symbol.lower() in vowels_list:
                vowels.append(symbol)
            else:
                consonants.append(symbol)
        return vowels, consonants

class Second(First):
    """Class to represent extended work with word.

    Attributes:
        word: str
            word to work with
        consonants: list
            list of constants
        vowels: list
            list of vowels
        shift: int
            number for shifting letters in encoding
    """

    def __init__(self, word, shift):
        super().__init__(word)
        self.shift = shift

    def encoder(self):
        """Encode old word and create new Second from encoded word."""
        new_word = []
        for symbol in self.consonants:
            new_word.append(chr(ord(symbol)+5))
        for symbol in self.vowels:
            new_word.append(chr(ord(symbol)+5))
        return Second("".join(new_word), 0)
