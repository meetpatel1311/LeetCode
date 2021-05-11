class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[0:m] + nums2[0:n]
        nums3.sort()
        for i in range(len(nums1)):
            nums1[i] = nums3[i]
