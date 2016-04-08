#217. Contains Duplicate
def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l==0 or l==1:
            return False
        else:
            nums.sort()
            i=0
            while i < l -1:
                if nums[i] ==nums[i+1]:
                    return True
                i = i+1
            return False    

#66. Plus One
def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry =1
        for i in range(len(digits)-1,-1,-1):
            sum = digits[i] +carry
            carry = sum//10 
            digits[i] = sum%10
        if carry == 0:
            return digits
        else:
            digits.insert(0,carry)
            return digits

#189. Rotate Array
def __rv(self,nums,st,end):
        while end > st:
            temp =nums[end]
            nums[end] = nums[st]
            nums[st] = temp
            end = end-1
            st = st +1
            
def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.__rv(nums,0,len(nums)-1)
        self.__rv(nums,0,k-1)
        self.__rv(nums,k,len(nums)-1)

#27. Remove Element
def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = []
        i = 0
        while i < len(nums):
            if nums[i]==val:
                del nums[i]
                i = i -1
            i = i + 1
#26. Remove Duplicates from Sorted Array
def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) -1:
            if nums[i] == nums[i+1]:   
                del nums[i+1]
            else:                       # I think this should be observed 
                i = i+1
