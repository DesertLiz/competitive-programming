# https://leetcode.com/problems/valid-palindrome/

class Solution:

  def isPalindrome(self, s: str) -> bool:
    processed = "".join(list(filter(is_valid, s.lower())))

    return processed == processed[::-1]


#  Utility function to check charcter validity
def is_valid(character):
  char_code = ord(character)
  char_range = range(ord('a'), ord('z') + 1)
  digit_range = range(ord('0'), ord('9') + 1)

  return char_code in char_range or char_code in digit_range



solution = Solution()

cases = ["A man, a plan, a canal: Panama"]

for case in cases:
  print("================")    
  print(case)
  print(solution.isPalindrome(case))

