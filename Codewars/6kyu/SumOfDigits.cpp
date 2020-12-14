#include <string>
using namespace std;

int digital_root(int n)
{
    string num = to_string(n);

    if (num.compare("0") == 0) {return 0;}

    int x = 0;
    for (int i=0; i<num.length(); i++)
    {
        x = (x + num[i]-'0') % 9;
    }

    return (x == 0) ? 9 : x % 9;

}
