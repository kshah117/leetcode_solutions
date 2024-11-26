class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        champs = []
        for i in range(n):
            is_champ = True
            for e in edges:
                if i == e[1]:
                    is_champ = False
                    break
            if is_champ:
                champs.append(i)
        if len(champs) == 1:
            return champs[0]
        else:
            return -1
