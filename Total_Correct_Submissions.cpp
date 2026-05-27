#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;
    
    // unordered_map provides faster insertions/lookups than a standard map
    unordered_map<string, long long> submissions;
    
    // There are 3 divisions, each with N problems, so 3 * N inputs total
    for (int i = 0; i < 3 * n; ++i) {
        string code;
        long long count;
        cin >> code >> count;
        submissions[code] += count;
    }
    
    // Extract the total submissions into a vector
    vector<long long> result;
    result.reserve(submissions.size());
    for (const auto& pair : submissions) {
        result.push_back(pair.second);
    }
    
    // Sort the results in non-decreasing order
    sort(result.begin(), result.end());
    
    // Print the results space-separated
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i] << (i == result.size() - 1 ? "" : " ");
    }
    cout << "\n";
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
