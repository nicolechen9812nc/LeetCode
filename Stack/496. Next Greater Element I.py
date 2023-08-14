#The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

#You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

#For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

#Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        for i in range(0,len(nums1)):
            
            for j in range(0,len(nums2)):
            
                flag,val = 1,0
                if nums1[i]==nums2[j]:
                    val = nums2[j]
        
                    for k in range(j+1,len(nums2)):
                        if nums2[k] > val:
                            ans.append(nums2[k])
                            flag = 0
                            break
                    
                    if flag == 1:
                        ans.append(-1)
        return ans
