# 📘 Task 1: Extend Trie with Suffix and Prefix Methods

## 🧠 Goal

Extend a `Trie` class by implementing:

### 1. `count_words_with_suffix(pattern: str) -> int`

- Counts how many words in the trie **end with the given suffix**
- Case-sensitive
- Returns `0` if no such words
- Raises `TypeError` if `pattern` is not a string

### 2. `has_prefix(prefix: str) -> bool`

- Returns `True` if any word **starts with the given prefix**
- Returns `False` otherwise
- Case-sensitive
- Raises `TypeError` if `prefix` is not a string

---

## 🧪 Tests

```python
words = ["apple", "application", "banana", "cat"]

assert trie.count_words_with_suffix("e") == 1        # "apple"
assert trie.count_words_with_suffix("ion") == 1      # "application"
assert trie.count_words_with_suffix("a") == 1        # "banana"
assert trie.count_words_with_suffix("at") == 1       # "cat"

assert trie.has_prefix("app") == True
assert trie.has_prefix("bat") == False
assert trie.has_prefix("ban") == True
assert trie.has_prefix("ca") == True

```

## ✅ Requirements

- Class Homework inherits from Trie
- Efficient for large datasets
- Full input validation

# 📘 Task 2: Longest Common Prefix with Trie

## 🧠 Goal

Create a class LongestCommonWord that extends the base Trie class and implements the method:

find_longest_common_word(strings: List[str]) -> str

This method returns the longest common prefix shared by all strings in the input list.

## ✅ Functional Requirements

- Accepts a list of strings as input
- Returns the longest common prefix as a string
- Returns an empty string "" if:
  - No common prefix exists
  - The input list is empty
- Must raise a TypeError if the input is not a list of strings

## ⚙️ Time Complexity

- O(S) where S is the total number of characters in all input strings

## 🧪 Example Tests

["flower", "flow", "flight"] → "fl"
["interspecies", "interstellar", "interstate"] → "inters"
["dog", "racecar", "car"] → ""
[] → ""

## ✅ Acceptance Criteria

- Correctly finds the longest common prefix
- Returns an empty string when appropriate
- Handles invalid input and edge cases
- Passes all provided test cases
- Efficient on large lists of strings
