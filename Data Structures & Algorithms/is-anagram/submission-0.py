from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        size_s = Counter(sorted(s))
        size_t = Counter(sorted(t)) 

        return True if size_s == size_t else False
        