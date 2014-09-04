#include <iostream>

using namespace std;

int main(){
	int nNCelsius;

	cout << "Input temperature in Cels: " << endl;
	cin >> nNCelsius;

	int nNFactor = 212 - 32;
	int nFahrenheit = nNFactor * nNCelsius/100 + 32;

	cout << "Temp in Fahrenh is: " << nFahrenheit << endl;

	return 0;
}
