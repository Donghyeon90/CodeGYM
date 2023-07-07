#Find how many 1's bits in the given string.

def hammingWeight (n):

    #Integer will be given and feed to this function.
    #Need to get a binary format of the given number.
    #Then, put that string into a list and count how many 1's in the list.

    binStr= bin(n)
    binList= list(binStr)

    count = 0

    for i in binList:
        if i =="1":
            count+=1

    return count

