class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> mymap;
        vector<int> ans;
        for(int i = 0; i<nums.size();i++){
            int finder = target - nums[i];
            if (mymap.find(finder) != mymap.end()){
                ans.push_back(mymap.find(finder)->second);
                ans.push_back(i);
                return ans;
            }
            mymap.insert({nums[i],i});
        }
        return ans;
        
}
};