class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if(s):
            c = 0
            temp = ''
            l=[]
            for rec in s:
                if(rec=='('):
                    c=c+1
                    temp = temp + rec
                else:
                    c=c-1
                    if(c<0):
                        c=0
                        if(temp):
                            l.append(temp)            
                            temp = ''
                    else:
                        temp = temp + rec
            if(temp):
                if(c>0):
                    c=0
                    temp = temp[::-1]
                    temp2=''
                    for rec in temp:
                        if(rec==')'):
                            c = c + 1 
                            temp2 = temp2 + rec
                        else:
                            c= c-1
                            if(c<0):
                                c=0
                                if(temp2):
                                    l.append(temp2[::-1])
                                    temp2=''
                            else:
                                temp2 = temp2 + rec
                    if(temp2):
                        l.append(temp2[::-1])
                    
                else:
                    l.append(temp)
            if(l):
                return(len(max(l,key=len)))
            else:
                return 0
        else:
            return 0
