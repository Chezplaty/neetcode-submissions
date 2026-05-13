from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        res = []

        for word in strs:
            groups[tuple(sorted(word))].append(word)
        
        for value in groups.values():
            res.append(value)
        
        return res

