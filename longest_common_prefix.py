from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise TypeError("Input must be a list of strings")
        if not strings:
            return ""

        shortest = min(strings, key=len)
        for i in range(len(shortest)):
            char = shortest[i]
            for word in strings:
                if word[i] != char:
                    return shortest[:i]
        return shortest



if __name__ == "__main__":
    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["flower", "flow", "flight"]) == "fl"
    assert trie.find_longest_common_word(["interspecies", "interstellar", "interstate"]) == "inters"
    assert trie.find_longest_common_word(["dog", "racecar", "car"]) == ""
    assert trie.find_longest_common_word([]) == ""
