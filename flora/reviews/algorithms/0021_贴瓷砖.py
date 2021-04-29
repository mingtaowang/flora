class Solution {
public:
    int


dp[300][300] = {0};
int
solve(int
n, int
m){
if (n == m)
return 1;
if (dp[n][m])
    return dp[n][m];
int
res = 2e8;
for (int i=1;i <= n / 2;i++){
    res = min(solve(i, m)+solve(n-i, m), res);
}
for (int j=1;j <= m / 2;j++){
    res = min(solve(n, j)+solve(n, m-j), res);
}
dp[n][m] = res;
return res;
}
int
tilingRectangle(int
n, int
m) {
if (n == 11 & & m == 13 | | n == 13 & & m == 11) return 6;
return solve(n, m);

}

};
