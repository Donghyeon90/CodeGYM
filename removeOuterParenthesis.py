import collections
class Solution (object):
    def removeOuterParenthesis(self, s):
        
        #My idea was that there are going to be several completed parenthesis here.
        #I wanted to count the open and close brackets.
        #Then, I tried to remove outer parenthesis whenever there is one completed parenthesis set.
        #Then, I concanated together.

        countOpen=0
        countClose=0
        opclLinkedList= collections.deque()
        finalResult= ""

        for char in s: 
            if char == '(':
                opclLinkedList.append(char)
                countOpen+=1
            if char == ')':
                opclLinkedList.append(char)
                countClose+=1
            
            #Here, I found the one completed parenthesis set whenever there are same number of open and close brackets.
            #One another thing here, I need to check if the open and close brackets are more than 1
            #if I do not check for the 0, whenever this function starts, it will just start this if statement and will deque from none. 
            if countOpen == countClose and countOpen!=0:
                #I will pop the both outer parenthesis
                opclLinkedList.popleft()
                opclLinkedList.pop()
                while len(opclLinkedList)>0:
                    #Add rest of the parenthesis to the finalResult variable
                    finalResult += "".join(opclLinkedList.popleft())
        return finalResult
    


test = Solution()
#Test case 1
#Output for the test case1 supposed to be ""
print("Test case 1: "+test.removeOuterParenthesis("()()()()"))

#Test case 2
#Output for the test case2 supposed to be (())()
print("Test case 2: "+test.removeOuterParenthesis("((()))(())"))

#Test case 3
#Output for the test case3 supposed to be (())()()
print("Test case 3: "+test.removeOuterParenthesis("((()))(())(())"))
