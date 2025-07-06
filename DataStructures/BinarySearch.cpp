#include <iostream>
#include <vector>
using namespace std;


int binary_search(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;  
        } else if (arr[mid] < target) {
            left = mid + 1; 
        } else {
            right = mid - 1; 
        }
    }

    return -1;  // Target not found
}

int main() {
    int n, target;

    
    cout << "Enter number of elements: ";
    cin >> n;

    vector<int> arr(n);

   
    cout << "Enter " << n << " sorted elements:\n";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    
    cout << "Enter target to search: ";
    cin >> target;

    
    int result = binary_search(arr, target);

    if (result != -1) {
        cout << "Target found at index: " << result << endl;
    } else {
        cout << "Target not found in array." << endl;
    }

    return 0;
}
