class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        n1=n2=n3=-inf
        for i in range(len(nums)):
            if nums[i]>n1:
                n3=n2
                n2=n1
                n1=nums[i]
            elif nums[i]>n2 and nums[i]!=n1:
                n3=n2
                n2=nums[i]
            elif nums[i]>n3 and nums[i]!=n1 and nums[i]!=n2:
                n3=nums[i]
        if n3 in nums:
            return n3
        else:
            return n1               
                