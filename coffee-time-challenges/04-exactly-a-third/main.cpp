#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int numbers[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 'x' };

  sort(numbers, numbers + 10);

  do {

    float a = 0;
    float b = 0;
    bool foundX = false;

	if(numbers[5] != 'x') 
	  continue;

    for(int i = 0; i < 10; i++) {

      if(numbers[i] == 'x') {
        foundX = true;
      } else {
        if(!foundX) {
          a *= 10;
          a += numbers[i];
        } else {
          b *= 10;
          b += numbers[i];
        }
      }
    }

    if(a != 0 && b != 0) {
      if(a / b == 3) {
        cout << b << " / " << a << endl;
      }
    }

  } while(next_permutation(numbers, numbers + 10));

  return 0;
}
