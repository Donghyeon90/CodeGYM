class Solution(object):
    def calSteps(self, nums):


        """
        You can go up to 1 or 2 steps per time.
        If the input is 7, then how many ways to get to the target number?
        """

        """
        Think about the problem from the last to the front.

        1 2 3 4 5
        5 3 2 1 1

        """
        step1=1
        step2=1
        for i in range(nums-2):
            #I need to make this range(nums-2) because it is already start from 1+1 =2 which is 3rd step already 

            temp = step1
            step1 = step1+step2
            step2 = temp
            print("step1: " +str(step1))
            print("step2: " +str(step2))
            print("i : " + str(i) )
        
        return step1
    

test= Solution()

print(test.calSteps(5))

print(test.calSteps(7))



