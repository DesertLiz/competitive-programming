# https://leetcode.com/problems/binary-search/

from typing import List

# Since input array is sorted we can choose a middle value and compare it
# to our target. While termination condition is if middle equals target.
# If target is less than middle work with only first half or array, etc. 

class Solution:
	def search(self, nums: List[int], target: int) -> int:
		start, end= 0, len(nums) - 1
		middle = end // 2

		while(nums[middle] != target):
			# no solution exists if our border indexes cross each other
			if(start > end):
				return -1

			# Adjust border indexes based on where target is relative to border values
			if(nums[middle] > target):
				end = middle - 1
			else:
				start = middle + 1

			# Re-calculate middle as average of current border indexes
			middle = (start + end) // 2
		
		return middle


# ==============================================

solution = Solution()

cases = [
		{"nums": [-1,0,3,5,9,12], "target": 9},
	 	{"nums": [-1,0,3,5,9,12], "target": 2}
	]


for case in cases:
  print("================")    
  print(case)
  print(solution.search(case["nums"], case["target"]))
