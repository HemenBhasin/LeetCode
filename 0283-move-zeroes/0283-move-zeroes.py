class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroes=nums.count(0)
        if zeroes>0:
            nums[:] = [x for x in nums if x != 0]
            nums+=[0]*zeroes
            return nums
        else:
            return nums            

        