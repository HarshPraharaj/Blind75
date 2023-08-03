class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = Counter(ransomNote)
        dict2 = Counter(magazine)
        print(dict1)
        print(dict2)

        for k in dict1.keys():
            if dict1[k] > dict2[k]:
                return False
        return True
