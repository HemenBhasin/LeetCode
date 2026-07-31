class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        minSize=n+1
        curr=0
        left=0
        for i in range(n):
            curr+=nums[i]
            while curr>=target:
                minSize=min(minSize,i-left+1)
                curr-=nums[left]
                left+=1
        return 0 if minSize>n else minSize        