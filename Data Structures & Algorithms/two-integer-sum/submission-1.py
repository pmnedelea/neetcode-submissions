class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {nums[0]: 0}
        
        for i in range(1,len(nums)):
            if a.get(target - nums[i]) != None:
                return [a[target - nums[i]],i]
            a[nums[i]] = i

            

