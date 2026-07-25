class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isalphanum(c):

            return (('A') <= c <= ('Z') or
                    ('a') <= c <= ('z') or
                    ('0') <= c <= ('9'))
 
        l = 0

        r = len(s) - 1

        while l < r:

            while l < r and not isalphanum(s[l]):

                l += 1

            while r > l and not isalphanum(s[r]):

                r -= 1

            
            if s[l].lower() != s[r].lower():

                return False

            l += 1
            r -= 1

        return True

