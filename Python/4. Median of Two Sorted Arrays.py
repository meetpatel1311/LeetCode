class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        i = 0
        j = 0
        l=[]
        while(i<len_nums1 and j< len_nums2):
            first = nums1[i]
            second = nums2[j]
            if(first<=second):
                l.append(first)
                i+=1
            else:
                l.append(second)
                j+=1
        if(i==len_nums1):
            while(j<len_nums2):
                l.append(nums2[j])
                j+=1
        elif(j==len_nums2):
            while(i<len_nums1):
                l.append(nums1[i])
                i+=1
        len_l = len_nums1 + len_nums2
        if(len_l%2==1):
            return float(l[len_l//2])
        else:
            first = len_l//2
            second = first-1
            return (l[first]+l[second])/2
        
        
