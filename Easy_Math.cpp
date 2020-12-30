// Question Link https://www.codechef.com/problems/RPD

#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    
    while(t-- > 0){
        int n,v,c,s,ans=0;
        
        cin>>n;
        
        int arr[n];
        
        for(int i = 0; i < n; i++){
            cin>>v;
            arr[i] = v;
        }
        
        for(int i = 0; i < n; i++){
            for(int j = i+1; j < n; j++){
                c = arr[i]*arr[j];
                s = 0;
                while(c != 0){
                    s += (c%10);
                    c /= 10;
                }
                if(ans < s){
                    ans = s;
                }
            }
        }
        
        cout<<ans<<endl;
    }
    return 0;
}
