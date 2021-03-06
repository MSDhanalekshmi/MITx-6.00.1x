# Write an iterative function iterPower(base, exp) that calculates the exponential base ^ exp  by simply using successive multiplication. For example, iterPower(base, exp) should compute base ^ exp by multiplying base times itself exp times. Write such a function below.

# This function should take in two values - base can be a float or an integer; exp will be an integer  0. It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.


def iterpower(base,exp,result=1):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    for i in range (exp):
        result *= base
    return result


# using while loop


def iterPower(base,exp):

    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -=1
    return result



    #correct





    
