class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_counter = 1
        zero_counter = 0
        zero_index = -1

        final_list = []
        for i in range(len(nums)):
            final_list.append(0)


        for i in range(len(nums)):
            if (nums[i] != 0):
                prod_counter *= nums[i]
            else:
                zero_counter += 1
                zero_index = i
                
            i += 1
        
        if zero_counter >= 2:
                return final_list

        if zero_counter == 1:
            final_list[zero_index] = prod_counter
            return final_list

        for i in range(len(nums)):
            final_list[i] = int(prod_counter / nums[i])

        return final_list        

                

        