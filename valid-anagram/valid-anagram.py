class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return dict(collections.Counter(s)) == dict(collections.Counter(t))