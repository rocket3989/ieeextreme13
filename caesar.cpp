// Collin Pearce 17%
#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long
#define ll long long
#define min(a, b) a < b?a:b
#define max(a, b) a > b?a:b
#define MOD 1000000007

unordered_map<string, bool> dp = {{"A", true},{"B", true},{"C", true},{"D", true},{"E", true},{"F", true},{"G", true},{"H", true},{"I", true},{"J", true},{"K", true},{"L", true},{"M", true},{"N", true},{"O", true},{"P", true},{"Q", true},{"R", true},{"S", true},{"T", true},{"U", true},{"V", true},{"W", true},{"X", true},{"Y", true},{"Z", true}};

bool isValid(string input){
    if (dp.find(input) != dp.end())
        return dp[input];
    for (int i = 0; i < input.size(); i++){
        if(input[i] >= input[0]){
            string half1 = input.substr(0, i);
            string half2 = input.substr(i,input.size() - i);
            if (half1.compare(half2) <= 0){
                if (isValid(half1)) && isValid(half2)){
                    dp[input] = true;
                    return true;
                }
            }
        }
    }
    dp[input] = false;
    return false;

}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int tc;
    cin >> tc;
    while(tc--){
        string val;
        cin >> val;
        if (isValid(val)) cout << 1;
        else cout << 0;
    }
    cout << endl;

}

// cpp implementation of caesar.py