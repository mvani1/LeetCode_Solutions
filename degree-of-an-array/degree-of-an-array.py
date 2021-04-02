class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums)<3 and len(set(nums))==len(nums):
            return 1
        h = {}
        maxi = (0,0)
        maxx = []
        for i in set(nums):
            h[i] = nums.count(i)
            if maxi[1]<h[i]:
                maxi = (i,h[i])
            if maxi[1] == h[i]:
                maxx.append((i,h[i]))
        k = (0,-1)
        maxx = list(map(lambda x: x if maxi[1] == x[1] else k,maxx))
        a = sorted(maxx,key=lambda x:x[1],reverse=True)
        minn = 999999
        for num in a:
            if num[1]!=-1:
                number , freq = num
                new = [i for i, n in enumerate(nums) if n == number]
                first,last = new[0],new[-1]
                length = (len(nums[first:last+1]))
                if minn > length:
                    minn = length
            
        return minn