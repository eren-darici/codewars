#include <string>
#include <iostream>

using namespace std;

int getCount(const string& inputStr)
{
    int num_vowels = 0;
    int lenWord = inputStr.length();
    
    for(int i = 0; i < lenWord; i++)
    {
        if (inputStr[i] =='a' || inputStr[i] =='e' || inputStr[i] =='i' || inputStr[i] =='o' || inputStr[i] =='u')
        {
            num_vowels++;
        }
    }

    
    return num_vowels;
}