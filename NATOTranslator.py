class NATOTranslator:
    nato_alphabet = {
        'a': 'alpha',
        'b': 'bravo',
        'c': 'charlie',
        'd': 'delta',
        'e': 'echo',
        'f': 'foxtrot',
        'g': 'golf',
        'h': 'hotel',
        'i': 'india',
        'j': 'juliet',
        'k': 'kilo',
        'l': 'lima',
        'm': 'mike',
        'n': 'november',
        'o': 'oscar',
        'p': 'papa',
        'q': 'quebec',
        'r': 'romeo',
        's': 'sierra',
        't': 'tango',
        'u': 'uniform',
        'v': 'victor',
        'w': 'whiskey',
        'x': 'x-ray',
        'y': 'yankee',
        'z': 'zulu'
    }

    def translate_string(self, word):
        translation = []

        for letter in word:
            if letter.lower() not in self.nato_alphabet:
                translation.append(letter)
            else:
                translation.append(letter + " - " + self.nato_alphabet[letter.lower()])

        return translation