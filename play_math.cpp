#include <iostream>
using namespace std;

int main() {
  
	float num1, num2, num3, num4, num5, sum_num;
  
	cout << "Enter 5 numbers: " << endl;
	cin >> num1 >> num2 >> num3 >> num4 >> num5;
	sum_num = num1 + num2 + num3 + num4 + num5;
	cout << "the average to this 5 numbers is: " << sum_num / 5 << endl;
	cout << "the sum of the first 3 numbers div by the sum last 2 numbers is: " <<(num1 + num2 + num3) / (num4 + num5) << endl;
	cout << "the avg of the first 3 numbers div by the avg of the last 2 numbers is: " <<((num1 + num2 + num3) / 3) / ((num4 + num5) / 2) << endl;
  
 	return 0;
}
