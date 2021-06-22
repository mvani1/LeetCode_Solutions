class Solution {
public:
    bool isValid(string s) {
      stack<char> stk;
        if (s.length() == 0)return true;
        if (s.length() == 1)return false;
        for(int i =0;i<s.size();++i){
            char c = s[i];
            cout << c;
            if(c=='}'||c==')'||c==']'){
                if(stk.size()==0)return false;
                else if(c=='}'&&stk.top()!='{')return false;                                 else if(c==')'&&stk.top()!='(')return false;
                else if(c==']'&&stk.top()!='[')return false;
                stk.pop();
            }
            else stk.push(c);
        }
        if (stk.size()>0)return false;
        return true;
    }
};