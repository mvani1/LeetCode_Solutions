class Solution {
    public String lastSubstring(String s) {
        if(s == null || s.length() < 2)
            return s;
        char[] chars = s.toCharArray();
        int start = 0;
        int i = 1;
        
        while(i < chars.length){
            if(chars[start] > chars[i]){
                i++;
            }
            else if(chars[start] < chars[i]){
                start = i;
                i++;
            }
            else{
                int j = start;
                int k = i;
                while(k < chars.length && chars[j] == chars[k]){
                    j++;
                    k++;
                }
                if(k == chars.length)
                    break;
                if(chars[k] > chars[start]){
                    start = k;
                    i = k+1;
                    continue;
                }
                if(chars[j] > chars[k]){
                    i = k+1;
                }
                else{
                    start = i;
                    i++;
                }
            }
        }
        
        return s.substring(start);
    }
}
    
