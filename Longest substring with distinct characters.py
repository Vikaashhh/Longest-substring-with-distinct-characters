class Solution:
    def longestUniqueSubstr(self, s):
        n = len(s)
        last_seen = {}  # stores the last index of each character
        max_len = 0
        start = 0  # start of the current window

        for end in range(n):
            char = s[end]

            # If character is already seen and is within the current window
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1  # move start next to the last seen character

            last_seen[char] = end  # update the last seen index
            max_len = max(max_len, end - start + 1)

        return max_len
