 class Solution:

    def encode(self, strs: List[str]) -> str:
        retString = ""
        
        for string in strs:
            retString += str(len(string)) + "#" + string

        return retString

    def decode(self, s: str) -> List[str]:
        i = 0

        resultList = []

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j + 1

            j = i + length

            resultList.append(s[i:j])

            i = j

        return resultList
            
        



