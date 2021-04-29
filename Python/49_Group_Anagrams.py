class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[]
        d={}
        ans=[]
        jj = 0
        for rec in strs:
            l.append(str(''.join(sorted(rec))))
        for i in range(0,len(l)):
            temp = l[i]
            if(temp in d.keys()):
                ans[d[temp]].append(strs[i])
            else:
                m=[]
                ans.append(m)
                d[temp]=jj
                jj+=1
                ans[d[temp]].append(strs[i])
        return ans
            
