class Solution {
public:
    
    int numKLenSubstrNoRepeats(string s, int k) {
        unordered_set<int> mymap;
        int start = 0;
        int ans = 0;        
        for(int i =0;i<s.size();i++){
            while (mymap.count(s[i])){
                mymap.erase(s[start++]);
            }
            mymap.insert(s[i]);
            
            ans += i - start + 1 >= k;

            
        }
        return ans;
    }
};