// Collin Pearce 75% TLE
// cpp implemenation of monokeros.py
#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long
#define ll long long
#define min(a, b) a < b?a:b
#define max(a, b) a > b?a:b
#define MOD 1000000007

struct Node{
    long val;
    Node* left;
    Node* right;
    Node(long _val){
        left = NULL;
        right = NULL;
        val = _val;
    }
};
int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    long val;
    cin >> val;
    Node* root = new Node(val);
    N--;
    cout << 1 << ' ';
    while(N--){
        int depth = 1;
        Node* currNode = root;
        cin >> val;
        while(true){
            depth ++;
            if(val > currNode -> val){
                if(currNode -> right == NULL){
                    currNode -> right = new Node(val);
                    cout << depth << ' ';
                    break;
                }
                currNode = currNode -> right;
            }
            else{
                if(currNode -> left == NULL){
                    currNode -> left = new Node(val);
                    cout << depth << ' ';
                    break;
                }
                currNode = currNode -> left;
            }
        }
    }
    cout << endl;
}