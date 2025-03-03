class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        S = len(gas)

        total_gas = 0
        cur_gas = 0
        si = 0

        for i in range(S):
            total_gas += gas[i] - cost[i]
            cur_gas += gas[i] - cost[i]

            if cur_gas < 0:
                si = i + 1
                cur_gas = 0

        return si if total_gas >= 0 else -1
