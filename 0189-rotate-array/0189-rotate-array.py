class Solution(object):
    def rotate(self, nums, k):

        n=len(nums)
        k=k%n
        nums[:]=list(nums[n-k:]+nums[:n-k])
 
        