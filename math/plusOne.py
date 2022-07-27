# https://leetcode.com/problems/plus-one/


from typing import List

class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    result = digits

    # No carry required just increment last digit
    if(digits[-1] != 9):
      result[-1] += 1
    else:
      # Carry required 
      carry = 1

      for i in range(len(digits)-1, -1, -1 ):
        if(digits[i] != 9 and carry):
          # Use up our carry and terminate as no further values need to be changed
          result[i] +=1
          break
        elif(digits[i] == 9):
          # Carry will continue in next iteration, set current digit to 0
          result[i] = 0
    

    # Leading zero indicates carry resulted in new leading digit 
    if(result[0] == 0):
      result = [1] + digits

    return result
    


# ==============================================

solution = Solution()

cases = [[1,2,3], [4,3,2,1], [9,9,9], [9,8,9], [1,0,0,0,9]]

for case in cases:
  print("================")    
  print(case)
  print(solution.plusOne(case))

      