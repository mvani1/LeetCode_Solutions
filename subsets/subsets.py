class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        APPROACH 1:
            Let's start from empty subset in output list. At each step one takes new integer into consideration and generates new subsets from the existing ones.
            
        TIME = SPACE = O(N*2^n)  to generate all subsets and then copy them into output list
        SPACE: 
        For a given number, it could be present or absent (i.e. binary choice) in a subset solution. As as result, for N numbers, we would have in total 2^N 
       
       CODE:
        subsets = [[]]
        for i in nums:
            subsets += [curr+[i] for curr in subsets]
        return(subsets) 
        
        
        
        APROACH 2: BAcktracking
        So, this time let us loop over the length of combination, rather than the candidate numbers, and generate all combinations for a given length with the help of backtracking technique.
        [[1] , [2] , [3]]
        [[1,2],[2,3],[1,3]]
        [[1,2,3]]
        We define a backtrack function named backtrack(first, curr) 
        which takes the index of first element to add and 
        a current combination as arguments.

        If the current combination is done, 
        we add the combination to the final output.

        Otherwise, we iterate over the indexes i 
        from first to the length of the entire sequence n.

        Add integer nums[i] into the current combination curr.

        Proceed to add more integers into the combination : 
        backtrack(i + 1, curr).

        Backtrack by removing nums[i] from curr.
        '''
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output