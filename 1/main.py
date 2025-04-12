from typing import List  # Import List from typing

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the complement and its index
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
