class Solution(object):
    def maxProduct(self, nums):
        minimum=nums[0]
        maximum=nums[0]
        ans=maximum
        for i in range(1,len(nums)):
            curr=nums[i]
            t1=max(curr*maximum,curr*minimum)
            tempmax=max(curr,t1)
            t2=min(curr*maximum,curr*minimum)
            minimum=min(curr,t2)
            maximum=tempmax
            ans=max(maximum,ans)
        return ans    