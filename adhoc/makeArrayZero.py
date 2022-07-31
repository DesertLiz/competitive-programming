# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

from typing import List

# Key insight is that each distinct element will needs its own operation to have
# it's value zeroed out, thus number of operations is simply numbers of distinct 
# elements. With edge case of [0] which requires no operations to zero out 
class Solution:
  def minimumOperations(self, nums: List[int]) -> int:
    nums = set(nums)
    operations = len(nums)

    if(0 in nums):
      operations-=1

    return operations



# ==============================================

solution = Solution()

cases = [[1,5,0,3,5], [0], [9,9,6,6,3,3,1,1]]

for case in cases:
  print("================")    
  print(case)
  print(solution.minimumOperations(case))

      