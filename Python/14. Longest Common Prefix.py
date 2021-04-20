class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        if(strs):
            if(len(strs)==1):
                return strs[0]
            len_strs = len(strs)
            temp = min(strs,key=len)
            len_temp = len(temp)
            for i in range(0,len_temp):
                gg=''
                search = temp[0:i+1]
                for rec in strs:
                    gg = gg + " " + rec[0:i+1]
                if(gg.count(search) != len_strs):
                    return s
                s = search
            if(s):
                return temp
            else:
                return ''
        else:
            return ''
                
