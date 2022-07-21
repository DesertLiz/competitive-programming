# https://leetcode.com/problems/two-sum/

class Solution:

  #  Effectively asking: Does target minus current val exist in nums 
  def twoSum(self, nums, target):
    haystack = {}

    #  Stucture input data for easier search
    for idx, val in enumerate(nums):
      if(val in haystack):
        haystack[val].append(idx)
      else: 
        haystack[val] = [idx]

    #  Search for solution
    for val in nums:
      needle = target - val

      if(needle in haystack):
        sameIdx = haystack[needle][0] == haystack[val][0]

        if(len(haystack[needle]) >= 2):
          return [haystack[needle][0], haystack[needle][1]]
        elif(not sameIdx): 
          return [haystack[needle][0], haystack[val][0]]


  def twoSum(self, nums, target):
    haystack = {}

    for idx, val in enumerate(nums):
      needle = target - val

      if(needle in haystack):
        return [idx, haystack[needle]]

      haystack[val] = idx







solution = Solution()

cases = [ ([2,7,11,15],9), ([3,2,4],6), ([3,3], 6),([-3,4,3,90],0), ([2,5,5,11],10)]

for case in cases:
  print("================")    
  # print(case)
  print(solution.twoSum(case[0], case[1]))


