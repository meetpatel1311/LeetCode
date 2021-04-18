class Solution:
    def myAtoi(self, str: str) -> int:
        l = str.split(" ")
        oper = ""
        for rec in l:
            if(rec!=''):
                oper = rec
                break
        if(oper==''):
            return 0
        else:
            sign = "+"
            temp = oper[0]
            if(temp=='-' or temp=='+'):
                sign = temp
                oper = oper[1::]            
            new=''
            for rec in oper:
                if(rec.isdigit()==False):
                    break
                new = new+rec
            if(new==""):
                return 0
            else:
                num = int(new)
                if(sign=='-'):
                    num = 0-num
                if(num>=2**31):
                    return 2**31-1
                elif(num<-2**31):
                    return -2**31
                else:
                    return num 
