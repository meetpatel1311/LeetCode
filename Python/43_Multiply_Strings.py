class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_1 = 0
        num_2 = 0
        power1 = len(num1)-1
        power2 = len(num2)-1
        for rec in num1:
            d = ord(rec)-ord('0')
            num_1+=d * 10**power1
            power1 -=1
        for rec in num2:
            d = ord(rec)-ord('0')
            num_2+=d * 10**power2
            power2 -=1
        return str(num_1*num_2)
