import copy
class Solution:

    def insert(self, l: List[List[int]], n: List[int]) -> List[List[int]]:
    
        l.append(n)
        l.sort()
        x=False
        y = False
        
        for i in range(1,len(l)):
        
            curr_min = l[i][0]
            if(l[i-1][0]<=curr_min and curr_min<=l[i-1][1]):
                curr_max = l[i][1]
                if(i==len(l)-1):
                    l[i-1][1] = max(l[i-1][1],curr_max)
                    l.pop()
                else:
                    if(l[i-1][1]>curr_max):
                        new_max = l[i-1][1]
                        for j in range(i+1,len(l)):
                        
                            if(l[j][0]==new_max):
                                l[i-1][1] = l[j][1]
                                x=True
                                break
                            elif(l[j][0]>new_max):
                                y=True
                                l[i-1][1] = max(new_max,l[j-1][1])
                                break
                        if(x):
                            for k in range(j,i-1,-1):
                                l.pop(k)
                        elif(y):
                            for k in range(j-1,i-1,-1):
                                l.pop(k)
                        else:
                            l[i-1][1] = max(new_max,l[-1][1])
                            for k in range(i,len(l)):
                                l.pop()
                        
                        break
                    else:
                        for j in range(i+1,len(l)):
                        
                            if(l[j][0]==curr_max):
                                l[i-1][1] = l[j][1]
                                x=True
                                break
                            elif(l[j][0]>curr_max):
                                y=True
                                l[i-1][1] = max(curr_max,l[j-1][1])
                                break
                        if(x):
                            for k in range(j,i-1,-1):
                                l.pop(k)
                        elif(y):
                            for k in range(j-1,i-1,-1):
                                l.pop(k)
                        else:
                            l[i-1][1] = max(curr_max,l[-1][1])
                            for k in range(i,len(l)):
                                l.pop()
                break
        return l
