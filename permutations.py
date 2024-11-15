class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Logic
        # Get all permutations excluding first element
        # Insert the first element at all possible positions of the permtation
        # Return the new permutations upstream
        # Repeat 


        if not nums:
            return [[]]
        ret = []

        all_perms = self.permute(nums[1:])

        for perm in all_perms:
            for i in range(len(perm) + 1):
                perm_copy = perm.copy()
                perm_copy.insert(i, nums[0])
                ret.append(perm_copy)

        return ret
        