"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""

import time


def bubble_sort(lst):
    """
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.
    """
    # Create a copy of the list to avoid modifying the original input
    arr = list(lst)
    n = len(arr)

    # Perform passes through the array
    for i in range(n):
        swapped = False
        # Last i elements are already in place, so we iterate up to n - i - 1
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Optimization: If no elements were swapped during this pass, the array is already sorted
        if not swapped:
            break

    return arr


def merge_sort(lst):
    """
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.
    """
    # Base case: a list with 0 or 1 element is already sorted
    if len(lst) <= 1:
        return list(lst)

    # Find the middle point to split the array into two halves
    mid = len(lst) // 2

    # Recursively divide and sort the left and right halves
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    # Merge the sorted halves and return the unified list
    return merge(left_half, right_half)


def merge(left, right):
    """
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    i = 0  # Pointer for left list
    j = 0  # Pointer for right list

    # Compare elements from both lists and append the smaller one to result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements from left, if any
    while i < len(left):
        result.append(left[i])
        i += 1

    # Append remaining elements from right, if any
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # DATASET #1
    # ===============================
    print("\n=== DATASET #1 ===")
    dataset_1 = [64, 34, 25, 12, 22, 11, 90, 5, 42]
    print(f"Original Dataset #1: {dataset_1}")

    b_sorted_1 = bubble_sort(dataset_1)
    m_sorted_1 = merge_sort(dataset_1)

    print(f"Bubble Sort Result:  {b_sorted_1}")
    print(f"Merge Sort Result:   {m_sorted_1}")

    # ===============================
    # DATASET #2
    # ===============================
    print("\n=== DATASET #2 ===")
    dataset_2 = [105, 8, 43, 99, 12, 87, 3, 56, 71, 19]
    print(f"Original Dataset #2: {dataset_2}")

    b_sorted_2 = bubble_sort(dataset_2)
    m_sorted_2 = merge_sort(dataset_2)

    print(f"Bubble Sort Result:  {b_sorted_2}")
    print(f"Merge Sort Result:   {m_sorted_2}")

    # ===============================
    # EDGE CASE TESTS
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    edge_cases = {
        "Empty List": [],
        "Single Element List": [42],
        "Already Sorted List": [1, 2, 3, 4, 5, 6, 7],
        "Reverse Sorted List": [9, 7, 5, 3, 1],
        "List with Duplicates": [5, 2, 8, 2, 5, 1, 8],
    }

    for name, data in edge_cases.items():
        print(f"\nTesting Edge Case: {name}")
        print(f"  Input:       {data}")
        print(f"  Bubble Sort: {bubble_sort(data)}")
        print(f"  Merge Sort:  {merge_sort(data)}")

    # Explanation of Edge Cases:
    # 1. Empty/Single Element: Base case triggers immediately in Merge Sort. Bubble Sort loops 0 or 1 time without swapping.
    # 2. Already Sorted: Bubble Sort hits swapped=False on pass 1 and terminates in O(N) time. Merge Sort still divides and reconstructs in O(N log N).
    # 3. Reverse Sorted: Represents worst-case scenario for Bubble Sort requiring max swaps (O(N^2)). Merge Sort performs normally (O(N log N)).
    # 4. Duplicates: Both algorithms handle duplicates cleanly maintaining stable relative order.

    # ===============================
    # PERFORMANCE ANALYSIS
    # ===============================
    print("\n=== PERFORMANCE ANALYSIS ===")
    large_dataset = list(range(2000, 0, -1))  # Reverse sorted list of 2000 items (worst case for Bubble Sort)

    start_time = time.perf_counter()
    bubble_sort(large_dataset)
    bubble_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    merge_sort(large_dataset)
    merge_time = time.perf_counter() - start_time

    print(f"Dataset Size: {len(large_dataset)} elements (Reverse-sorted worst case)")
    print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
    print(f"Merge Sort Time:  {merge_time:.6f} seconds")

    # ===============================
    # REAL-WORLD APPLICATION: COFFEE BEAN INVENTORY
    # ===============================
    print("\n=== REAL-WORLD EXAMPLE: COFFEE BEAN INVENTORY ===")

    # Custom comparison helper to sort tuples/dicts by coffee roast rating (scale 1-100)
    coffee_inventory = [
        {"name": "Ethiopian Yirgacheffe", "roast_score": 88},
        {"name": "Colombian Supremo", "roast_score": 75},
        {"name": "Guatemala Antigua", "roast_score": 92},
        {"name": "Sumatra Mandheling", "roast_score": 81},
        {"name": "Costa Rica Tarrazu", "roast_score": 85},
    ]

    def merge_sort_coffee(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = merge_sort_coffee(lst[:mid])
        right = merge_sort_coffee(lst[mid:])

        # Custom merge step extracting 'roast_score'
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i]["roast_score"] >= right[j]["roast_score"]:  # Sort highest rating first
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sorted_coffee = merge_sort_coffee(coffee_inventory)

    print("Coffee varieties sorted by Roast Score (Highest to Lowest):")
    for item in sorted_coffee:
        print(f"  - {item['name']}: Score {item['roast_score']}/100")


if __name__ == "__main__":
    main()