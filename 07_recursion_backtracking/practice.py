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
    print("==================================================")
    print("🚀 ผลการทดสอบโค้ดของคุณ (07_recursion_backtracking)")
    print("==================================================")

    # Test 1: factorial
    try:
        res1_a = factorial(5)
        res1_b = factorial(0)
        assert res1_a == 120 and res1_b == 1, f"Expected (120, 1), got ({res1_a}, {res1_b})"
        print("[Pass] โจทย์ที่ 1: factorial")
        print(f"       -> factorial(5) = {res1_a} (ถูกต้อง!)")
        print(f"       -> factorial(0) = {res1_b} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 1: factorial -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 1: {e}")

    print("--------------------------------------------------")

    # Test 2: fibonacci
    try:
        res2 = fibonacci(6)
        assert res2 == 8, f"Expected 8, got {res2}"
        print("[Pass] โจทย์ที่ 2: fibonacci")
        print(f"       -> fibonacci(6) = {res2} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 2: fibonacci -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 2: {e}")

    print("--------------------------------------------------")

    # Test 3: subsets
    try:
        sample3 = [1, 2, 3]
        subs = subsets(sample3)
        normalized_subs = sorted([sorted(s) for s in (subs or [])])
        expected_subs = sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
        assert normalized_subs == expected_subs, f"Expected {expected_subs}, got {subs}"
        print("[Pass] โจทย์ที่ 3: subsets")
        print(f"       -> Input:         {sample3}")
        print(f"       -> Output ของคุณ: {subs} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 3: subsets -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 3: {e}")

    print("--------------------------------------------------")

    # Test 4: permutations
    try:
        sample4 = [1, 2, 3]
        perms = permutations(sample4)
        assert len(perms or []) == 6 and [1, 2, 3] in (perms or []), f"Permutations invalid: {perms}"
        print("[Pass] โจทย์ที่ 4: permutations")
        print(f"       -> Input:         {sample4}")
        print(f"       -> จำนวนรูปแบบ:   {len(perms)} รูปแบบ (ครบ 3! = 6 รูปแบบ)")
        print(f"       -> Output ของคุณ: {perms} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 4: permutations -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 4: {e}")

    print("--------------------------------------------------")

    # Test 5: combination_sum
    try:
        sample5 = [2, 3, 6, 7]
        target5 = 7
        combos = combination_sum(sample5, target5)
        normalized_combos = sorted([sorted(c) for c in (combos or [])])
        expected_combos = sorted([[2, 2, 3], [7]])
        assert normalized_combos == expected_combos, f"Expected {expected_combos}, got {combos}"
        print("[Pass] โจทย์ที่ 5: combination_sum")
        print(f"       -> candidates: {sample5}, target: {target5}")
        print(f"       -> Output ของคุณ: {combos} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 5: combination_sum -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 5: {e}")

    print("==================================================")
