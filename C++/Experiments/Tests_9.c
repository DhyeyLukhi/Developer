#include <stdio.h>

int main(){

    // Variables Declaration
    char string[100];
    char character;
    int i;

    printf("Enter the String: ");
    gets(string);

    printf("Enter the character: ");
    scanf("%c", &character);

    for (int i = 0; i < 100; i++)
    {
        if (character == string[i])
        {
            printf("Entered Character founded at position no. %d\n", i+1);
        }
    }
    


    return 0;
}