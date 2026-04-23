class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = {1, 2}
        my_set.remove(1)
        my_set.remove(2)
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False
        