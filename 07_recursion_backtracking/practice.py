"""
07_recursion_backtracking / practice.py
ไฟล์สำหรับฝึกเขียนโค้ดด้วยตัวเอง
คำแนะนำ: เขียนโค้ดในช่อง TODO โดยไม่เปิดดูเฉลย แล้วรัน 'python practice.py' เพื่อตรวจสอบ
"""

from typing import List


def factorial(n: int) -> int:
    """
    โจทย์ที่ 1: คำนวณ N! ด้วย Recursion
    - Base case: n <= 1 คืน 1
    - Recursive case: n * factorial(n - 1)
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def fibonacci(n: int) -> int:
    """
    โจทย์ที่ 2: คำนวณเลข Fibonacci ตัวที่ n
    - F(0) = 0, F(1) = 1
    - F(n) = F(n-1) + F(n-2)
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def subsets(nums: List[int]) -> List[List[int]]:
    """
    โจทย์ที่ 3: Subsets (LeetCode 78)
    - หา Power Set ของ nums
    - โครงสร้าง: backtrack(start, current_path)
    - อย่าลืม copy list: result.append(list(current_path))
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def permutations(nums: List[int]) -> List[List[int]]:
    """
    โจทย์ที่ 4: Permutations (LeetCode 46)
    - สลับเปลี่ยนลำดับสมาชิกทุกรูปแบบ
    - ใช้ array used = [False] * len(nums) เพื่อเช็คว่าหยิบตัวไหนไปแล้ว
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    โจทย์ที่ 5: Combination Sum (LeetCode 39)
    - หาชุดตัวเลขที่บวกกันได้ target (ใช้ตัวเดิมซ้ำได้)
    - Base cases: remaining == 0 (เจอคำตอบ), remaining < 0 (ตัดทิ้ง)
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


# ==========================================
# 🧪 Test Cases ตรวจสอบผลลัพธ์
# ==========================================
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    print("Testing your practice implementations in 07_recursion_backtracking...")

    try:
        # Test 1: factorial
        assert factorial(5) == 120, "Test 1 Failed"
        assert factorial(0) == 1, "Test 1.1 Failed"
        print("[Pass] Test 1: factorial")

        # Test 2: fibonacci
        assert fibonacci(6) == 8, "Test 2 Failed: F(6) = 8"
        print("[Pass] Test 2: fibonacci")

        # Test 3: subsets
        subs = subsets([1, 2, 3])
        normalized_subs = sorted([sorted(s) for s in (subs or [])])
        expected_subs = sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
        assert normalized_subs == expected_subs, f"Test 3 Failed: got {subs}"
        print("[Pass] Test 3: subsets")

        # Test 4: permutations
        perms = permutations([1, 2, 3])
        assert len(perms or []) == 6, "Test 4 Failed: length must be 6"
        assert [1, 2, 3] in (perms or []) and [3, 2, 1] in (perms or []), "Test 4 Failed"
        print("[Pass] Test 4: permutations")

        # Test 5: combination_sum
        combos = combination_sum([2, 3, 6, 7], 7)
        normalized_combos = sorted([sorted(c) for c in (combos or [])])
        expected_combos = sorted([[2, 2, 3], [7]])
        assert normalized_combos == expected_combos, f"Test 5 Failed: got {combos}"
        print("[Pass] Test 5: combination_sum")

        print("\n[EXCELLENT] All tests in 07_recursion_backtracking passed!")
    except AssertionError as e:
        print(f"\n[FAIL] {e}")
        print("Tip: ทบทวน Choose -> Explore -> Unchoose ใน README.md / solutions.py")
    except Exception as e:
        print(f"\n[ERROR] เกิดข้อผิดพลาด: {e}")
