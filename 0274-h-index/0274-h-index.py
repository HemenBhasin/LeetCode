class Solution:
    def hIndex(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        ans=0
        for i in range(len(arr)):
            if arr[i]>=i+1:
                ans=i+1
            else:
                break
        return ans            
