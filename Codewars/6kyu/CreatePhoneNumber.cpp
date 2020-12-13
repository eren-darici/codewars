#include <string>
using namespace std;


string createPhoneNumber(const int arr [10]){
    //your code here

    string number = "";
    number += "(";

    for (int i = 0; i < 3 ; i++)
    {
        number += to_string(arr[i]);
    }
    number += ") ";

    for (int i = 3; i < 6 ; i++)
    {
        number += to_string(arr[i]);
    }
    number += "-";


    for (int i = 6; i < 9 ; i++)
    {
        number += to_string(arr[i]);
    }

    return number;
  
}