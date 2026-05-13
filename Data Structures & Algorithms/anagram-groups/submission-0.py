class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = tuple(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        
        anagrams = []
        for word in groups.values():
            anagrams.append(word)
        
        return anagrams