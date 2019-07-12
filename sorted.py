class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if (len(nums1) ==0):
            nums1 = nums2
        else:
            j=0
            while len(nums2) != 0:

                if ((nums2[len(nums2)-1])) <= (nums1[0]):
                    nums1= nums2+nums1
                    nums2 = []
                elif((nums1[len(nums1)-1])) <= (nums2[0]):
                    nums1=nums1+nums2
                    nums2=[] 
                elif(nums2[0]) < nums1[0]:
                    
                    for i in range(len(nums2)):
                        if (nums2[i] >= nums1[0]):
                            nums1 = nums2[:i] + nums1
                            nums2= nums2 [i:]
                            break
                    
                elif(nums2[len(nums2)-1]) >= nums1[len(nums1)-1]:
                    for i in range((len(nums2)-1),0,-1):
                        if (nums2[i] <= nums1[len(nums1)-1]):

                            nums1 = nums1+nums2[i+1:]

                            nums2= nums2[:i+1]
                            break
                    
                elif((nums1[j]) <= (nums2[0])) and (nums1[j]!=nums1[j+1]) and  j<len(nums1):
                    
                    nums1 = nums1[:j+1]+[nums2[0]]+nums1[j+1:]
                    
                    nums2.remove(nums2[0])
                    
                j = j+1
            
                   
            
            
               
        
             
        print nums1
        if (len(nums1)%2) == 1:
            return (float(nums1[(len(nums1)//2)]))
        elif len(nums1) == 1:
            return float(nums1[0])
        else:
            median = (float((nums1[(len(nums1)//2)-1])+ (nums1[(len(nums1)//2)])))/2
            return median

num1=[3,9]
num2=[1,2,4,5,6,8]

med= Solution()
print med.findMedianSortedArrays(num1,num2)
