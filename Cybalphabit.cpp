#include<bits/stdc++.h>
#define ll long long int
using namespace std;

ll arr[26]; 
int main(){
    int t;
    cin>>t;
    arr[0] = 1;
    for(int i = 1; i < 26; i++){
        arr[i] =  arr[i-1] * 2;
    }
    while(t-- > 0){
        vector<char> ans;
        int n,k;
        cin>>n>>k;
        for(int i = 0; i < n; i++){
            for(int j = 25; j >= 0; j--){
                if(k-arr[j] >= n-i-1){
                    ans.push_back(char('a'+j));
                    k -= arr[j];
                    break;
                }
            }
        }
        
        if(k > 0 || ans.size() < n){
            cout<<"-1";
        }else{
            for(char a : ans){
                cout << a;
            }
        }
        
        cout<<endl;
    }
    return 0;
}
