// Iskandar Sobirov 16% WA
#include <bits/stdc++.h>
using namespace std;

#define long long ll;
#define unsigned long ull;
#define timesaver  ios_base::sync_with_stdio(false); cin.tie(0)
#define min(a,b) a < b ? a:b;
#define max(a,b) a > b ? a:b;
#define mod 1e9 + 7;

 
int main()
{
    timesaver; 

  int cases;
string res;
  cin >> cases; 
  
 std::bitset<8> bit,hold;  
  while(cases--)
  { 
    cin >> bit;  
    
  
     
      if(bit.count()==0)
      { 
          bit.flip(1);   
          //cout << bit << endl;
      }
      else if(bit.count()==1)
        bit.flip(1);
      else if(bit.count()==2)
        bit.flip(1);
    }
   
  
 cout <<bit.count() << endl;
   


    return 0;
}
