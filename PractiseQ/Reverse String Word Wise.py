# Reverse the given string word-wise. The last word in the given string should come at 1st place,
#  the last-second word at 2nd place, and so on. Individual words should remain as it is.

# Input Format:
# The first and only line of input contains a string without any leading and trailing spaces.
# Output Format :
# The only line of the output prints the Word wise reversed string.
# Constraints :
# 0 <= |S| <= 10^5
# where |S| represents the length of string, S.
# Sample Input 1:
# Welcome to Coding Ninjas
# Sample Output 1:
# Ninjas Coding to Welcome
# Sample Input 2:
# Always indent your code
# Sample Output 2:
# code your indent Always



def reverseStringWordWise(string):
    
    #Your code goes here
    l = string.split()
    l.reverse()
    str = " ".join(l)
    return str

    # or 
    
    arr = string.split()
    return " ".join(arr[::-1])





string = input()
ans = reverseStringWordWise(string)
print(ans)
        
