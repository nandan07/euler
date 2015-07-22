#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>
#define tr(container, it) \
for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
using namespace std;

bool ispandigit(long long n){
		set<int> d;
		int r=(int)n%10;
		while(n>0){
				d.insert((int)n%10);
				n=int(n/10);
		}
		for(int i=1;i<=d.size();i++){
				if(d.find(i)!=d.end())
						continue;
				else
						return false;
		}
		return true;

}

void get_prime(vector<int> &v,long long n){
		v[0]=0;
		v[1]=0;
		for(long long i=2;i<n;i++){
				if(v[i]==1){
						for(long long j=i*2;j<n;j+=i){
								if(v[j]){
										if(j%i==0){
												v[j]=0;}
										else
												v[j]=1;
								}
						}
				}
		}
}

int main() {
		long long n;
		scanf("%lld",&n);
		vector<int> v(n+1,1);
		get_prime(v,n);
		set<int> s;
		long long ans=0;
		for(int i=0;i<n;i++)
				if(v[i])
						ans++;
		cout<<ans;
		return 0;
}
