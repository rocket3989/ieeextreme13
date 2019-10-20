// Collin Pearce
// cpp implementation of lexical.py
#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long
#define ll long long
#define min(a, b) a < b?a:b
#define max(a, b) a > b?a:b
#define MOD 1000000007

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ull A, B, N;

    cin >> N >> A >> B;

    if(A > N / 2 && B < N)
        cout << "NO\n";
    else{
        cout << "YES\n";
        ull bCount = N / B;

        N %= B;
        string bChar = to_string(B);
        string aChar = to_string(A);
        if (N == 0){
            string output = "";
            while(bCount--) output += bChar + " ";
            cout << output;
        }
        
        else if (N < A){
            ull x = (ull)ceil((A - N) / (double)(B - A));
            bCount -= x;
            N += B * x;
            ull aCount = (N / A) - 1;
            N = N % A;
            string output = "";
            while(aCount--) output += aChar + " ";
            output += to_string(A + N) + " ";
            while(bCount--) output += bChar + " ";
            cout << output;
        }
        
        else{
            cout << N << " ";
            string output = "";
            while(bCount--) output += bChar + " ";
            cout << output;
        }
        
        cout << endl;
    }
}