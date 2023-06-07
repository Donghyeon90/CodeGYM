#This takes the object and store as list.
#Then, sumRange function returns the sum of the whole integer list.


class NumArray(object):
    def __init__(self, nums):


        #This initilization function takes the object (list of numbers)
        #Then, store in the sums variable

        self.nums = nums
    

    def sumRange(self, left, right):
        #This function takes the start and end point of list, then returns the sum of the whole integers.

        return sum(self.nums[left,right+1])
    ################

    ##########