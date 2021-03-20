class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dict(dictionary)

    def __iter__(self):
        return self

    def __next__(self):
        while self.dictionary:
            key = next(iter(self.dictionary))
            value = self.dictionary[key]
            self.dictionary.pop(key)
            return key, value
        raise StopIteration()
