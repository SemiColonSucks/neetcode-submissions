class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map1,hash_map2={},{}
        for i in s:
            if i in hash_map1:
                hash_map1[i]+=1
            else:
                hash_map1[i]=1
        
        for i in t:
            if i in hash_map2:
                hash_map2[i]+=1
            else:
                hash_map2[i]=1
        if len(s)>len(t):
            for i in hash_map1:
                if i not in hash_map2:
                    return False
                elif hash_map1[i]!=hash_map2[i]:
                    return False
            return True
        elif len(s)<len(t):
            for i in hash_map2:
                if i not in hash_map1:
                    return False
                elif hash_map1[i]!=hash_map2[i]:
                    return False
            return True
        else:
            for i in hash_map1:
                if i not in hash_map2:
                    return False
                elif hash_map1[i]!=hash_map2[i]:
                    return False
            return True
    
            