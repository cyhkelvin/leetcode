class Solution {
public:
    string addStrings(string num1, string num2) {
        int carry = 0;
        int len1 = num1.size()-1, len2 = num2.size()-1;
        string s = "";
        while(len1>=0||len2>=0||carry!=0){
            carry += len1>=0? num1[len1--]-'0':0;
            carry += len2>=0? num2[len2--]-'0':0;
            s = to_string(carry%10) + s;
            carry /= 10;
        }
        return s;
    }
};

//seems like string.push_back(char(sum%10+'0')); and  reverse(res.begin(),res.end());  are faster than to_string() function