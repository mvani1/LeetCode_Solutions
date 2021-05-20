class Solution(object):
    def combinationSum(self, candidates, target):
        return self.back(candidates,target,[],[])
    def back(self,candidates,target,final,result):
        if target < 0 :
            return
        if target == 0:
            result.append(final)
            return 
        for i in range(len(candidates)):
            self.back(candidates[i:],target-candidates[i],final+[candidates[i]],result)
        return result            
