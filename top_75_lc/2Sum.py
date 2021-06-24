# Approach - 1, N^2, 1


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_len = len(nums)
        for num1_pos in range(0, nums_len):
            for num2_pos in range(num1_pos + 1, nums_len):
                if nums[num1_pos] + nums[num2_pos] == target:
                    return [num1_pos, num2_pos]


# Approach - 2, N, N
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map_pos = dict()
        nums_len = len(nums)
        for pos in range(0, nums_len):
            if nums[pos] in map_pos.keys():

                if 2 * nums[pos] == target:
                    return [pos, map_pos[nums[pos]]]
            else:

                map_pos[nums[pos]] = pos

        for key in map_pos.keys():
            complement = target - key

            if complement in map_pos.keys() and complement != key:

                return [map_pos[key], map_pos[complement]]