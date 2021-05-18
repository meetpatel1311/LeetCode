class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        x = False
        kharidyo = 0
        # vechyo = 0
        for i in range(0,len(prices)-1):
            temp1 = prices[i]
            temp2 = prices[i+1]
            if(x==False and temp1<temp2):
                x=True
                kharidyo = temp1
            elif(x==True and temp1>kharidyo and temp1>=temp2):
                x=False
                profit = profit + temp1-kharidyo
                kharidyo = 0
        if(x==True and temp2>kharidyo):
            profit = profit + temp2 - kharidyo
        return profit
