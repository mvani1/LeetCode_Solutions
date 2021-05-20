class Solution:
    '''
    Brute :
    Instead of making a double length copy of numsnums array , we can traverse circularly in the numsnums array by making use of the \text{%(modulus)} operator. For every element nums[i]nums[i], we start searching in the numsnums array(of length nn) from the index (i+1)%n(i+1) and look at the next(cicularly) n-1n−1 elements. For nums[i]nums[i] we do so by scanning over nums[j]nums[j], such that (i+1)%n &leq; j &leq; (i+(n-1))%n(i+1), and we look for the first greater element found. If no such element is found, we put a \text{-1}-1 at the appropriate position in the resres array.
    
    Time = O(n^2)
    Space = O(n)
    '''
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        Time = O(n)
        Space = O(n)
        '''
        res = [0 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<= nums[i%len(nums)]:
                stack.pop()
            res[i%len(nums)] = -1 if not stack else nums[stack[-1]]
            stack.append(i%len(nums))
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<= nums[i%len(nums)]:
                stack.pop()
            res[i%len(nums)] = -1 if not stack else nums[stack[-1]]
            stack.append(i%len(nums))
        return res