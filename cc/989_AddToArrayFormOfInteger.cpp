class Solution {
public:
    vector<int> addToArrayForm(vector<int>& A, int K) {
        if(A.size() == 0) return A;
        int m = A.size() - 1, c = 0;
        vector<int> res;
        while(m >= 0 || K > 0 || c == 1) {
            int x = (m >= 0 ? A[m--] : 0) + (K % 10) + c; 
            res.push_back(x % 10);
            c = x / 10;
            K = K / 10;
        }
        std::reverse(res.begin(), res.end());
        
        //string K_str = to_string(K);
        //int A_len = A.size()-1;
        //int K_len = K_str.size()-1;
        //int carry = 0;
        ////cout<<A_len<<" "<<K_len<<" "<<carry<<endl;
        ////int len = A_len>K_len? A_len:K_len;
        //vector<int> res;
        //while (A_len>=0 || K_len>=0 || carry !=0){
        //    //for ( int j=0; j<res.size(); j++){
        //    //    cout<<res[j]<<" ";
        //    //}cout<<"\n";
        //    res.insert(res.begin(),carry);
        //    res[0] += K_len>=0 ? K_str[K_len --] - '0':0;
        //    res[0] += A_len>=0 ? A[A_len --]:0;
        //    carry = res[0]/10;
        //    res[0] = res[0]%10;
        //}
        
//a - '0' is equivalent to ((int)a) - ((int)'0'), which means the ascii values of the characters are subtracted from each other. Since 0 comes directly before 1 in the ascii table (and so on until 9), the difference between the two gives the number that the character a represents.
            
        return res;
    }
};