class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        candidate=nums[n//2]
        count=0
        for num in nums:
            if num==candidate:
                count+=1
        if count>(n/2):
            return candidate
        return -1    
