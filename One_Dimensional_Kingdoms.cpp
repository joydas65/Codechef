#include <bits/stdc++.h>
using namespace std;

static char buf[1 << 25];
static int bufpos = 0, buflen = 0;

static inline int gc() {
    if (bufpos == buflen) {
        buflen = (int)fread(buf, 1, sizeof(buf), stdin);
        bufpos = 0;
        if (buflen == 0) return -1;
    }
    return buf[bufpos++];
}

static inline long long readInt() {
    int c = gc();
    while (c != '-' && (c < '0' || c > '9')) c = gc();
    int sign = 1;
    if (c == '-') { sign = -1; c = gc(); }
    long long x = 0;
    while (c >= '0' && c <= '9') { x = x * 10 + (c - '0'); c = gc(); }
    return x * sign;
}

int main() {
    int t = (int)readInt();
    string out;
    out.reserve(1 << 20);
    while (t--) {
        int n = (int)readInt();
        vector<pair<int,int>> iv(n);
        for (int i = 0; i < n; i++) {
            int a = (int)readInt();
            int b = (int)readInt();
            iv[i] = {b, a};
        }
        sort(iv.begin(), iv.end());
        long long last = LLONG_MIN;
        int cnt = 0;
        bool first = true;
        for (auto &pr : iv) {
            int b = pr.first, a = pr.second;
            if (first || a > last) {
                cnt++;
                last = b;
                first = false;
            }
        }
        out += to_string(cnt);
        out += '\n';
    }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
