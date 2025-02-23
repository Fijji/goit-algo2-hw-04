import pygtrie

class LongestCommonWord(pygtrie.CharTrie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise ValueError("Вхідні дані -> список рядків!")

        if not strings:
            return ""
        if len(strings) == 1:
            return strings[0]

        for word in strings:
            self[word] = True

        prefix = strings[0]
        for word in strings[1:]:
            new_prefix = ""
            for i in range(min(len(prefix), len(word))):
                if prefix[i] == word[i]:
                    new_prefix += prefix[i]
                else:
                    break

            prefix = new_prefix
            if not prefix:
                return ""
        return prefix

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
