#include <iostream>
#include <vector>
#include <string>


using namespace std;

int main()
{
    #ifdef _DEBUG
    vector<string> msg {"DEBUG:", "Hello", "C++", "World", "from", "VS Code!"};
    #else
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code!"};
    #endif
    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
    system("pause");
    return 0;
}