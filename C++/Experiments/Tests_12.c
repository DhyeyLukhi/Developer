#include <stdio.h>

int main(){

    char string[100];
    char delete;
    int i, j;

    printf("Enter the String: ");
    gets(string);
    

    printf("Enter the character to Delete: ");
    scanf("%c", &delete);


    printf("value: %d\n", sizeof(string));


     for (int i = 0; i < 100; i++)
     {
         if (delete == string[i])
         {
             for (int j = i; j < string[j] != '\0'; j++)
             {
                 string[j] = string[j+1];
             }
            
         }
     }
    

     printf("String: %s", string);
    


    return 0;
}
