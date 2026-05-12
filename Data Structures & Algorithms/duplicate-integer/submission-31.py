class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = list()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.append(num)

        return False