#include <stdio.h>

int main(){

    // Variables Declaration
    char string[100];
    char character, replace;
    int i;

    printf("Enter the String: ");
    gets(string);

    printf("Enter the character to Delete: ");
    scanf("%c", &character);

    printf("Enter the character to replace: ");
    scanf(" %c", &replace);


    for (int i = 0; i < 100; i++)
    {
        if (character == string[i])
        {
            string[i] = replace;
        }
    }
    

    printf("String: %s", string);
    


    return 0;
}