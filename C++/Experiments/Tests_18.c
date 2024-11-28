#include <stdio.h>

int main()
{
    int var, *ptr;
    var = 2.3;
    int *ptr2 = &var;

    printf("The value is %d", ptr2);

    return 0;
}