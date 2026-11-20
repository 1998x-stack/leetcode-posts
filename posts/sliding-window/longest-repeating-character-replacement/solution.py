class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = best = 0
        for right, char in enumerate(s):
            count[ord(char) - ord('A')] += 1
            max_freq = max(count)
            while right - left + 1 - max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
                max_freq = max(count)
            best = max(best, right - left + 1)
        return best
