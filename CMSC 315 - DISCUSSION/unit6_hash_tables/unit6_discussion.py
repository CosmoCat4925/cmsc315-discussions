"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # How Python Dictionaries behave as Hash Tables:
    # - Python dictionaries are implemented under the hood using a dynamic hash table.
    # - When a key-value pair is inserted, Python computes a hash value for the key using `hash(key)`.
    # - This hash code is mapped to an index in an underlying array (bucket array).
    # - This implementation allows average-time O(1) complexity for insertion, lookup, and deletion.

    # 1. Create an empty dictionary
    student_grades = {}

    # 2. Add at least 5 key-value pairs (Real-World Scenario: Student Grade Book)
    student_grades["Alice"] = 92.5
    student_grades["Bob"] = 85.0
    student_grades["Charlie"] = 78.0
    student_grades["Diana"] = 95.5
    student_grades["Evan"] = 88.0

    print("\n=== INSERT OPERATIONS ===")
    print("Populated Student Grades Dictionary:")
    # 4. Display the contents
    for student, grade in student_grades.items():
        print(f"  - {student}: {grade}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    # How Lookup Works:
    # - When accessing `student_grades["Alice"]`, Python hashes the key "Alice".
    # - It checks the hash table location corresponding to that hash code.
    # - Because the lookup directly accesses the calculated index without scanning all items,
    #   retrieval takes constant time O(1) on average.

    print("\n=== LOOKUP OPERATIONS ===")
    alice_grade = student_grades["Alice"]
    diana_grade = student_grades["Diana"]

    print(f"Retrieved Alice's Grade: {alice_grade}")
    print(f"Retrieved Diana's Grade: {diana_grade}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    # How Update Works:
    # - Keys in a hash table must be unique.
    # - Assigning a value to an existing key causes Python to locate the existing entry
    #   via its hash code and overwrite its associated value rather than adding a new pair.

    print("\n=== UPDATE OPERATIONS ===")
    print(f"Before Update (Charlie): {student_grades['Charlie']}")

    # Updating Charlie's grade after extra credit submission
    student_grades["Charlie"] = 84.0

    print(f"After Update  (Charlie): {student_grades['Charlie']}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    # How Deletion Works:
    # - The `del` keyword (or `.pop()` method) calculates the key's hash, locates its index,
    #   and removes the key-value pair from the table.
    # - Python marks the entry bucket as deleted/empty so future operations continue operating efficiently.

    print("\n=== DELETE OPERATIONS ===")
    print(f"Dictionary before deleting Evan: {student_grades}")

    # Remove Evan from the dictionary using `del`
    del student_grades["Evan"]

    print(f"Dictionary after deleting Evan:  {student_grades}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Looking up a non-existent key using bracket notation vs .get()
    # Direct access like `student_grades["Frank"]` raises a `KeyError` if the key is not in the hash table.
    # Safe lookup uses the `.get()` method, which returns `None` (or a specified default) without crashing.
    print("--- Edge Case 1: Looking up a missing key ---")
    missing_student = "Frank"
    result = student_grades.get(missing_student, "Student Not Found")
    print(f"Lookup for '{missing_student}': {result}")

    # Edge Case 2: Safely deleting a missing key
    # Using `del student_grades["Frank"]` directly raises a `KeyError`.
    # Using `.pop(key, default)` safely attempts removal without causing an unhandled exception.
    print("\n--- Edge Case 2: Safely deleting a missing key ---")
    deleted_val = student_grades.pop("Frank", "Key did not exist - no error raised")
    print(f"Attempted deletion of 'Frank': {deleted_val}")

    # Edge Case 3: Assigning/Updating a missing key
    # Assigning to a non-existent key will not fail; instead, Python inserts it as a new entry.
    print("\n--- Edge Case 3: Updating a key that doesn't exist ---")
    print(f"Contains 'Grace' before update? {'Grace' in student_grades}")
    student_grades["Grace"] = 91.0  # Acts as an insertion
    print(f"Contains 'Grace' after update?  {'Grace' in student_grades}")
    print(f"Updated dictionary: {student_grades}")


if __name__ == "__main__":
    main()