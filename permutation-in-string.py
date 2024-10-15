class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1 = {}
        for c in s1:
            m1[c] = m1.get(c, 0) + 1
        
        for i in range(len(s2)):
            m2 = m1.copy()
            for j in range(i, len(s2)):
                c2 = s2[j]

                if c2 not in m2:
                    break
                
                m2[c2] -= 1
                if m2.get(c2) == 0:
                    m2.pop(c2)

                if len(m2) == 0:
                    return True

        return False
        
sol = Solution()
print(sol.checkInclusion("adc", "dcda"))
            
            

            