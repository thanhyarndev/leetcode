class Solution(object):
    def longestCommonPrefix(self, strs):
       
        # Edge case: If the list is empty, return an empty string.
        if not strs:
            return ""
        
        # Start with the first string in the array as the initial prefix
        prefix = strs[0]
        
        # Compare this prefix with each string in the array
        for string in strs[1:]:
            # Update the prefix by checking common characters with each string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""  # If no common prefix, return an empty string
        
        return prefix
