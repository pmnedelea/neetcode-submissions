class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        found = set()
        
        for current in range(len(nums)):
            i = 0 
            j = len(nums) - 1
            
            while i<j:
                total = nums[i] + nums[j] + nums[current]

                if current == i:
                    i+=1
                elif current == j:
                    j-=1
                elif total < 0:
                    i+=1
                elif total > 0:
                    j-=1
                else:
                    found.add(tuple(sorted([nums[i], nums[j], nums[current]])))
                    j -= 1
                    i += 1

        results = list()
        for item in found:
            results.append(list(item))
        
        return results




        