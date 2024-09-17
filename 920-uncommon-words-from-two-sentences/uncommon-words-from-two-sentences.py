class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        mp = {}
        retval = []

        split_s1 = s1.split()
        split_s2 = s2.split()
        sentence = split_s1 + split_s2
        for word in sentence:
            if word not in mp:
                mp[word] = 1
            else:
                mp[word] += 1
        for i in mp:
            if mp[i] == 1:
                retval.append(i)
        return retval