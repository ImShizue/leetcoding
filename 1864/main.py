class Solution:
	def minSwaps(self, s: str) -> int:
		count_0 = s.count('0')
		count_1 = s.count('1')

		if abs(count_0 - count_1) > 1:
			return -1

		def count_swaps(pattern):
			swaps = 0
			for i in range(len(s)):
				if s[i] != pattern[i]:
					swaps += 1
			return swaps // 2

		pattern1 = ''.join(['0' if i % 2 == 0 else '1' for i in range(len(s))])
		pattern2 = ''.join(['1' if i % 2 == 0 else '0' for i in range(len(s))])

		if count_0 == count_1:
			return min(count_swaps(pattern1), count_swaps(pattern2))
		elif count_0 > count_1:
			return count_swaps(pattern1)
		else:
			return count_swaps(pattern2)

if __name__ == "__main__":
	solution = Solution()
	print(solution.minSwaps("111000"))  # Output: 1
	print(solution.minSwaps("010"))     # Output: 0
	print(solution.minSwaps("1110"))    # Output: -1
