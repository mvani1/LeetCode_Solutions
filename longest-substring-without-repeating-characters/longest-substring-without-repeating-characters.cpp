class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> mymap;
        int i = 0;
        int j =0 ;
        int ans = 0;
        while(i<s.size() && j<s.size()){
            if (mymap.find(s[j]) ==mymap.end()){
                            mymap.insert(s[j++]);
            ans = max(j-i,ans);

            }
            else{
mymap.erase(s[i++]);
        }}
        return ans;
    }
};