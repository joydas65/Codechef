// Question Link https://www.codechef.com/problems/ANKTRAIN

#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    
    unordered_map<int, string> umap;
    
    int i = 7;
    
    while(i <= 500){
        umap[i] = to_string(i+1) + "SU";
        umap[i+1] = to_string(i) + "SL";
        
        i += 8;
    }
    
    i = 1;
    
    while(i <= 500){
        for(int j = i; j <= i+2; j++){
            if(j == i){
                umap[j] = to_string(j+3) + "LB";
                umap[j+3] = to_string(j) + "LB";
            }else if(j == i+1){
                umap[j] = to_string(j+3) + "MB";
                umap[j+3] = to_string(j) + "MB";
            }else{
                umap[j+3] = to_string(j) + "UB";
                umap[j] = to_string(j+3) + "UB";
            }
        }
        i += 8;
    }
    
    while(t-- > 0){
        int n;
        
        cin>>n;
        
        cout<<umap[n]<<endl;
        
        //cout<<endl;
    }
    return 0;
}
