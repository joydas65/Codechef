#include <cstdio>
#include <algorithm>
#include <vector>
#include <array>
using namespace std;

static char buf[1 << 25];
static int bufpos, buflen;

static inline int readChar() {
    if (bufpos == buflen) {
        buflen = (int)fread(buf, 1, sizeof(buf), stdin);
        bufpos = 0;
        if (buflen == 0) return -1;
    }
    return buf[bufpos++];
}

static inline long long readLong() {
    int c = readChar();
    while (c != '-' && (c < '0' || c > '9')) c = readChar();
    int sign = 1;
    if (c == '-') { sign = -1; c = readChar(); }
    long long x = 0;
    while (c >= '0' && c <= '9') {
        x = x * 10 + (c - '0');
        c = readChar();
    }
    return x * sign;
}

int main() {
    int t = (int)readLong();
    while (t--) {
        long long n = readLong();
        readLong();
        vector<array<long long, 3>> v(n);
        for (long long i = 0; i < n; i++) {
            long long s = readLong();
            long long f = readLong();
            long long p = readLong();
            v[i] = {p, f, s};
        }
        sort(v.begin(), v.end());
        long long count = 0, curp = -1, last = -1;
        for (size_t i = 0; i < v.size(); i++) {
            long long p = v[i][0], f = v[i][1], s = v[i][2];
            if (p != curp) { curp = p; last = -1; }
            if (s >= last) { count++; last = f; }
        }
        printf("%lld\n", count);
    }
    return 0;
}
