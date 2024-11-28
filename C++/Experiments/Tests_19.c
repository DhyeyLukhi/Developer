#include <stdio.h>

int fact(int n){
    if (n == 0 || n == 1)
    {
        return 1;
    }
    else{
        
        return n * fact(n-1);
    }
}

int main(){

    int n, val;

    printf("Enter the value: ");
    scanf("%d", &n);

    val = fact(n);

    printf("Val is : %d", val);

    // struct student
    // {
    //     int val;
    //     float anyt;
    //     char str[10];
    //     char yo;
    // };

    // union student2
    // {
    //     int new;
    //     float what;
    //     char bar[10];
    //     char bhar;
    // };
    
    

    // int val1 = 2.5, val2, val3, val4;
    // float ans, ans2, ans3; 
    // ans = 50%2/3+2;
    // ans2 = 21/val1+3;
    // ans3= (1 > 2) || (2 < 3) && (5 < 1);
 
    // printf("The answer is 50 % 2 / 3 + 2: %f\n", ans);
    // printf("The answer is 21 / 2.5 + 3: %f\n", ans2);
    // printf("The answer is (1 > 2) || (2 < 3) && (5 < 1) : %f\n", ans3);

    


    return 0;
}