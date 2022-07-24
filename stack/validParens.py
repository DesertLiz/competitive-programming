# https://leetcode.com/problems/valid-parentheses/

# Iterate on string elements until items are exhaused or validity is disproven.
# Validity is maintained if each open symbol is added to the openSymbols (stack) and
# each closing symbol is matched with it's corresponding open symbol when checked
# by popping last item added fromt the stack

class Solution:
  def isValid(self, s: str) -> bool:
    symbolDict = { "(" : ")", "[" : "]", "{" : "}" }
    openSymbols = []

    for symbol in list(s):
      if(symbol in symbolDict):
        openSymbols.append(symbol)
      else:
        if(len(openSymbols) == 0):
          return False
        else: 
          popSymbol = openSymbols.pop()

          # case invalid s is caused by incorrect closing symbol e.g ( ]
          if(symbolDict[popSymbol] != symbol):
            return False

    # Handle cases where only open symbols are passed
    if(len(openSymbols) == 0):
      return True
    else:
      return False






# ==============================================

solution = Solution()

cases = ["((", "}", "()","()[]{}", "(]", "({([])})", "({([)})" ]

for case in cases:
  print("================")    
  print(case)
  print(solution.isValid(case))
