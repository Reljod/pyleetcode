"""
From leetcode:

Given a string s, find the length of the longest substring
without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

def get_longest_substr_length(string: str) -> int:
    # TODO: Improve performance since this only beats 35% of python codes in leetcode.
    s_ptr = 0
    longest_substr_len = 0
    substr_set = set()

    for end_ptr in range(len(string)):
        while (string[end_ptr] in substr_set):
            substr_set.remove(string[s_ptr])
            s_ptr += 1
        else:
            substr_set.add(string[end_ptr])

        longest_substr_len = max(longest_substr_len, len(substr_set))

    return longest_substr_len

def test_get_longest_substr_length() -> None:
    string_longest_map = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("reljodoreta", 6)
    ]

    for string, expected_length in string_longest_map:
        assert get_longest_substr_length(string) == expected_length

def test_get_longest_substr_length_on_empty_string() -> None:
    string = ""
    expected_length = 0

    assert get_longest_substr_length(string) == expected_length
