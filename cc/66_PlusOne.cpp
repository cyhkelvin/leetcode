class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1;
        for (int index = digits.size()-1 ; index > -1 ; index--){
            int add = digits[index]+carry;
            digits[index] = add%10;
            carry = add/10;
            //cout<<carry<<"\t"<<digits[index]<<"\t"<<index<<"\n";
            if (carry == 0){
                break;
            }
        }
        if (carry != 0){
            digits.insert(digits.begin(),carry);
        }
        return digits;
    }
};