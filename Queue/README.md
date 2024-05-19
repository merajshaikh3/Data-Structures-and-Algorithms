# Queues

This repository contains an implementation of a Queue using LinkedLists. Below, you'll find a detailed explanation of the Queue data structure, how elements are added and removed, its time and space complexities, real-world applications, advantages, and disadvantages.

## Queue Implementation Using LinkedLists

**Description:** A Queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. The element that is added first is the one that is removed first. In this implementation, a linked list is used to maintain the order of elements.

**Basic Operations (Methods)**
Enqueue: Adds an element to the end of the queue.
Dequeue: Removes an element from the front of the queue.
Peek: Returns the front element without removing it.
isEmpty: Checks if the queue is empty.

## Time and Space Complexities

| Operation	| Time Complexity	| Space Complexity |
| ---	| ---	| --- |
| Enqueue	| O(1)	| O(1) |
| Dequeue	| O(1)	| O(1) |
| Peek	| O(1)	| O(1) |
| isEmpty	| O(1)	| O(1) |

## Advantages and Disadvantages

Note: These advantages & disadvantages are for the Linked List implementation

| Advantages	| Disadvantages |
| --- | --- |
| Simple to implement	| Access to elements in the middle is slow |
| Dynamic size, not limited by a fixed size	| More memory overhead due to pointers |
| Efficient O(1) time complexity for operations	|

## Use Case	Real-World Examples

| Order Processing Systems	| Managing customer orders in the order they are received |
| ---	| --- |
| Scheduling Tasks	| CPU task scheduling, where tasks are executed in the order they arrive |
| Print Queue Management	| Managing print jobs in a printer queue |
| Breadth-First Search (BFS) Algorithm	| Exploring nodes level by level in tree/graph traversal |
