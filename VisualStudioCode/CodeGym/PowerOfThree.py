#LeetCode Practice


def isPowerOfThree( n):

    #return True if the n is power of 3
    #otherwise return False.

    #How are you going to solve this problem?
    #First,  I will check if the number is less than 1 or not. 
    #Second, I will constantly check n mod 3 ==0 whcih means it can be divided by the 3.
    #Third, I will use // floor division to make sure the result is always integer here instead of using regular division.
    # 

    if n <1:
        return False
    else:
        while (n%3==0):
            n= n//3

    if n ==1:
        return True
    else:
        return False 


