class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_sort=sorted(set(nums))
        longest=1
        current=1

        for i in range(1,len(num_sort)):
            if num_sort[i]==num_sort[i-1]+1:
                current+=1
                longest=max(longest,current)
            else:
                current=1   



        
        return longest 