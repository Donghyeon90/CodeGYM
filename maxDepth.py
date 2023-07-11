import collections

class Solutions(object):
    def maxDepth(self, s):


        #Variables
        countDepth=0
        opclStack= collections.deque()


        for char in s:
            if char =='(':
                opclStack.append(char)

            if char== ')':

                if len(opclStack)>countDepth:
                    countDepth= len(opclStack)

                opclStack.pop()
        return countDepth
    

test =Solutions()
#Test case 1: Maxdepth is 4
print(test.maxDepth("(((()())))"))
#Test case 2: Max depth is 5
print(test.maxDepth("((((())()()()()9)))"))
#Test case 3: Max depth is 2
print(test.maxDepth("(()())"))