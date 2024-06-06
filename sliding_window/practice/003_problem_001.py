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

def main():

    # s = "abcabcbb"
    # s = "bbbbb"
    s = "dvdf"
    # s = "pwwkew"
    # s = "reljodoreta"
    # s = ""

    left = 0
    max_len = 0
    substr_set = set()

    for right in range(len(s)):

        while(s[right] in substr_set):
            substr_set.remove(s[left])
            left += 1
        else:
            substr_set.add(s[right])

        max_len = max(max_len, len(substr_set))

    print(f"max len: {max_len}")

if __name__ == "__main__":
    main()
