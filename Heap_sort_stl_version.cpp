#include<bits/stdc++.h>
using namespace std;

class Pqueue
{
	int n;
	int cur;
	vector<int> arr;
public:
	Pqueue(){

	}

	Pqueue(int n){
		this-> n = n;
		this-> cur = -1;
		arr.resize(n);
	}

	Pqueue(vector<int> &v):Pqueue(v.size()){
		for(auto i : v)
			push(i);
	}



	void push(int x){
		arr[++cur] = x;
		int temp = cur;
		while(arr[(temp-(temp%2==0) )/2] < arr[temp]){
			swap(arr[(temp-(temp%2==0) )/2],arr[temp]);
			temp = (temp-(temp%2==0) )/2;
		}
	}

	int top(){
		return arr[0];
	}

	int pop(){
		swap(arr[0],arr[cur--]);
		int temp = 0;

		while(temp <= cur){
			int l = 2*temp + 1;
			int r = 2*temp + 2;
			if( r > cur ){
				if(l <= cur){
					if(arr[l] > arr[temp]){
						swap(arr[l],arr[temp]);
					}
				}
				break;
			}
			if(arr[l] > arr[r]){
				if(arr[l] > arr[temp]){
					swap(arr[l],arr[temp]);
					temp = l;
				}
				else
					break;
			}
			else{
				if(arr[r] > arr[temp]){
					swap(arr[r],arr[temp]);
					temp = r;
				}
				else break;

			}
		}


		return arr[cur+1];
	}

	bool empty(){
		return (cur == -1);
	}

	void Heap_sort(vector<int> &v){
		Pqueue* pqt = new Pqueue(v);
		int temp = pqt->n-1;
		while(!pqt->empty()){
			v[temp--] = pqt->pop(); 
		}
	}
};

bool fun(){
	int n =  5 + rand()%95;
	vector<int> a;
	vector<int> b;
	for(int i = 0 ; i < n ; ++i){
		int x = rand()%1000;
		a.push_back(x);
		b.push_back(x);
	}
	sort(a.begin(), a.end());
	Pqueue pq;
	pq.Heap_sort(b);

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


}

