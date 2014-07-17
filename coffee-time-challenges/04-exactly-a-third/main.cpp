#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int numbers[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 'x' };

  sort(numbers, numbers + 10);

  do {

    int a = 0;
    int b = 0;

	if(numbers[5] != 'x') 
	  continue;

    for(int i = 0; i < 5; i++) {
  	  a *= 10;
   	  a += numbers[i];
    }
    
	for(int i = 6; i < 10; i++) {
  	  b *= 10;
   	  b += numbers[i];
    }

    if(a != 0 && b != 0) {
      if(a / b == 3 && a % b == 0) {
        cout << b << " / " << a << endl;
      }
    }

  } while(next_permutation(numbers, numbers + 10));

  return 0;
}
