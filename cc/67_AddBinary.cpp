class Solution {
public:
    string addBinary(string a, string b) {
        //cout<<a.length()<<"\n";
        //cout<<a<<"\n";
        //int len = a.length()>b.length()? a.length():b.length();
        //cout<<len<<endl;
        //int c = 0;
        //int test = c==0? a[0]+'0':3;
        //cout<<"a[0]:"<<a[0]<<endl;
        //cout<<"a[0]+0:"<<a[0]+'0'<<endl;
        //cout<<"a[0]-0:"<<a[0]-'1'<<endl;
        //cout<<"test:"<<test<<endl;
        
        string s = "";
        int c = 0, i = a.length()-1, j = b.length()-1;
        while ( i >= 0 || j >= 0 || c != 0 ){
            c += i >= 0 ? a[i--] - '0' : 0;
            c += j >= 0 ? b[j--] - '0' : 0;
            s = char( c%2 + '0' ) + s;
            c /= 2;
        }
        
        
        return s;
    }
};