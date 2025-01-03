# Time Complexity : o(log n)
# Space Complexity : o(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach in three sentences only
# https://leetcode.com/problems/find-peak-element/ 


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return left