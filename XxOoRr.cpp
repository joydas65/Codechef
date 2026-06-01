#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while (T--) {
        int N, K;
        cin >> N >> K;

        const int BITS = 30;          // since A_i <= 1e9 < 2^30
        vector<long long> set_bit_count(BITS, 0);

        for (int i = 0; i < N; i++) {
            long long a;
            cin >> a;
            for (int p = 0; p < BITS; p++) {
                if (a & (1LL << p)) {
                    set_bit_count[p]++;
                }
            }
        }

        long long total_ops = 0;
        for (int p = 0; p < BITS; p++) {
            // Each operation flips bit p in at most K elements
            total_ops += (set_bit_count[p] + K - 1) / K;   // ceil
        }

        cout << total_ops << "\n";
    }
    return 0;
}
