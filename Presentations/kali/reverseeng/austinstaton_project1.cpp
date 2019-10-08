/******************************************************************************
 *  This is first project in CSCE350 with Dr. Jason O'Kane.
 *
 *  The assignment requires one to:
 *    1. Read four integers (assume ints are >= 0) from standard input.
 *    2. Compute thier sum, if at least one number is greater than 0.
 *    3. Print this sum.
 *    4. Contine steps 1-3 until four zeros (0 0 0 0) are entered.
 *
 *  This is it. Do nothing more; do nothing less.
 *
 *  This implementation was written by:
 *    Austin Staton | 08-28-2019
 *
 *  Referenes from http://cplusplus.com were used to complete this assignment.
 */

#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::vector;

int main(int argc, char *argv[]) {
  
  int sum = 0;
  bool done = false; 
  vector<int> numbers;

  // We want to continue this process, until the user prompts otherwise.
  while(!done) {
    // 1. Read in four integers from std input.
    bool isPositive = false; // This will determine if a sum is needed.

    for (int i = 0; i < 4; i++) {
      int value;
      cin >> value;
      numbers.push_back(value);
      
      if (value > 0) {
	isPositive = true;
      }
    }

    // 2. Sum the four numbers, if at least one number was positive.
    if (!isPositive) {
      done = true;
      break;
    } else {
      for(int i = 0; i < 4; i++) {
         sum += numbers.at(i); 
      }
    }

    // 3. Print this sum.
    cout << sum << endl;

    // 4. Return and repeat.
    numbers.clear(); // This Resets the vector.
    sum = 0;
  }

  return 0;
}
