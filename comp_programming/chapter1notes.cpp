#include <bits/stdc++.h>
// g++ -std=c++11 -O2 -Wall chapter1notes.cpp -o chap1

/* Another way of shortening code is to use macros, a macro means that certain strings in the code
 * will be changed before the compilation.
 */

#define F first
#define S second
#define PB push_back
#define MP make_pair

// macros can also have parameters which makes it possible to shorten loops
#define REP(i, a, b) for (int i = a; i <= b; i++)

void shortening_code(){
  typedef long long ll;
  
  /* using typedef, we can abreviate long long to ll
   * instead of long long a = _______
   * we can use ll a = _______
   *
   * this could also apply to more complicated datatypes like vector<int>
   * instead of vector<int> we could use typedef vector<int> vi
   *
   */

  ll a = 12345;
  ll b = 67890;
  cout << a * b << endl;
  
  // Using macros
  /* v.push_back(make_pair(y1, x1));
   * v.push_back(make_pair(y2, x2));
   * int d = v[i].first+v[i].second;
   * 
   * Can be shortened to
   */
  v.PB(MP(y1, x1));
  v.PB(MP(y2, x2));
  int d = v[i].F+v[i].S;

  // Using macro loop
  /* for (int i = 1; i <= n; i++){
   *    search(i);
   * }
   * Can be shortened to
   */
  REP(i,1,n){
    search(i);
  }
  // left off on bottom of page 19
}



