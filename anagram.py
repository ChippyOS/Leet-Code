class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        count = [0] * 26

        for i in range(len(s)):
            #Since they are lower case letters, 
            #it will subtract the hex value of whatever the letters are
            #and take that spot in the array and plus or equal it to 1
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1


        for num in count:
            if num != 0:
                return False
        
        return True
