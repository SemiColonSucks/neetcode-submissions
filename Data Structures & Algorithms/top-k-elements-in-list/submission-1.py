class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output=[]
        top_freq={}
        for i in range(len(nums)):
            if nums[i] in top_freq:
                top_freq[nums[i]]+=1
            else:
                top_freq[nums[i]]=1
        sorted_items = sorted(top_freq.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            output.append(sorted_items[i][0])
        return output