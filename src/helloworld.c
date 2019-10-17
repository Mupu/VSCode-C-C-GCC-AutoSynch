#include <stdio.h>

int main(void)
{
    #ifdef _DEBUG
    printf("DEBUG: Hello, World from VS Code!\n");
    #else
    printf("Hello, World from VS Code!\n");
    #endif
    
    printf("Press ENTER key to continue . . .");
    getchar();
    return 0;
}