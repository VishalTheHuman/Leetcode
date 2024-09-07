class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        indices = []
        for i in range(len(s1)): 
            if s1[i]!=s2[i]: 
                indices.append(i)

            if len(indices) > 2:
                return False
        
        return not(len(indices) == 1 or (len(indices)==2 and (s1[indices[0]]!= s2[indices[1]] or s1[indices[1]]!=s2[indices[0]])))
