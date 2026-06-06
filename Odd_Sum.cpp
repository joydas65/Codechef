#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;

    string output;
    output.reserve(t * 12);          // rough size hint
    char buffer[32];

    while (t--) {
        long long n;
        scanf("%lld", &n);
        long long answer = 1 + (n - 1) * (n - 2);   // fits in 64-bit
        int len = sprintf(buffer, "%lld\n", answer);
        output.append(buffer, len);
    }

    fwrite(output.data(), 1, output.size(), stdout);
    return 0;
}
