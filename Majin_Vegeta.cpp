#include <bits/stdc++.h>
using namespace std;

const int MAXVAL = 1e6 + 1;

int distinct_prime_factor_count[MAXVAL];
long long prefix_omega_sum[MAXVAL];

void build_omega_sieve() {
    // For each prime p, increment count for all its multiples
    for (int p = 2; p < MAXVAL; p++) {
        if (distinct_prime_factor_count[p] == 0) {   // p is prime
            for (int multiple = p; multiple < MAXVAL; multiple += p) {
                distinct_prime_factor_count[multiple]++;
            }
        }
    }
}

void build_prefix_sum() {
    prefix_omega_sum[0] = 0;
    for (int i = 1; i < MAXVAL; i++) {
        prefix_omega_sum[i] = prefix_omega_sum[i - 1] + distinct_prime_factor_count[i];
    }
}

long long energy_from_n_to_m(int n, int m) {
    // Sum omega(k) for k = n to m-1  (each step k→k+1 costs omega(k))
    return prefix_omega_sum[m - 1] - prefix_omega_sum[n - 1];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    build_omega_sieve();
    build_prefix_sum();

    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        cout << energy_from_n_to_m(n, m) << "\n";
    }
    return 0;
}
