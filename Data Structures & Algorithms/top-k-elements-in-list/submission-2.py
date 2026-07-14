class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets=dict((x,[]) for x in range(len(nums)+1))
        top_freq={}
        output=[]
        for i in range(len(nums)):
            if nums[i] in top_freq:
                top_freq[nums[i]]+=1
            else:
                top_freq[nums[i]]=1

        for i,j in top_freq.items():
            if j in buckets:
                buckets[j].append(i)
        
        print(buckets)
        for i in range(len(nums),-1,-1):
                if i in buckets:
                    for num in buckets[i]:
                        output.append(num)
                        if len(output)==k:
                            return output
        