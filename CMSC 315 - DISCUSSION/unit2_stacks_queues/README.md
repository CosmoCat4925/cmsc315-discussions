# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

## Reflection Response

1. When completing this project I practiced the implementation of the theory we've learned the last few days. I also learned Pythons's built in collections.deque which uses a doubly linked list to ensure enqueueing and dequeueing both run in O(1) time.
2. When using a standard python library for a queue case causes list.pop(0) to shift all remaining elements to the left, resulting in slow O(n) operations. That is why I used collections.deque which runs far quicker and simpler. Attempting to read index -1 or 0 throws runtime exceptions, so i added a is_empty() check before retrieving or emptying elements.
3. A great example of a real world LIFO system would be a stack of cafeteria trays. or the undo feature of a programming IDE like IntelliJ. A great example of a real world FIFO is a restaurant kitchen fridge. All ingredient expiration dates must be tracked and the soonest dates must be used first, so as not to waste ingredients. A software example of this would be a printer queue. the fist job queued to the printer should be printed first, then the next job, and so forth.