#include <stdio.h>

int main() 
{
    int n;
    printf("Enter the number of subjects: ");
    scanf("%d", &n);

    int total= 0;
    for (int i = 1; i <= n; i++)
    {
        int m;
        printf("Enter marks for subject %d: ", i);
        scanf("%d", &m);
        total += m;
    }

    float avg = (float)total / n;

    printf("Average marks: %.2f\n", avg);

    return 0;
}