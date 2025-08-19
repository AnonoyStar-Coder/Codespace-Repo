#include <stdio.h>

int BinarySearch(int arr[], int left, int right, int key) {

    while (left <= right) {
        
        int mid = left + (right - left) / 2;

        if (arr[mid] == key) {
            return mid;
        }
        if (arr[mid] < key) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}

int main() {
    int arr[] = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key;

    printf("\nEnter the key to be found 'SHOULD BE A MULTIPLE OF 2' : ");
    scanf("%d", &key);

    int result = BinarySearch(arr, 0, n - 1, key);

    if (result != -1) {
        printf("\nElement %d found at index %d\n", key, result);
    } else {
        printf("\nElement %d not found in the array\n", key);
    }
    printf("\n");

    return 0;
}
