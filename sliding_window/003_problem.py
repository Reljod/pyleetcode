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
    return 0

def test_get_longest_substr_length() -> None:
    string_longest_map = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("reljodoreta", 6)
    ]

    for string, expected_length in string_longest_map:
        assert get_longest_substr_length(string) == expected_length
