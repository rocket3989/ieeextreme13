// Collin Pearce
// cpp convex implementation 
#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long
#define ll long long
#define min(a, b) a < b?a:b
#define max(a, b) a > b?a:b
#define MOD 1000000007


struct point {
    int x, y;
};

struct line {
    point p1, p2;
};

bool colinear(line l1, point p) { 
   if(p.x <= max(l1.p1.x, l1.p2.x) && p.x <= min(l1.p1.x, l1.p2.x) 
      && (p.y <= max(l1.p1.y, l1.p2.y) && p.y <= min(l1.p1.y, l1.p2.y)))
        return true;
   
    return false;
}

int direction(point a, point b, point c) {
    int val = (b.y-a.y)*(c.x-b.x)-(b.x-a.x)*(c.y-b.y);
    if (val == 0)
        return 0;     
    else if(val < 0)
        return 2;    
    return 1;    
}

bool isIntersect(line l1, line l2) {
    int dir1 = direction(l1.p1, l1.p2, l2.p1);
    int dir2 = direction(l1.p1, l1.p2, l2.p2);
    int dir3 = direction(l2.p1, l2.p2, l1.p1);
    int dir4 = direction(l2.p1, l2.p2, l1.p2);
    
    if(dir1 != dir2 && dir3 != dir4)
        return true; 

    if(dir1==0 && colinear(l1, l2.p1)) 
        return true;

    if(dir2==0 && colinear(l1, l2.p2)) 
        return true;

    if(dir3==0 && colinear(l2, l1.p1)) 
        return true;

    if(dir4==0 && colinear(l2, l1.p2)) 
        return true;
            
    return false;
}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, M;
    cin >> N >> M;
    vector<line> poly(N);
    vector<point> points;
    point first, recent;
    cin >> first.x >> first.y;
    recent = first;

    for(int i = 0; i < N - 1; i++){
        poly[i].p1 = recent;
        cin >> recent.x >> recent.y;
        poly[i].p2 = recent;       
    }
    poly[N-1].p1 = recent;
    poly[N-1].p2 = first;
    
    point temp;
    ull insideCount = 0;
    for(int i = 0; i < M; i++){
        cin >> temp.x >> temp.y;
        bool outside = false;
        points.push_back(temp);

        for (auto val : poly){
            if ((temp.y - val.p1.y) * (val.p2.x - val.p1.x) - (temp.x - val.p1.x) * (val.p2.y - val.p1.y) < 0){
                outside = true;
                break;
            }
        }
        if(!outside)
            insideCount++;
    }
    
    // ull outsideCount = points.size() * (points.size() - 1) / 2;
    ull outsideCount = 0;
    for(int i = 0; i < points.size(); i++){
        for(int j = 0; j < points.size(); j++){
            line test;
            test.p1 = points[i], test.p2 = points[j];
            bool failed = false;
            for(auto val : poly){
                if (isIntersect(val, test)){
                    failed = true;
                    break;
                }
            }
            if(!failed){
                // cout << test.p1.x << ' ' << test.p1.y << ' ' << test.p2.x << ' ' << test.p2.y << endl;
                outsideCount++;
            }
        }
    }
    


    cout << (outsideCount/2 )+ (insideCount * (insideCount - 1)) / 2 << endl;


// line l1 = {{0,0}, {5, 5}};
//    line l2 = {{2,-10}, {3, 10}};
        

}