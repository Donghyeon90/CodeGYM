import collections
class Solution(object):
    def isValid(self, s ):


        #Things I need to check 
        TYPE_CHECK = {'(':')', '{':'}', '[':']'}

        #stack for checking open and close bracket
        opclStack = collections.deque()

        for char in s :
            if char in '({[':
                #if char is open bracket, then put that into the stack
                opclStack.append(char)
            if char in ')}]':
                #if char is close bracket, then check if the stack has something or not.
                #if its empty, that means there is no open bracket to match with the close brack.
                #so it will return false 
                if len(opclStack) == 0:
                    return False
                #Also, here we need to check if the open and close bracket are the same type
                elif TYPE_CHECK[opclStack[-1]] != char:
                    return False
                #it is correct type open and close bracket, so it will just pop the open bracket in the stack
                else:
                    opclStack.pop()

        #return true if there is no char in the stack at the end of the process.
        return True

test = Solution()
#Test cases 
print(test.isValid("()()()"))
print(test.isValid("()(){}"))
print(test.isValid("()[]{}"))
print(test.isValid("(}){()()}"))
