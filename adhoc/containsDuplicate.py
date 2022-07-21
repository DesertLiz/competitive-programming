class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(set(nums)) != len(nums)


    def containsDuplicate(self, nums) -> bool:
        hashset = set()

        for num in nums:
          if(num in hashset):
            return True
          
          hashset.add(num)

        return False



solution = Solution()

cases = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]

for case in cases:
  print("================")    
  print(case)
  print(solution.containsDuplicate(case))