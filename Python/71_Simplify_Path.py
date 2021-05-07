class Solution:
    def simplifyPath(self, s: str) -> str:
        count = s.count('/')
        for i in range(count,1,-1):
            s=s.replace('/'*i,'/')
        l = s.split('/')
        count = l.count("")           
        for i in range(count):
            l.remove("")
        len_l=len(l)
        i=0
        j=0
        while(j<len_l):
            j+=1
            if(l[i]=='..'):
                l.pop(i)
                if(i>0):
                    l.pop(i-1)
                    i=i-1
                
            elif(l[i]=='.'):
                l.pop(i)
            else:
                i+=1
        return "/"+"/".join(l)
