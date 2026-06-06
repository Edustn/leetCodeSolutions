class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list_intersection = [] 
        for element in nums1:
            if element in nums2:
                list_intersection.append(element)
                nums2[nums2.index(element)] = -1
        return (list_intersection)