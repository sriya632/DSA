
#include <iostream>
#include <vector>
using namespace std;

vector<int> selection_sort(vector<int> unsorted_list) {
    int n = unsorted_list.size();
    for(int i =0;i<n;i++){
    int min = i;
    for(int j=i;j<n;j++){
        if(unsorted_list[min]>unsorted_list[j]){
            min = j;
        }
    }
        int temp=unsorted_list[min];
        unsorted_list[min]=unsorted_list[i];
        unsorted_list[i]=temp;
        
    }
    
    return {unsorted_list};
}

int main() {
    vector<int> input = {5, 2, 4, 6, 1, 3};

    vector<int> sorted = selection_sort(input);

    cout << "Sorted list: ";
    for (int num : sorted) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
