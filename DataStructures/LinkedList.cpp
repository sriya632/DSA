#include <iostream>
using namespace std;

class Node {
    public:
    int data;
    Node* next;
};
void printList(Node*n){
    while(n!=NULL){
        cout<<n->data<<endl;
        n=n->next;
    }

}
int main(){
Node* head = new Node();
Node* sec = new Node();
Node* third = new Node();
Node* four = new Node();

head->data = 1;
head->next = sec;

sec->data = 2;
sec->next = third;

third->data = 3;
third->next = four;

four->data = 4;
four->next = NULL;

printList(head);
}