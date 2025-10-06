"""
performance_lab.py
HOW TO RUN:
  python performance_lab.py
"""

from collections import Counter
from typing import List, Tuple, Optional, Iterable


# ─────────────────────────────────────────────────────────
# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3
# ─────────────────────────────────────────────────────────
def most_frequent(numbers: Iterable[int]) -> Optional[int]:
    """
    Returns one of the values with the highest frequency.
    If numbers is empty, returns None.
    """
    numbers = list(numbers)
    if not numbers:
        return None
    counts = Counter(numbers)
    # Counter.most_common(1) returns [(value, count)]
    return counts.most_common(1)[0][0]

"""
Time and Space Analysis for problem 1:
- Best-case: O(1) if the input is empty (we return early).
- Worst-case: O(n) to count all elements.
- Average-case: O(n) — single pass to count, constant work per element on average.
- Space complexity: O(k) where k is # of distinct elements (<= n) to store the frequency map.
- Why this approach? Counter/dict gives O(1) average-time updates and easy extraction of the mode.
- Could it be optimized? If values are from a small, known range, an array bucket count could be faster/lower-overhead.
"""


# ─────────────────────────────────────────────────────────
# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]
# ─────────────────────────────────────────────────────────
def remove_duplicates(nums: Iterable[int]) -> List[int]:
    """
    Preserves the first occurrence of each element, discarding later duplicates.
    """
    seen = set()
    out: List[int] = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

"""
Time and Space Analysis for problem 2:
- Best-case: O(n) — even if all are duplicates, we still scan once.
- Worst-case: O(n) — all unique, we insert each into the set.
- Average-case: O(n).
- Space complexity: O(k) where k is # of unique elements (<= n), plus O(n) for the output list.
- Why this approach? A set gives O(1) average membership checks, making one linear pass sufficient.
- Could it be optimized? If input is sorted, we can remove dupes in O(n) with O(1) extra space by comparing adjacents.
"""


# ─────────────────────────────────────────────────────────
# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]
# ─────────────────────────────────────────────────────────
def find_pairs(nums: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Optimized O(n) average-time solution using a set of seen values.
    Assumes `nums` contains no duplicates.
    Returns list of (small, large) tuples; output order not guaranteed.
    """
    seen = set()
    pairs: List[Tuple[int, int]] = []
    for x in nums:
        need = target - x
        if need in seen:
            a, b = (need, x) if need < x else (x, need)
            pairs.append((a, b))
        seen.add(x)
    return pairs


def find_pairs_naive(nums: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Naive O(n^2) double loop for comparison (Optimize One baseline).
    Assumes nums has no duplicates.
    """
    n = len(nums)
    out: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                a, b = (nums[i], nums[j]) if nums[i] < nums[j] else (nums[j], nums[i])
                out.append((a, b))
    return out

"""
Time and Space Analysis for problem 3:
- Best-case: O(n) optimized (single pass; pairs found as we go). Naive: O(n^2).
- Worst-case: O(n) optimized (still single pass, few/no pairs). Naive: O(n^2).
- Average-case: O(n) optimized; O(n^2) naive.
- Space complexity: Optimized uses O(n) for the seen set and O(p) for output. Naive uses O(p) for output only.
- Why this approach? The set-based method trades memory for speed, reducing quadratic work to linear on average.
- Could it be optimized? If the list is sorted, a two-pointer approach is O(n) time and O(1) extra space (besides output).
- Refactor comparison (Optimize One): Naive double loop (O(n^2)) → Set-based single pass (O(n)), much better for large inputs.
"""


# ─────────────────────────────────────────────────────────
# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.
# ─────────────────────────────────────────────────────────
def add_n_items(n: int, initial_capacity: int = 1) -> List[int]:
    """
    Simulates dynamic array resizing by doubling capacity when full.
    Prints a message each time a resize occurs, including copy cost.
    Returns the filled list (values 0..n-1) to make testing easy.
    """
    capacity = max(1, int(initial_capacity))
    size = 0
    arr = [None] * capacity
    for i in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            new_arr = [None] * new_capacity
            # simulate copy
            for j in range(size):
                new_arr[j] = arr[j]
            arr = new_arr
            print(f"Resizing: {capacity} → {new_capacity} (copied {size} items)")
            capacity = new_capacity
        arr[size] = i
        size += 1
    return arr[:size]

"""
Time and Space Analysis for problem 4:
- When do resizes happen? Whenever size == capacity; capacity doubles (1→2→4→8→...).
- Worst-case for a single append: O(k) to copy k items during a resize (k equals old capacity).
- Amortized time per append overall: O(1). Over n appends, total copies form a geometric series: < 2n.
- Space complexity: O(n) for the stored items; plus transient O(capacity) during each resize.
- Why does doubling reduce cost overall? Doubling ensures resizes become exponentially rarer, so average cost per append stays constant.
"""


# ─────────────────────────────────────────────────────────
# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]
# ─────────────────────────────────────────────────────────
def running_total(nums: Iterable[float]) -> List[float]:
    """
    Returns prefix sums of nums.
    """
    out: List[float] = []
    s = 0
    for x in nums:
        s += x
        out.append(s)
    return out

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) — must read each element at least once.
- Worst-case: O(n).
- Average-case: O(n).
- Space complexity: O(n) to store the output prefix sums.
- Why this approach? One pass with an accumulator is optimal and simple.
- Could it be optimized? If we were allowed to mutate input in place, we could compute prefix sums in O(1) extra space.
"""


# ─────────────────────────────────────────────────────────
# TESTS (edge cases included)
# ─────────────────────────────────────────────────────────
def _test_p1():
    assert most_frequent([]) is None
    assert most_frequent([7]) == 7
    got = most_frequent([1, 2, 2, 3, 3])  # tie: 2 or 3 acceptable
    assert got in (2, 3)
    assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3

def _test_p2():
    assert remove_duplicates([]) == []
    assert remove_duplicates([1]) == [1]
    assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([3, -1, 3, -1, 2]) == [3, -1, 2]

def _test_p3():
    assert find_pairs([], 5) == []
    assert find_pairs([5], 5) == []
    assert set(find_pairs([1, 2, 3, 4], 5)) == {(1, 4), (2, 3)}
    assert set(find_pairs([0, -1, 1, 2], 1)) == {(-1, 2), (0, 1)}
    # Compare to naive for sanity
    import random
    arr = random.sample(range(-50, 50), 20)  # distinct values
    t = 10
    assert set(find_pairs(arr, t)) == set(find_pairs_naive(arr, t))

def _test_p4():
    assert add_n_items(0) == []
    assert add_n_items(1) == [0]
    # This will also print the resize messages: 1→2→4→8
    assert add_n_items(6, initial_capacity=1) == [0, 1, 2, 3, 4, 5]

def _test_p5():
    assert running_total([]) == []
    assert running_total([5]) == [5]
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_total([0, -1, 1]) == [0, -1, 0]
    # Floating example: prefix sums of [0.5, 0.5] are [0.5, 1.0]
    assert running_total([0.5, 0.5]) == [0.5, 1.0]


# ─────────────────────────────────────────────────────────
# TEST RUNNER  (keep this at the very end)
# ─────────────────────────────────────────────────────────
def run_tests():
    _test_p1()
    _test_p2()
    _test_p3()
    _test_p4()
    _test_p5()
    print("All tests passed ✅")


if __name__ == "__main__":
    run_tests()
    # Show the resize prints explicitly (Problem 4 demo)
    print("Resizing demo:")
    add_n_items(6)
    print("DONE ✅")
