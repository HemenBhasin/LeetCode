import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        combined = nums1 + nums2
        combined_sorted=sorted(combined)
        median_val = statistics.median(combined_sorted)
        return median_val