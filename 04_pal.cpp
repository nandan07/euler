#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;

bool isPal(int N){
		vector<int> pal;
		vector<int> st;
		int t=N;
		while(t){
				st.push_back(t%10);
				t=t/10;
		}
		for (int p=0;p<st.size()/2;p++)
				if (st[p]!=st[st.size()-p-1])
						return false;
		return true;
}
vector<long long> getPal(long long  n){
		vector<long long> pal;
		while(--n)
				if (isPal(n))
						pal.push_back(n);
		return pal;
}

vector<long long> getPal(long long start,long long end){
		vector<long long> pal;
		for (int n=start;n>=end;n--)
				if (isPal(n))
						pal.push_back(n);
		return pal;
}

int main(){
		long long  N;
		scanf("%illd",&N);
		vector<long long> pal=getPal(999999,101101);
		while(N--){
				long long t;
				scanf("%lld",&t);
				bool found=false;
				long long ans=0;
				for (int i=0;i<pal.size();i++){
						if ((not(found))&&(pal[i]<t))
								for (int p=100;p<1000;p++)
										for (int q=p;q<1000;q++)
												if((not(found))&&(p*q==pal[i])){
														ans=pal[i];
														found=true;
														break;
												}
										if (found)
												break;
								if(found)
										break;
						if(found)
										break;
				}
				if(found)
						printf("%lld\n",ans);
		}
		return 0;
}
