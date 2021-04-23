class Solution:
    def isValid(self, s: str) -> bool:
        if(s==''):
            return True            
        temp = s[0]    
        if(temp==')' or temp==']' or temp=='}'):
            return False
        l=['t']
        x=False
        for temp in s:
            if(temp=='(' or temp=='[' or temp=='{'):
                l.append(temp)
            else:
                rr = l[len(l)-1]
                if(temp==')'):
                    if(rr != '('):
                        x=True
                        break
                elif(temp==']'):
                    if(rr != '['):
                        x=True
                        break
                else:
                    if(rr != '{'):
                        x=True
                        break
                l.pop()
        # print(l,x)
        if(x):
            return False
        else:
            del l[0]
            if(len(l)>0):
                return False
            else:
                
                return True
