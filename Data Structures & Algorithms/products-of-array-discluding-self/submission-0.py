class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod=[1]*len(nums)
        prefix_prod[0]=1
        
        suffix_prod=[1]*len(nums)

        for i in range(1,len(nums)):
            prefix_prod[i]=prefix_prod[i-1]*nums[i-1]
        print(prefix_prod)

        for i in range(len(nums)-2,-1,-1):
            suffix_prod[i]=suffix_prod[i+1]*nums[i+1]
        print(suffix_prod)

        result=[]
        for i in range(len(nums)):
            result.append(prefix_prod[i]*suffix_prod[i])
        return result
