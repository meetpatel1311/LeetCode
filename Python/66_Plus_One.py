class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for rec in digits:
            s = s+ str(rec)
        temp = int(s) +1
        digits.clear()
        for rec in str(temp):
            digits.append(int(rec))
        return digits
