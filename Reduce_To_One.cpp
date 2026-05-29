#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;
const int MAXN = 1e6 + 2;

long long factorial_mod[MAXN];

void precompute_factorials() {
    factorial_mod[0] = 1;
    for (int i = 1; i < MAXN; i++) {
        factorial_mod[i] = (factorial_mod[i - 1] * i) % MOD;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    precompute_factorials();

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        // answer = (N+1)! - 1  (mod 1e9+7)
        long long answer = (factorial_mod[N + 1] - 1 + MOD) % MOD;
        cout << answer << "\n";
    }
    return 0;
}
