class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        for f in fruits:
            placed = False
            for j in range(len(baskets)):
                if baskets[j] >= f:
                    baskets[j] = 0
                    placed = True
                    break
            if not placed:
                unplaced += 1
        return unplaced