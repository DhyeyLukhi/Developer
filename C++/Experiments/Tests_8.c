#include <stdio.h>

int main() {
    char str[100];
    char ch;
    int i, found = 0;

    printf("Enter a string: ");
    gets(str);

    printf("Enter a character to find: ");
    scanf("%c", &ch);

    for(i = 0; str[i] != '\0'; ++i) {

        if(ch == str[i]) {
            found = 1;
            break;
            
        }
        
    }

    // 

   

    return 0;
}
