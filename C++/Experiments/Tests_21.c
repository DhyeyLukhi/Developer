#include <stdio.h>

int main(){
    int num, num2 = 0, ans = 0, temp;

    printf("Enter the number: ");
    scanf("%d", &num);

    temp = num;


   while(num > 0)
    {
        num2 = num % 10;
        ans = ans * 10 + num2;
        num = num / 10;
    }


    if (ans == temp)
    {
        printf("Entered number is Palindrome number.\n");
    }
    else
    {
        printf("Entered number is no Palindrome number.\n");
    }

    
    
    
    
    
    
    
    return 0;
}