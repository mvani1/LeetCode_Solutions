class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n, mod = len(A), 10**9 + 7
        left, right = [None] * n, [None] * n 
        # Use list as stack
        s1, s2 = [], [] 

        # getting number of element strictly 
        # larger than A[i] on Left. 
        for i in range(0, n): 
            cnt = 1

            # get elements from stack until 
            # element greater than A[i] found 
            while len(s1) > 0 and s1[-1][0] > A[i]: 
                cnt += s1[-1][1] 
                s1.pop() 

            s1.append([A[i], cnt]) 
            left[i] = cnt 
        print(left)
        for i in range(n - 1, -1, -1): 
            cnt = 1

        # get elements from stack until 
        # element greater or equal to A[i] found 
            while len(s2) > 0 and s2[-1][0] >= A[i]: 
                cnt += s2[-1][1] 
                s2.pop() 

            s2.append([A[i], cnt]) 
            right[i] = cnt 
        c = 0
        for i in range(n):
            c += (A[i]*left[i]*right[i])
        return(c%mod)