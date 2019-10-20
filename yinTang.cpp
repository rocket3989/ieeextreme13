// Iskandar Sobirov 57% WA

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define unsigned long ull;
#define timesaver  ios_base::sync_with_stdio(false); cin.tie(0)
#define min(a,b) a < b ? a:b;
#define max(a,b) a > b ? a:b;
#define mod 1e9 + 7;

 
int main()
{
    timesaver; 
    string temp;

    int n;
    cin >> n;
    if(n % 2 == 0)
    {
      for(int i = 0; i <  n; i++)
        {
          if(i == n / 10 ) temp+='y';
          else temp+='Y';
        }
    }
    else 
    {
        for(int i = 0; i < n; i++)
          {
            if(i  != n / 2) temp+='Y';
            else temp+='y';
          }
    }

      cout << temp << "\n";




    return 0;
}
