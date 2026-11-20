from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        need = Counter(t)
        missing = len(t)
        left = 0
        best_left, best_len = 0, len(s) + 1
        for right, char in enumerate(s):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            while missing == 0:
                window_len = right - left + 1
                if window_len < best_len:
                    best_left, best_len = left, window_len
                outgoing = s[left]
                need[outgoing] += 1
                if need[outgoing] > 0:
                    missing += 1
                left += 1
        return "" if best_len > len(s) else s[best_left:best_left + best_len]
