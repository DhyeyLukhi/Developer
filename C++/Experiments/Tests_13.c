#include<stdio.h>

int main(){

    int i, j, line;

    printf("enter the number of lines");
    scanf("%d", &line);

    for (int i = 0; i < line; i++)
    {
        for (int j = 0; j < line - i; j++)
        {
            printf("%c", i+65);
        }
        printf("\n");
    }

    return 0;
}