
def isPalindrome(s):
    def toChar (s):
        ans = ''
        for c in s:
            if c in 'acbdcefghijklmnopqrstuvwxyz':
                ans += c
        return ans


    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal (s[1 : -1])
    return isPal(toChar(s))
           

print("Is malayalam a palindrome or not ?")
print (isPalindrome("malayalam"))