"""
07_recursion_backtracking / solutions.py
เฉลยตัวอย่างโค้ดที่ถูกต้องและสะอาด สำหรับ Recursion & Backtracking Patterns
"""

from typing import List


def factorial(n: int) -> int:
    """
    คำนวณ N! ด้วย Recursion
    Base Case: n <= 1 -> 1
    Recursive Case: n * factorial(n - 1)
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    หาเลข Fibonacci ลำดับที่ n: F(0)=0, F(1)=1, F(n) = F(n-1) + F(n-2)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def subsets(nums: List[int]) -> List[List[int]]:
    """
    หา Subsets ทั้งหมดที่เป็นไปได้ (Power Set) (LeetCode 78)
    Time: O(N * 2^N)
    Space: O(N) Call Stack
    """
    result: List[List[int]] = []

    def backtrack(start: int, current_path: List[int]):
        # ทุกจุดระหว่างทางคือ subset ที่ถูกต้อง บันทึกสำเนาลงใน result
        result.append(list(current_path))

        for i in range(start, len(nums)):
            # Choose
            current_path.append(nums[i])
            # Explore (เริ่มตัวถัดไป i + 1 เพื่อไม่ให้ซ้ำลำดับเดิม)
            backtrack(i + 1, current_path)
            # Unchoose
            current_path.pop()

    backtrack(0, [])
    return result


def permutations(nums: List[int]) -> List[List[int]]:
    """
    หาการเรียงสับเปลี่ยนทั้งหมด (LeetCode 46)
    Time: O(N * N!)
    Space: O(N)
    """
    result: List[List[int]] = []

    def backtrack(current_path: List[int], used: List[bool]):
        # Base case: เมื่อจัดสมาชิกครบทุกตัวแล้ว
        if len(current_path) == len(nums):
            result.append(list(current_path))
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            # Choose
            used[i] = True
            current_path.append(nums[i])

            # Explore
            backtrack(current_path, used)

            # Unchoose
            current_path.pop()
            used[i] = False

    backtrack([], [False] * len(nums))
    return result


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    หาชุดตัวเลขที่บวกกันได้ target (สามารถใช้เลขตัวเดิมซ้ำได้) (LeetCode 39)
    Time: O(2^T) โดย T คือ target
    Space: O(T)
    """
    result: List[List[int]] = []

    def backtrack(start: int, current_path: List[int], remaining: int):
        # Base Case 1: ผลรวมถึงเป้าหมายแล้ว
        if remaining == 0:
            result.append(list(current_path))
            return

        # Base Case 2: ผลรวมเกินเป้าหมาย (Pruning)
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            candidate = candidates[i]
            # Choose
            current_path.append(candidate)
            # Explore: ส่ง i เดิมเข้าไป เพราะสามารถใช้เลขเดิมซ้ำได้
            backtrack(i, current_path, remaining - candidate)
            # Unchoose
            current_path.pop()

    backtrack(0, [], target)
    return result


# ==========================================
# 🧪 Test Cases ตรวจสอบความถูกต้อง
# ==========================================
if __name__ == "__main__":
    print("Testing 07_recursion_backtracking solutions...")

    # Test 1: factorial
    assert factorial(5) == 120, "Test 1 failed"
    assert factorial(0) == 1, "Test 1.1 failed"

    # Test 2: fibonacci
    assert fibonacci(6) == 8, "Test 2 failed: F(6) = 8"

    # Test 3: subsets
    subs = subsets([1, 2, 3])
    normalized_subs = sorted([sorted(s) for s in subs])
    expected_subs = sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
    assert normalized_subs == expected_subs, f"Test 3 failed: {subs}"

    # Test 4: permutations
    perms = permutations([1, 2, 3])
    assert len(perms) == 6, "Test 4 failed: len should be 3! = 6"
    assert [1, 2, 3] in perms and [3, 2, 1] in perms, "Test 4 elements failed"

    # Test 5: combination_sum
    combos = combination_sum([2, 3, 6, 7], 7)
    normalized_combos = sorted([sorted(c) for c in combos])
    expected_combos = sorted([[2, 2, 3], [7]])
    assert normalized_combos == expected_combos, f"Test 5 failed: {combos}"

    print("[OK] All tests in 07_recursion_backtracking passed successfully!")
