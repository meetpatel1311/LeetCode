class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]: 
        output = []
        i=0
        
        if(words and s):
            
            len_w = len(words)            
            len_words = len(words[0])
            len_s = len(s)
            while(i<=len_s - (len_w*len_words)):
                  words_copy = words.copy()
                  temp = s[i:i+len_words]
                  if(temp in words_copy):
                        j = i+len_words
                        words_copy.remove(temp)
                        while(words_copy):
                            temp = s[j:j+len_words]
                            j = j+len_words
                            if(temp in words_copy):
                                words_copy.remove(temp)
                            else:
                                break
                  if(not words_copy):
                        output.append(i)
                            
                  i = i+1
            return output
        else:
            return output
        
        
