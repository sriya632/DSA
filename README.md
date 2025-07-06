# DSA
Practicing DSA techniques

Data Structures :

Arrays:
Arrays store multiple values of same data type.
The size of an array is fixed.
They are retrieved using index number starting from 0 to n-1.
An element in an array can be accessed by its index in o(1) time.

Strings:

Linked lists:

Singly linked lists:
Singly linked lists contain nodes with data and also a pointer to the next element.
LL donot have any defined size and they are dynamic.
Traversal through the LL takes a lot of time as it has to traverse through each node.
The last node of the linked list doesnot contain any pointer.
LL takes a lot of memory as it has to store both the data and also the pointer to the next node.
No fixed data type for linked list.

Doubly Linked List:
Doubly linked lists have nodes with data and two pointers. One pointer points to the previous node and other to the next node.
The end node doesnt have a pointer pointing to the next. 
Deleting a node from the DLL should be done only after checking if the DLL is empty or not. 

Circular LL:
Circular LL is a singly LL with the pointer from the tail of the LL pointing to the first node. 
Deleting a tail node takes O(n) since before removing , we need to make the pointer from the second last node to point the first node. 

Stack:
Stack is a data strcuture that follows filo
first in last out.
It has three operations : push, pop,peek.

clear()—Clear the stack.
isEmpty()—Check to see if the stack is empty.
push(el)—Put the element el on the top of the stack.
pop()—Take the topmost element from the stack.
topEl()—Return the topmost element in the stack without removing it.

Insertion and deletion from the list have a time complexity of O(1) (on average)

Queue:
Follows FIFO
First in first out.

clear()
size()
enqueue()-adds element to the queue
dequeue()-removes element to the queue
firstel()-return first element
Empty()-checks if empty or not

Sorting :

Insertion Sort:
Insertion sort is a sorting algorithm that takes the first element in an array and considers it sorted.
It then checks the array with the next elements until it finds an element which is lesser than the first one and then swaps thme. 
This continues until there are no swaps left.
time complexity is O(n^2).
no additional space is used.

Selection sort:
From an unsorted array, min element is checked and selected. That minimum element is then swapped with the first element. Next min element is checked from the rest of the elements and then swapped witht he second place . This continues until all elemts are swapped. 
It is not a stable algorithm because elemnts can be jumped if they are of the same value.

time complexity O(n^2)
extra space used.

Bubble Sort:
In bubble sort, first element in an array is selected and it is checked with the rest all items and then swapped. This cycle continues for all first elements until there are no more swaps left. 

the list is sorted on n passes.
Time complexity: O(n^2)
It is a stable algorithm.

Vanilla Binary Search:
Binary search is an efficient array search algorithm. 
It works by narrowing down the search range by half each time. 
The key observation here is that the array is sorted
pick the middle element, so that half elements are discarded.
Time Complexity: O(log(n))
the iterative version of binary search uses O(1) memory 
while the recursive version uses O(log(N)) memory.

Recursion :
Technique where a function calls itself 
Two types :
Tailed recursion :
if recursive call is at the end of the function, its tailed recursion 
Non-tailed Recursion :
The recursion call is not the last call performed in the function.


