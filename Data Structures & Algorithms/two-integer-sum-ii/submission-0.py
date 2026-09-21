class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        izq = 0
        der = len(numbers) - 1
        
        while izq <= der:
            suma = numbers[izq]+ numbers[der]
            if suma == target:
                return [izq+1, der+1]
            elif suma < target:
                izq += 1
            else:
                der -= 1
        return []