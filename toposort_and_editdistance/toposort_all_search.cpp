#include<bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i,n) for(ll i=0; i<(n); i++)
#define all(x) (x).begin(), (x).end()
#define lb(c, x) distance((c).begin(), lower_bound(all(c), (x)))

vector<vector<ll>> G;
ll n, m, k;
set<vector<ll>> st;

void Output(){
   if(st.size()==0){
       cout << "Not exist" << "\n";
       exit(0);
   }
   for(auto array : st){
      for(auto e : array) cout << e+1 << " ";
      cout << "\n";
   }
   exit(0);
}

void dfs(queue<ll> que, vector<ll> In, vector<ll> ans){
   if(que.empty()){
      if(ans.size() == n) st.insert(ans);
      if(st.size()>=k) Output();
      return;
   }
   ll que_size = que.size();
   while(que_size--){
      ll v = que.front();
      ans.push_back(v);
      que.pop();
      queue<ll> new_que = que;
      vector<ll> new_In = In;
      for(auto nv : G[v]){
         new_In[nv]--;
         if(new_In[nv] == 0) new_que.push(nv);
      }
      dfs(new_que, new_In, ans);
      que.push(v);
      ans.pop_back();
   }
}

int main() {
   cin >> n >> m >> k;
   G.resize(n);
   vector<ll> In(n);
   queue<ll> que; // 入次数が0の頂点の集合
   vector<ll> ans; // トポロジカルソートした順を記録する

   for(ll i=0; i<m; i++){
      ll a, b; cin >> a >> b;
      a--; b--;
      G[a].push_back(b);
      In[b]++;
   }
   for(ll i=0; i<n; i++){
      if(In[i] == 0) que.push(i);
   }
   dfs(que, In, ans);
   Output();
   
   return 0;
}
