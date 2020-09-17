#include <bits/stdc++.h>
using namespace std;

int partition(vector<int>&v, int l,int r){
	int ran_num = l + rand()%(r-l);
	swap(v[ran_num],v[r]);
	int val = v[r];
	int cur = l-1;
	for(int i = l ; i<= r ; ++i){
		if(v[i] <= val)
			swap(v[i],v[++cur]);
	}
	return cur;

}

void QuickSort(vector<int>&v, int l,int r){
	if(l<r){
		int pos =  partition(v,l,r);
		QuickSort(v,l,pos-1);
		QuickSort(v,pos+1,r);
	}

}



bool fun(){
	int n =  5 + rand()%1000;
	vector<int> a;
	vector<int> b;
	for(int i = 0 ; i < n ; ++i){
		int x = rand()%100000;
		a.push_back(x);
		b.push_back(x);
	}
	sort(a.begin(), a.end());
	QuickSort(b,0,n-1);

	for(int i = 0 ; i < n ; ++i){
		if(a[i] != b[i]){
			cout<<i<<" ----------"<<endl;
			for(int j = 0 ; j < n ; ++j  ){
				cout<<a[j]<<" "<<b[j]<<endl;
			}
			return true;
			break;
		}
	}

	return false;
}

int main(){
    int t = 10000;
	while(t--){
		if(fun()){
			cout<<10000 - t<<endl;
			break;
		}
	}
	if(t == -1){
		cout<<"passed";
	}

    return 0;
    }//main