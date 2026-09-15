class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n=len(nums)
        nums_set=set(nums)
        for i in range(1,n+2):
            if i not in nums_set:
                return i

        