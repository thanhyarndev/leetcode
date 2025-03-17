class Solution(object):
    def romanToInt(self, s):
        # Map of Roman numeral symbols to their corresponding integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        for i in range(len(s) - 1):
            # If the current numeral is smaller than the next, subtract it
            if roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        
        # Add the last symbol's value
        total += roman_map[s[-1]]
        
        return total
