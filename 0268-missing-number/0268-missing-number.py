class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum_n=int((n*(n+1))/2)
        total=0
        for i in range(n):
            total+=nums[i]
        no=sum_n-total
        return no    