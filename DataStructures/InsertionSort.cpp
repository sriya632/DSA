#include <iostream>
#include <vector>
using namespace std;

vector<int> insertion_sort(vector<int> unsorted_list) {
    int n = unsorted_list.size();

    for (int i = 1; i < n; i++) {
        int j = i;
        while (j > 0 && unsorted_list[j] < unsorted_list[j - 1]) {
            // Swap using a temporary variable
            int temp = unsorted_list[j];
            unsorted_list[j] = unsorted_list[j - 1];
            unsorted_list[j - 1] = temp;
            j--;
        }
    }

    return unsorted_list;
}

int main() {
    vector<int> input = {5, 2, 4, 6, 1, 3};

    vector<int> sorted = insertion_sort(input);

    cout << "Sorted list: ";
    for (int num : sorted) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
