// Collin Pearce 59% TLE
#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long
#define ll long long
#define min(a, b) a < b?a:b
#define max(a, b) a > b?a:b
#define MOD 1000000007

long getCombinations(vector<vector<long>> &ele, int N, long cost, int depth){
    if (depth == N) return cost;
    long best = cost;
    for(auto a : ele[depth]){
        long newCost = cost - a + ele[depth][0];
        if (newCost < 0) break;
        best = min(best, getCombinations(ele, N, newCost, depth + 1));
    }
    return best;
}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int tc;
    cin >> tc;
    while(tc--){
        long B, N, val, cost = 0;
        cin >> B >> N;
        vector<vector<long>> ele(10);
        vector<int> eleCount(N);
        for(int i = 0; i < N; i++){
            cin >> eleCount[i];
        }
        for(int i = 0; i < N; i++){
            for(int j = 0; j < eleCount[i]; j++){
                cin >> val;
                ele[i].push_back(val);
                
            }
            sort(ele[i].begin(), ele[i].end());
            cost += ele[i][0];
        }

        if (cost > B){
            cout << 0 << endl;
            continue;
        }
        long ans = getCombinations(ele, N, B - cost, 0);
        cout << B - ans << endl;
    }
}

// generate all possible arrangements using recurrance, 
// then return largest under maximum