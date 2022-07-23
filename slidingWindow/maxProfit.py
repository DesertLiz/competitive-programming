# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

# Use scout to iterate over prices comparing to lowestBuy to find highest
# possible profit. If a better (or equivalent) price is found than the 
# current lowestBuy advance window and restart the search 

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    lowestBuy, scoutIdx, maxProfit = prices[0], 0, 0
    
    while(scoutIdx < len(prices)):
      if(prices[scoutIdx] <= lowestBuy):
        # Found better buying opportunity, advance window start idx, restart search
        lowestBuy = prices[scoutIdx]

      else:
        # Window contains profitable opportunity, compare to current maxProfit
        possibleProfit = prices[scoutIdx] - lowestBuy

        if(maxProfit < possibleProfit):
          maxProfit = possibleProfit

      scoutIdx+=1

    return maxProfit



# ==============================================

solution = Solution()

cases = [[7,1,5,3,6,4],[7,6,4,3,1], [0], [1], [3,2,1], [1,0,1,10000], [1,2,0,2]]

for case in cases:
  print("================")    
  print(case)
  print(solution.maxProfit(case))
