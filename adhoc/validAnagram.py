# https://leetcode.com/problems/valid-anagram/

from collections import Counter

class Solution:

  def isAnagram(self, s: str, t: str) -> bool:
    char_count = {}

    for letter in s:
      char_count[letter] = char_count[letter] + 1 if letter in char_count else 1


    for letter in t:
      if(letter not in char_count or char_count[letter] == 0):
        return False
      else:
        char_count[letter] -=1


    remaining_chars = sum(char_count.values())

    return True if remaining_chars == 0 else False



  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True        

  def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


  def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

            

              



solution = Solution()

cases = [["anagram", "nagaram"], ["rat", "car"]]

for case in cases:
  print("================")    
  print(case)
  print(solution.isAnagram(case[0], case[1]))