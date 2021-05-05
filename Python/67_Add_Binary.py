class Solution:
    def addBinary(self, a: str, b: str) -> str:
        f = int(a,2)
        s = int(b,2)
        st = str(bin(f+s))
        return (st[2::])
