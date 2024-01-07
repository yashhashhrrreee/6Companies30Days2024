class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n = len(nums[0])
        re = []

        for k, trim in queries:
            L = [(int(s[n-trim:]), i) for i, s in enumerate(nums)]
            heapify(L)
            re.append(nsmallest(k, L)[-1][1])
        
        return re