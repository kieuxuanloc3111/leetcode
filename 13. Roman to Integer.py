class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        i = 0
        value = 0
        while i < len(s):

            if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                value += roman_dict[s[i + 1]] - roman_dict[s[i]]
                i += 2
            else:
                value += roman_dict[s[i]]
                i += 1
        return value

s= "MCMXCIV"
a=Solution()
print(a.romanToInt(s))