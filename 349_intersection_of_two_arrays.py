class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list_intersection = []
        for element in nums1:
            if element in nums2:
                list_intersection.append(element)

        return list(set(list_intersection))
