class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxsum=nums[0]
        currsum=0
        for num in nums:
            if currsum<0:
                currsum=0
            currsum+=num
            maxsum=max(maxsum,currsum)
        return maxsum        