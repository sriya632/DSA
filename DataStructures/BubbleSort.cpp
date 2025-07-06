#include <iostream>
#include <vector>
using namespace std;

vector<int> bubble_sort(vector<int> unsorted_list) {
    int n = unsorted_list.size();

    for (int i = n - 1; i >= 0; i--) {
        bool swapped = false;
        for (int j = 0; j < i; j++) {
            if (unsorted_list[j] > unsorted_list[j + 1]) {
                int temp = unsorted_list[j];
                unsorted_list[j] = unsorted_list[j + 1];
                unsorted_list[j + 1] = temp;
                swapped = true;
            }
        }

        if (!swapped) return unsorted_list;
    }


    return {unsorted_list};
}

int main() {
    vector<int> input = {5, 2, 4, 6, 1, 3};

    vector<int> sorted = bubble_sort(input);

    cout << "Sorted list: ";
    for (int num : sorted) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}