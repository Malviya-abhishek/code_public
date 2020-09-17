#include <bits/stdc++.h>
using namespace std;

class Trie {
    private:
    bool isEnd;
    vector<Trie*> search_item;
    vector<string> entity;

    void recursive_search(auto i, vector<string> &res){
    	if(i->isEnd)
    		for(auto j : i->entity)
    			res.push_back(j);

    	for(auto k : i->search_item)
    		if(k)
    			recursive_search(k, res);
    }
 
    
public: 
    Trie(){
    	isEnd = false;
    	search_item.resize(CHAR_MAX,NULL);
    }

    void insert(string word,string num){
    	Trie* cur = this;
    	for(char c : word){
    		int x = int(c);
    		if(cur->search_item[x] == NULL)
    			cur->search_item[x] = new Trie();
    		cur = cur->search_item[x];
    	}
    	cur->isEnd = true;
    	cur->entity.push_back(num);

    	swap(word,num);
    	cur = this;
    	for(char c : word){
    		int x = int(c);
    		if(cur->search_item[x] == NULL)
    			cur->search_item[x] = new Trie();
    		cur = cur->search_item[x];
    	}
    	cur->isEnd = true;
    	cur->entity.push_back(num);
    }

    vector<string> search(string prefix) {
    	Trie* cur = this;
    	vector<string> res;
    	res.push_back(prefix);
    	for(char c : prefix){
    		int x = int(c);
    		if(cur->search_item[x] == NULL)
    			return res;
    		cur = cur->search_item[x];
    	}

    	if(cur->isEnd)
    		for(auto i : cur->entity)
    			res.push_back(i);
    	

    	for(auto i : cur->search_item)
    		if(i)
    			recursive_search(i,res);
    	return res;
    }

    void print(vector<string> v){
    	int n = v.size();
    	cout<<v[0]<<"->";
    	if(n == 1)
    		cout<<"No Entry";
    	else
    		for(int i = 1; i < n ; ++i)
    			cout<<v[i]<<" ";
    	cout<<endl;
    }

};


int main(){
  	Trie phone_book;
  	phone_book.insert("apple","789456");
  	phone_book.insert("apple","78945623");

  	phone_book.print(phone_book.search("apple"));
  	phone_book.print(phone_book.search("789456"));
  	phone_book.print(phone_book.search("app"));

  	phone_book.insert("app","789321");

  	phone_book.print(phone_book.search("app"));
  	phone_book.print(phone_book.search("789"));
  	
	return 0;
	}//main