import csv
import re

from collections import defaultdict
from typing import List

class WordLengthTrie:
    def __init__(self):
        self.leaf = set()
        self.children = defaultdict(lambda: WordLengthTrie())

    def add_word(self, original: str, words: List[str]):
        if not words:
            self.leaf.add(original)
        else:
            word = words[0]
            remainder = words[1::]

            self.children[len(word)].add_word(original, remainder)

    def traverse(self):
        for word in self.leaf:
            yield word

        for child in self.children.values():
            yield from child.traverse()
        

word_length_trie = WordLengthTrie()

def save_title(title: str):
    words = re.findall(r'\w+', title)

    word_length_trie.add_word(title, words)

if __name__ == "__main__":
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            save_title(row[0])

    while True:
        known_letter = input("Known letter, leave empty to skip: ").strip().lower()

        if known_letter:
            known_letter_index = int(input("Known letter index: ").strip()) - 1

        query = input("Search query: ").strip()
        query_word_lengths = [int(c) for c in query.split(" ")]

        root = word_length_trie
        for index in query_word_lengths:
            root = root.children[index]

        print("----------------")

        for title in root.traverse():
            if not known_letter or re.findall(r'\w', title)[known_letter_index].lower() == known_letter:
                print(title)

        print("----------------")
            