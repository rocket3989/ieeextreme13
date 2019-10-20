// Iskandar Sobirov 22% WA

#include <bits/stdc++.h>
using namespace std;

#define long long ll;
#define unsigned long ull;
#define timesaver  ios_base::sync_with_stdio(false); cin.tie(0)
#define min(a,b) a < b ? a:b;
#define max(a,b) a > b ? a:b;
#define mx 1e5 + 7;

bool isUnique(string s)
{
    bool check = false; 
    set<char> val;
    for(int i = 0; i < s.size(); i++)
      val.insert(s[i]);

    return s.size() == val.size() ? true:false;
}

bool isInOrder(string s)
{
     string temp = s;
     reverse(s.begin(),s.end());
     if(s == temp) return true;


    return false;
}
 int findMinimumSwaps(string arr) 
{ 
    if(arr.size()<= 1) return 0;
    if(isUnique(arr)) return 0;
    //if(isInOrder(arr)) return 0;

    set<char>val;
    int size = arr.size();
        

       int minimumSwaps = 0; 
    set<char>val2;
    char prev = 'E';
      for(int i = 0 ; i < size; i++)
      {

          if(val2.find(arr[i])!= val2.end() && arr[i]!= arr[i-1]){
         
                if(arr[i]!=prev)
                minimumSwaps++;

                prev = arr[i];
          }
        
          else {
            val2.insert(arr[i]);
             
          }
      }

    if(arr[0] == arr[size - 1]) minimumSwaps--;

    return minimumSwaps / 2;
} 
int main()
{
    timesaver; 
    int cases;
    cin >> cases; 

    for(int i = 0; i < cases; i++)
    {
         string val;
        cin >> val;

        cout << findMinimumSwaps(val) << "\n";

    }
     

    





    return 0;
}


