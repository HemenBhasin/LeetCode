class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        tickets=0
        farthest=0
        curr_end=0
        for limit in range(n-1):
            farthest=max(farthest,limit+nums[limit])
            if limit==curr_end:
                tickets+=1
                curr_end=farthest
        return tickets        