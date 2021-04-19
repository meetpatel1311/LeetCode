class Solution:
    def intToRoman(self, num: int) -> str:
        th = ['','M','MM','MMM']
        hun  = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        ten = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones =  ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return th[num//1000]+hun[(num%1000)//100]+ten[(num%100)//10]+ones[num%10]
