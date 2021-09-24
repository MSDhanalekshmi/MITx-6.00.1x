def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a < b :
        temp = a
        a = b
        b = temp

        
    if b == 0:
        return a
    else:
        return gcdRecur (b, a % b )

# correct
    