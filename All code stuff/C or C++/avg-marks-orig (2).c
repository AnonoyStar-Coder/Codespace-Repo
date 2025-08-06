#include <stdio.h>

int main() {
    int numSubjects;
    printf("Enter the number of subjects: ");
    scanf("%d", &numSubjects);

    int totalMarks = 0;
    for (int i = 1; i <= numSubjects; i++) {
        int marks;
        printf("Enter marks for subject %d: ", i);
        scanf("%d", &marks);
        totalMarks += marks;
    }

    float average = (float)totalMarks / numSubjects;

    printf("Average marks: %.2f\n", average);

    return 0;
}
