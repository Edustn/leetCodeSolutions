class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        historic = {}

        for index, element in enumerate(nums):
            if element in historic:
                oldHistoric = historic[element] 
                distance = index - oldHistoric

                if distance <= k:
                    return True
            historic[element] = index


        return False