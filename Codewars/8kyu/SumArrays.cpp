#include <vector>
#include <iostream>
#include <numeric>
using namespace std;

int sum(vector<int> nums) {
  // your code here
    int total = 0;
    

    return accumulate(nums.begin(), nums.end(), total); 
}
