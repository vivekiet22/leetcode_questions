class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        ans = []
        # print(len(pattern))
        for word in words:
            d = {}
            for i in range(len(pattern)):
                if pattern[i] in d.keys():
                    if d[pattern[i]] != word[i]:
                        break
                        
                if word[i] in d.values():
                    # print(word)
                    # print("entered")
                    k = "k"
                    for j in d.keys():
                        if d[j] == word[i] :
                            k = j
                            # print(j)
                            # print(pattern[i])
                    if pattern[i] != k:
                        break
                else:
                    d[pattern[i] ] = word[i]
                    # d[word[i]] = pattern[i]
                print(d)
                if i == len(pattern)-1:
                    ans.append(word)
        # print(ans)  
        return ans
