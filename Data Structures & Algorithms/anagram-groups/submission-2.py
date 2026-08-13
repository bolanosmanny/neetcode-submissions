class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}

        for s in strs:
            alpha = [0] * 26
            for l in s:
                letter = ord(l) - ord('a')
                alpha[letter] = alpha[letter] + 1

            twins = tuple(alpha)

            if(twins in table):
                table[twins].append(s)
            else:
                table[twins] = [s]

        return list(table.values())

    




