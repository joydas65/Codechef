#include <bits/stdc++.h>
using namespace std;

static char buf[1 << 25];
int bufpos, buflen;

inline int gc() {
    if (bufpos == buflen) {
        buflen = (int)fread(buf, 1, sizeof(buf), stdin);
        bufpos = 0;
        if (buflen == 0) return -1;
    }
    return buf[bufpos++];
}

inline long long readLL() {
    int c = gc();
    while (c != '-' && (c < '0' || c > '9')) c = gc();
    long long sign = 1;
    if (c == '-') { sign = -1; c = gc(); }
    long long x = 0;
    while (c >= '0' && c <= '9') { x = x * 10 + (c - '0'); c = gc(); }
    return x * sign;
}

int main() {
    int t = (int)readLL();
    string out;
    out.reserve(1 << 24);
    vector<long long> a;
    a.reserve(200000);
    char tmp[24];
    while (t--) {
        int n = (int)readLL();
        long long p = readLL();
        long long q = readLL();
        a.resize(n);
        for (int i = 0; i < n; i++) a[i] = readLL();
        sort(a.begin(), a.end());
        long long ones = p, twos = q;
        long long cnt = 0;
        for (int i = 0; i < n; i++) {
            long long v = a[i];
            long long h = v >> 1;
            long long y = twos < h ? twos : h;
            long long x = v - 2 * y;
            if (x <= ones) { ones -= x; twos -= y; cnt++; }
        }
        int len = 0;
        if (cnt == 0) tmp[len++] = '0';
        else { long long c = cnt; char rev[24]; int rl = 0; while (c) { rev[rl++] = char('0' + c % 10); c /= 10; } while (rl) tmp[len++] = rev[--rl]; }
        tmp[len++] = '\n';
        out.append(tmp, len);
    }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
