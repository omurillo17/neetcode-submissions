class Solution:
    def search(self, nums: List[int], target: int) -> int:
        izq = 0
        der = len(nums) - 1

        while izq <= der:
            mid = (izq + der) //2
            if nums[mid]== target:
                return mid
            elif nums[mid] < target:
                izq = mid + 1
            else:
                der = mid - 1
        return -1