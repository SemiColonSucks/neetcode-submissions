class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=float('-inf')

        l,r=0,len(heights)-1
        while l<r:
            curr_water=(r-l)*min(heights[r],heights[l])
            if max_water<curr_water:
                max_water=curr_water
            if heights[r]<heights[l]:
                r-=1
            else:
                l+=1
        return max_water
