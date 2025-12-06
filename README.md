# Algorithm Homework 02

This repository contains solutions for two fundamental data structure problems: a **Request Processing System** using a Queue (FIFO) and a **Palindrome Checker** using a Deque.

---

## Task 1: Request Processing System Simulation (Queue)

This Python program simulates a service center's request handling process using the `queue.Queue` data structure. It demonstrates the **FIFO (First-In, First-Out)** principle.

### Key Features
* **Request Generation:** Automatically creates new requests with a unique ID.
* **Queue Management:** Adds new requests to the end of the queue (`put()`).
* **Processing Simulation:** Sequentially removes requests from the front of the queue (`get()`) to simulate processing.

### Execution Flow
1.  The `generate_request()` function creates and enqueues a request.
2.  The `process_request()` function dequeues and simulates the handling of a request.
3.  The main loop continuously generates and processes requests, simulating a real-time workflow.

---

## Task 2: Palindrome Checker (Deque)

This program implements a highly efficient palindrome checker using the `collections.deque` (Double-Ended Queue) structure.

### Algorithm Summary
1.  **Preprocessing:** The input string is cleaned to ignore spaces, punctuation, and other non-alphanumeric characters using regular expressions (`re`). All characters are converted to lowercase.
2.  **Deque Population:** The cleaned string's characters are added to the `deque`.
3.  **Comparison:** The program compares characters from both ends simultaneously using `popleft()` and `pop()` until the deque has one or zero elements remaining.

### Requirements Fulfilled
* **Case-Insensitive:** Achieved by converting the input to lowercase.
* **Space/Punctuation-Agnostic:** Achieved by cleaning the string using regex.
* **Efficiency:** The comparison process runs in linear time $O(n)$, as `popleft()` and `pop()` operations are $O(1)$.