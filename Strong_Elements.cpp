#include <iostream>
using namespace std;

int computeGCD(int a, int b) {
    return b == 0 ? a : computeGCD(b, a % b);
}

int main() {
	int t,n,ans;
	cin >> t;
	while (t-- > 0) {
	    cin >> n;
	    int arr[n];
	    for (int i = 0; i < n; i++) {
	        cin >> arr[i];
	    }
	    
	    int forward[n], backward[n];
	    
	    forward[0] = arr[0];
	    backward[n-1] = arr[n-1];
	    
	    for (int i = 1; i < n; i++) {
	        forward[i] = computeGCD(forward[i-1], arr[i]);
	    }
	    
	    for (int i = n - 2; i >= 0; i--) {
	        backward[i] = computeGCD(backward[i+1], arr[i]);
	    }
	    
	    ans = 0;
	    
	    for (int i = 0; i < n; i++) {
	        if (i == 0 && backward[i + 1] > 1) {
	            ans++;
	        } else if (i == n - 1 && forward[n - 2] > 1) {
	            ans++;
	        } else if (computeGCD(forward[i-1],backward[i+1]) > 1) {
	            ans++;
	        }
	    }
	    
	    cout << ans << "\n";
	}
	return 0;
}
