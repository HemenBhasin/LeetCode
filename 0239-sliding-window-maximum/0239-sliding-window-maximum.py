import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # deque will store the indices of the elements, not the elements themselves
        q = collections.deque()
        ans = []        
        for i in range(len(nums)):
            # 1. Remove the front element if it's outside the current window bounds
            if q and q[0] < i - k + 1:
                q.popleft()               
            # 2. Remove all elements from the back that are smaller than the current element
            # They are useless because the current element is bigger and appears later
            while q and nums[q[-1]] < nums[i]:
                q.pop()                
            # 3. Add the current element's index to the back of the queue
            q.append(i)            
            # 4. Once we have processed at least 'k' elements, start adding to our answer
            # The largest element is ALWAYS at the front of our deque
            if i >= k - 1:
                ans.append(nums[q[0]])                
        return ans