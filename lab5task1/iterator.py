from collections.abc import Iterable, Iterator

class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection, reverse=False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value

class WordsCollection(Iterable):
    def __init__(self, collection=[]):
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, reverse=True)

def main():
    collection = WordsCollection(["apple", "banana", "cherry"])
    print("Straight iteration:")
    for element in collection:
        print(element)

    print("\nReverse iteration:")
    for element in collection.reverse_iterator():
        print(element)


if __name__ == "__main__":
    main()
