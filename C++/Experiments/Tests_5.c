#include <stdio.h>
int main()
{
    FILE *fp;
    int ch, num;
    fp = fopen("Classified", "r"); // open the file for reading
    if (fp == NULL) // check if the f ile was opened successfully
    {
        printf("Error opening file\n");
        return 1;
    }
    ch = getc(fp); // read a character from the file
    num = getw(fp); // read an integer from the file
    printf("Character: %c\n", ch); // print the character
    printf("Integer: %d\n", num); // print the integer
    fclose(fp); // close the file
    return 0;
}

