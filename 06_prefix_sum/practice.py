"""
06_prefix_sum / practice.py
ไฟล์สำหรับฝึกเขียนโค้ดด้วยตัวเอง
คำแนะนำ: เขียนโค้ดในช่อง TODO โดยไม่เปิดดูเฉลย แล้วรัน 'python practice.py' เพื่อตรวจสอบ
"""

from typing import List


def running_sum(nums: List[int]) -> List[int]:
    """
    โจทย์ที่ 1: คำนวณผลรวมสะสม (LeetCode 1480)
    - ตัวอย่าง nums = [1, 2, 3, 4] -> [1, 3, 6, 10]
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


class NumArray:
    """
    โจทย์ที่ 2: Range Sum Query - Immutable (LeetCode 303)
    - เตรียม prefix sum array ไว้ใน __init__ เพื่อให้ตอบ sumRange ได้ใน O(1)
    - ผลรวมช่วง [left, right] = prefix[right + 1] - prefix[left]
    """

    def __init__(self, nums: List[int]):
        # TODO: สร้าง prefix sum list
        pass

    def sumRange(self, left: int, right: int) -> int:
        # TODO: คำนวณผลรวมช่วงใน O(1)
        pass


def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """
    โจทย์ที่ 3: นับจำนวน Subarray ที่มีผลรวมเท่ากับ k (LeetCode 560)
    - วนลูปสะสม current_sum
    - ตรวจว่าเคยมี current_sum - k ใน hash map หรือไม่
    - อย่าลืมตั้งค่าเริ่มต้น {0: 1} ใน hash map
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def find_max_length_equal_0_1(nums: List[int]) -> int:
    """
    โจทย์ที่ 4: Contiguous Array (LeetCode 525)
    - หาความยาวของ Subarray ที่มีจำนวน 0 และ 1 เท่ากัน
    - เคล็ดลับ: เปลี่ยน 0 ให้เป็น -1 แล้วใช้ Prefix Sum + Hash Map {sum: first_index}
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
    print("🚀 ผลการทดสอบโค้ดของคุณ (06_prefix_sum)")
    print("==================================================")

    # Test 1: running_sum
    try:
        sample1 = [1, 2, 3, 4]
        res1 = running_sum(sample1)
        assert res1 == [1, 3, 6, 10], f"Expected [1, 3, 6, 10], got {res1}"
        print("[Pass] โจทย์ที่ 1: running_sum")
        print(f"       -> Input:         {sample1}")
        print(f"       -> Output ของคุณ: {res1} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 1: running_sum -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 1: {e}")

    print("--------------------------------------------------")

    # Test 2: NumArray
    try:
        data2 = [-2, 0, 3, -5, 2, -1]
        na = NumArray(data2)
        r1 = na.sumRange(0, 2)
        r2 = na.sumRange(2, 5)
        r3 = na.sumRange(0, 5)
        assert r1 == 1 and r2 == -1 and r3 == -3, f"Expected (1, -1, -3), got ({r1}, {r2}, {r3})"
        print("[Pass] โจทย์ที่ 2: NumArray")
        print(f"       -> Array: {data2}")
        print(f"       -> sumRange(0, 2): {r1} (ถูกต้อง!)")
        print(f"       -> sumRange(2, 5): {r2} (ถูกต้อง!)")
        print(f"       -> sumRange(0, 5): {r3} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 2: NumArray -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 2: {e}")

    print("--------------------------------------------------")

    # Test 3: subarray_sum_equals_k
    try:
        s3_a = subarray_sum_equals_k([1, 1, 1], 2)
        s3_b = subarray_sum_equals_k([1, 2, 3], 3)
        assert s3_a == 2, f"Expected 2, got {s3_a}"
        assert s3_b == 2, f"Expected 2, got {s3_b}"
        print("[Pass] โจทย์ที่ 3: subarray_sum_equals_k")
        print(f"       -> [1, 1, 1], k=2 -> ผลลัพธ์: {s3_a} (ถูกต้อง!)")
        print(f"       -> [1, 2, 3], k=3 -> ผลลัพธ์: {s3_b} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 3: subarray_sum_equals_k -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 3: {e}")

    print("--------------------------------------------------")

    # Test 4: find_max_length_equal_0_1
    try:
        sample4 = [0, 1, 1, 0, 1, 1, 1, 0]
        res4 = find_max_length_equal_0_1(sample4)
        assert res4 == 4, f"Expected 4, got {res4}"
        print("[Pass] โจทย์ที่ 4: find_max_length_equal_0_1")
        print(f"       -> Input:         {sample4}")
        print(f"       -> Output ของคุณ: {res4} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 4: find_max_length_equal_0_1 -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 4: {e}")

    print("==================================================")
