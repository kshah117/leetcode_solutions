class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ret = []
        N = len(digits)

        for i in range(N):
            if digits[i] == 0:
                continue
            for j in range(N):
                if i == j:
                    continue
                for k in range(N):
                    if i == k or j == k or digits[k] % 2 == 1:
                        continue
                    ret.append(int(str(digits[i]) + str(digits[j]) + str(digits[k])))

        ret = list(set(ret))
        ret.sort()
        return ret

