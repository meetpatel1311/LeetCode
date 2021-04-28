class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        d = {}
        c.sort()
        for i in range(1,target+1):
            d[i] = []
            for rec in c:
                if(rec>=i):
                    if(rec==i):
                        d[i].append([i])
                    break
                else:
                    if(d[i-rec]):
                        for rec1 in d[i-rec]:
                            l = []
                            l.append(rec)
                            l.extend(rec1)
                            l.sort()
                            if(l not in  d[i]):
                                d[i].append(l.copy())
        return d[target]
