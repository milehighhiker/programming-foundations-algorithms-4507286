class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = dict()
        for c in s:
            if c in s_map.keys():
                s_map[c] += 1
            else:
                s_map[c] = 1
        
        t_map = dict()
        for c in t:
            if c in t_map.keys():
                t_map[c] += 1
            else:
                t_map[c] = 1

        for v1, v2 in s_map.values(), t_map.values():
            if v1 != v2:
                return False

        return True
