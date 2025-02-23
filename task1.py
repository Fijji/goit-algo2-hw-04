import pygtrie

class Homework:
    def __init__(self):
        self.trie = pygtrie.CharTrie()

    def add_word(self, word: str, index: int):
        self.trie[word] = index

    def count_words_with_suffix(self, pattern: str) -> int:
        if not isinstance(pattern, str) or not pattern:
            raise ValueError("Pattern має бути непорожнім рядком")

        return sum(1 for word in self.trie.keys() if word.endswith(pattern))

    def has_prefix(self, prefix: str) -> bool:
        if not isinstance(prefix, str) or not prefix:
            raise ValueError("Prefix має бути непорожнім рядком")

        return self.trie.has_subtrie(prefix)

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]

    for i, word in enumerate(words):
        trie.add_word(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat
