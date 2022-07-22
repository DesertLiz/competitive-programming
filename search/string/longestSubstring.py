# https://leetcode.com/problems/longest-substring-without-repeating-characters/


# Iterate through string with two pointers checking for unique substr, when we hit
# a repeat restart the search but setting start pointer 1 position beyond the repeated character idx

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    i,scoutIdx,currLen,maxLen,strLen = 0,0,0,0,len(s)
    charDict = {}

    while(scoutIdx < strLen):
        charOfInterest = s[scoutIdx]

        if(charOfInterest in charDict):
          # When repeat is found we no longer need to store any chars with index before the repreat
          unnecessaryChars = s[ i : charDict[charOfInterest] + 1 ]
          currLen -=len(unnecessaryChars)

          #  Adjust current window by moving 1 index beyond repeat
          i = charDict[charOfInterest] + 1

          #remove (now unnecessary) indexes before repeat
          [charDict.pop(key) for key in unnecessaryChars]
          
          # Replace original repeated char idx, with new scouted char idx
          charDict[charOfInterest] = scoutIdx
          currLen +=1

        else:
          charDict[s[scoutIdx]] = scoutIdx
          currLen +=1

          if(currLen > maxLen):
            maxLen = currLen

        scoutIdx+=1  

    return maxLen 



solution = Solution()

cases = ["aab", "dvdf", "dvdfatdv"]

for case in cases:
  print("================")    
  print(case)
  print(solution.lengthOfLongestSubstring(case))
