class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Step 1: If x is negative or ends with zero but is not zero itself, it's not a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Step 2: Reverse the second half of the number
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Step 3: If x is equal to reversed_half or x equals reversed_half // 10 (for odd-length numbers)
        return x == reversed_half or x == reversed_half // 10
