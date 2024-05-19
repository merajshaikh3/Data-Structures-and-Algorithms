# Stacks

This repository contains an implementation of a Stack using LinkedLists. Below, you'll find a detailed explanation of the Stack data structure, how elements are added and removed, its time and space complexities, real-world applications, advantages, and disadvantages.

## Stack Implementation Using LinkedLists

**Description:** A Stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. The element that is added last is the one that is removed first. In this implementation, a linked list is used to maintain the order of elements.

**Basic Operations (Methods)**
* Push: Adds an element to the top of the stack.
* Pop: Removes the top element from the stack.
* Peek: Returns the top element without removing it.
* isEmpty: Checks if the stack is empty.

## Time and Space Complexities

| Operation	| Time Complexity	| Space Complexity |
| ---	| ---	| --- |
| Push	| O(1)	| O(1) |
| Pop	| O(1)	| O(1) |
| Peek	| O(1)	| O(1) |
| isEmpty	| O(1)	| O(1) |

## Advantages and Disadvantages

Note: These advantages & disadvantages are for the Linked List implementation

| Advantages	| Disadvantages |
| --- | --- |
| Simple to implement	| Access to elements other than the top is slow |
| Dynamic size, not limited by a fixed size	| More memory overhead due to pointers |
| Efficient O(1) time complexity for operations	|

## Use Case	Real-World Examples

| Use Case | Details |
| ---	| --- |
| Function Call Management	| Managing function calls and recursion |
| Expression Evaluation	| Evaluating expressions in compilers |
| Undo Mechanisms	| Implementing undo features in applications |
| Depth-First Search (DFS) Algorithm	| Exploring nodes deep into the graph before backtracking |
