#include <bits/stdc++.h>
using namespace std;

void Merger(vector<int> &v, int l, int mid, int r){
	vector<int> a;
	vector<int> b;
	for(int i = l ; i <= mid ; ++i)
		a.push_back(v[i]);
	for(int i = mid+1 ; i <= r ; ++i)
		b.push_back(v[i]);

	int i = 0, j = 0, k = l;
	while(i < a.size() and j <b.size()){
		if(a[i] <= b[j])
			v[k] = a[i++];
		else 
			v[k] = b[j++];
		k++;
	}

	while(i < a.size())
		v[k++] = a[i++];
	while(j < b.size())
		v[k++] = b[j++];

}

void MergeSort(vector<int>&v, int l,int r){
	if(r > l){
		int mid = l + (r-l)/2;
		MergeSort(v,l,mid);
		MergeSort(v,mid+1,r);
		Merger(v,l,mid,r);
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
	MergeSort(b,0,n-1);

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