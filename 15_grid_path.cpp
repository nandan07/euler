#include<iostream>
#include<cstdio>
using namespace std;

int main() {
		int max=10;
		int mod=1000;
		int comb[max][max];
		comb[0][0]=1;
		for (int i=1;i<max;i++){
				comb[i][0]=1;
				//cout<<"a"<<i<<"0"<<endl;
				for (int j=1;j<max;j++){
						comb[i][j]=(comb[i-1][j-1]+comb[i-1][j])%mod;
						//cout<<comb[i][j]<<endl;
						//cout<<"a"<<i<<j<<"= "<<"a"<<i-1<<j-1<<" + a"<<i-1<<j<<endl;
				}
		}
		for (int r=1;r<max;r++){
				for (int c=1;c<max;c++)
						printf("%3d ",comb[r][c]);
				printf("\n");
		}
//		int n;
//		scanf("%d",&n);
//		while(n--){
//				int N,M;
//				scanf("%d%d",&N,&M);
//				printf("%d\n",comb[N+M][N]);
//		}
		return 0;
}


