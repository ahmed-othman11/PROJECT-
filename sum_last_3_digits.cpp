// Program to read an int and print the sum of last 3 digits.

#include <iostream>
using namespace std;


int main() {

	int num, mod0=0, mod1=0, mod2=0, result;
	cout << "enter the numbers: ";
	cin >> num;


	mod0 = num % 10;
	num = num / 10;
	cout << "mod0 = " << mod0 << endl;

	mod1 = num % 10;
	num = num / 10;
	cout << "mod1 = " << mod1 << endl;

	mod2 = num % 10;
	num = num / 10;
	cout << "mod2 = " << mod2 << endl;

	result = mod0 + mod1 + mod2;

	cout << "the result is: " << result << endl;


 	return 0;
}
