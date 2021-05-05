class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if(words):
            len_words = len(words)
            if(len_words==1):
                s = words[0]
                s = s + " "*(maxWidth - len(s))
                l=[]
                l.append(s)
                return l
            else:
                c = 0
                i=0
                ans = []
                while(i<len_words):
                    len_temp = 0
                    l=[]
                    while(True and i<len_words):
                        my = words[i]
                        len_temp = len_temp + len(my) + 1
                        # print(my,len_temp)
                        if(len_temp>maxWidth+1):
                            break
                        l.append(my)     
                        i = i + 1
                        
                    ans.append(l)
                l = []
                for i in range(0,len(ans)-1):
                    len_ = 0
                    temp = ans[i].copy()
                    len_ans = len(temp)
                    
                    for rec in temp: 
                        len_ = len_ + len(rec)
                    if(len_ans==1):
                        ans[i].append(" "*(maxWidth-len(rec)))
                    else:
                        spaces = maxWidth - len_
                        equall = spaces//(len_ans - 1)
                        remaining = spaces % (len_ans-1)
                        for j in range(1,(len_ans*2) - 1,2):
                            if(remaining==0):
                                ans[i].insert(j," "*equall)
                            else:
                                ans[i].insert(j," "*(equall+1))
                                remaining = remaining -1
                s=''
                for rec in (ans[-1]):
                    s = s + rec + " "
                len_s = len(s)
                if(len_s>maxWidth):
                    s = s[0:maxWidth]
                else:
                    s = s + " "*(maxWidth - len_s)
                for i in range (len(ans)-1):
                    temp = ''
                    for rec in ans[i]:
                        temp = temp + rec
                    l.append(temp)
                l.append(s)
                return l
