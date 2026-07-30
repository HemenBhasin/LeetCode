class Solution:
    def climbStairs(self, n: int) -> int:
        arr=[0]*(n+1)
        arr[1]=1
        if n>=2:
            arr[2]=2
        for i in range(3,n+1):
            arr[i]=arr[i-1]+arr[i-2] 
        return arr[n]    
