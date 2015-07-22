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

vector<long long> get_prime_list(vector<long long> &prime){
		for (long long i=2;i<prime.size();i++){
				if (!prime[i]){
						for (long long j=i;j<prime.size();j=j+i){
								prime[j]=i;
						}
				}
		}
		return prime;
}

long long prime_factor(vector<long long> &prime,long long n,long long k){
		long long count;
		set<long long> factors;
		while(n>1){
				factors.insert(prime[n]);
				n=(long long)n/prime[n];
		}
		return (long long)factors.size();
}

int main() {
		long long mod=2000007;
//Should intialize the vector with 0
		
		long long N=20;
		long long k=2;
		//scanf("%lld %lld",&N,&k);
		bool point;
		vector<long long> prime_list(mod,0);
		prime_list[0]=0;
		prime_list[1]=0;
		long long window=0;
		long long start=0;
		get_prime_list(prime_list);
		for(long long i=0;i<=N;i++){
				bool window=true;
				for (int w=0;w<k;w++){
						if(prime_factor(prime_list,i+w,k)!=k)
								window=false;
				}
				if (window)
						cout<<i<<endl;
		}
		
		/*for (long long i=0;i<=N+k-1;i++){
				if(i==20)
						point=!point;
				//cout<<num_of_prime_factor(prime_list,i,k)<<endl;
				if(prime_factor(prime_list,i,k)==k){
						window++;
						//cout<<start<<window<<endl;
						if (window==k){
								cout<<start<<endl;
								start=i;
								window=1;
						}
						else if(window==1)
								start=i;
				}
				else
						window=0;
		}*/
		return 0;
}
