// Collin Pearce 85%
// Solution found after competition

#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ull unsigned long long
#define timesaver  ios_base::sync_with_stdio(false); cin.tie(0)
#define min(a,b) a < b ? a:b;
#define max(a,b) a > b ? a:b;
#define mod 1e9 + 7;

 
int main()
{
    timesaver; 

    int N, len;
    string first;
    cin >> N; 
    vector<bitset<22>> inputs(N);  
    vector<ll> score(N, 0);

    cin >> first;
    len = first.size();

    bitset<22>firstSet(first);
    inputs[0] = firstSet;
    for(int i = 1; i < N; i++){
        cin >> inputs[i];
    }
    
    for (int i = 0; i < 1 << len; i++){
        int best = -1;
        int bestFound = -1;
        bitset<22> curr(i);
        for(int i = 0; i < N; i++){
            int comp = (curr ^ inputs[i]).count();
            if (comp == best){
                bestFound = -1;
            }
            if (comp > best){
                best = comp;
                bestFound = i;
            }
        }
        if (bestFound != -1)
            score[bestFound] += 1;
    }
    int worst = 0;
    for(int i = 1; i < N; i++)
        if (score[i] < score[worst])
            worst = i;

    cout << score[worst] << endl;
}
