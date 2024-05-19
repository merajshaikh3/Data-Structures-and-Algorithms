# HashMap

This repository contains implementations of Hashmaps using three different methods: chaining (using LinkedList), linear probing, and quadratic probing. Below, you'll find a detailed explanation of each method, including how elements are added, what happens in the case of collisions, their time and space complexities, real-world applications, advantages, and disadvantages.

## Methods of Creating Hashmaps
### Chaining (using LinkedList)
**Description:** In this method, each bucket of the hashmap contains a linked list. When a collision occurs (i.e., when multiple keys hash to the same bucket), the new element is added to the linked list at that bucket.

**Adding Elements:**

* Compute the hash code of the key and find the corresponding bucket.
* If the bucket is empty, create a new linked list and add the element.
* If the bucket is not empty, append the new element to the linked list.

**Collision Handling:** Collisions are handled by adding the colliding element to the linked list of the corresponding bucket.

### Linear Probing
**Description:** In linear probing, when a collision occurs, the algorithm searches the next available slot in the array sequentially.

**Adding Elements:**

* Compute the hash code of the key and find the corresponding bucket.
* If the bucket is empty, add the element.
* If the bucket is occupied, check the next slot (i.e., index + 1) until an empty slot is found.

**Collision Handling:** Collisions are resolved by moving sequentially through the array to find the next available slot.

### Quadratic Probing
**Description:** Quadratic probing handles collisions by checking index + 1, index + 4, index + 9, and so on (following a quadratic sequence).

**Adding Elements:**

* Compute the hash code of the key and find the corresponding bucket.
* If the bucket is empty, add the element.
* If the bucket is occupied, use a quadratic function to find the next available slot.

**Collision Handling:** Collisions are resolved by moving through the array using a quadratic function to determine the next slot.

## Time and Space Complexities

| Method | Insertion	| Deletion	| Search	| Space Complexity |
| --- | ---	| ---	| ---	| --- |
| Chaining	| O(1) (avg), O(n) (worst)	| O(1) (avg), O(n) (worst)	| O(1) (avg), O(n) (worst)	| O(n + m) |
| Linear Probing	| O(1) (avg), O(n) (worst)	| O(1) (avg), O(n) (worst)	| O(1) (avg), O(n) (worst)	| O(n) |
| Quadratic Probing	| O(1) (avg), O(n) (worst)	| O(1) (avg), O(n) (worst)	| O(1) (avg), O(n) (worst)	| O(n) |

