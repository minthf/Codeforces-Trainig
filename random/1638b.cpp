#include <iostream>
using namespace std;

int main(){
	int t, n, a, odd=0, even=0;
	cin >> t;
	bool er = false;
	while(t--){
		cin >> n;
		odd = 0;
		even = 0;
		er = false;
		while(n--){
			cin >> a;
			if (a % 2 == 0){
				if (even != 0){
					
					if (a < even){
						er = true;
					} 
				}
				even = a;
			}
			else{
				if (odd != 0){
					if (a < odd){
						er = true;
					} 
				}
				odd = a;
			}
		}
		if (er) cout << "NO" << endl;
		else cout << "YES" << endl;
	}

}