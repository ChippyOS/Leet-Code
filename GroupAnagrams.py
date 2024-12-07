 class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        finalList = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord("a")] += 1
            
            finalList[tuple(count)].append(string)
        return list(finalList.values())

