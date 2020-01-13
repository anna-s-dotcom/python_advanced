# Erstelle einen Iterator welchter einen Satz übergeben bekommt.
# Es soll die einzelnen Wörter als Elemente beinhalten/ausgeben.

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence[:-1].split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.sentence):
            self.index = 0
            raise StopIteration
        else:
            self.index += 1
            return self.sentence[self.index-1]

sentence = Sentence('Hello World!')

for word in sentence:
    print(word)
for word in sentence:
    print(word)
# > Hello
# > World
# > ! (Optional)
