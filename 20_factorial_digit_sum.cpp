#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;

void mutiply(vector<int> & v, int n){
		int carray=0;
		for (int i=0;i<v.size();i++){
				int t=(v[i]*n)+carray;
				v[i]=t%10;
				carray=t/10;
		}
		while(carray){
				v.push_back(carray%10);
				carray/=10;
		}
}
int main(){
		int n;
		scanf("%d",&n);
		while(n--){
				vector <int> num(1,1);
				int N;
				scanf("%d",&N);
				for (int i=1;i<=N;i++){
						mutiply(num,i);
				}
				int ans=0;
				for(int i=num.size()-1;i>=0;i--)
						ans+=num[i];
				printf("%d\n",ans);
		}
		return 0;
}

