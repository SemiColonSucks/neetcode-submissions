class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map={}
        for s in strs:
            k="".join(sorted(s))
            print(k)
            if k not in anagram_map:
                anagram_map[k]=[]
            anagram_map[k].append(s)
        return list(anagram_map.values())