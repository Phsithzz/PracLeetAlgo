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
    print("Testing your practice implementations in 06_prefix_sum...")

    try:
        # Test 1: running_sum
        assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10], "Test 1 Failed"
        print("[Pass] Test 1: running_sum")

        # Test 2: NumArray
        na = NumArray([-2, 0, 3, -5, 2, -1])
        assert na.sumRange(0, 2) == 1, "Test 2.1 Failed"
        assert na.sumRange(2, 5) == -1, "Test 2.2 Failed"
        assert na.sumRange(0, 5) == -3, "Test 2.3 Failed"
        print("[Pass] Test 2: NumArray")

        # Test 3: subarray_sum_equals_k
        assert subarray_sum_equals_k([1, 1, 1], 2) == 2, "Test 3.1 Failed"
        assert subarray_sum_equals_k([1, 2, 3], 3) == 2, "Test 3.2 Failed"
        assert subarray_sum_equals_k([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4, "Test 3.3 Failed"
        print("[Pass] Test 3: subarray_sum_equals_k")

        # Test 4: find_max_length_equal_0_1
        assert find_max_length_equal_0_1([0, 1]) == 2, "Test 4.1 Failed"
        assert find_max_length_equal_0_1([0, 1, 0]) == 2, "Test 4.2 Failed"
        assert find_max_length_equal_0_1([0, 1, 1, 0, 1, 1, 1, 0]) == 4, "Test 4.3 Failed"
        print("[Pass] Test 4: find_max_length_equal_0_1")

        print("\n[EXCELLENT] All tests in 06_prefix_sum passed!")
    except AssertionError as e:
        print(f"\n[FAIL] {e}")
        print("Tip: ทบทวนความสัมพันธ์ (current_sum - k) และ {0: 1} ใน README.md / solutions.py")
    except Exception as e:
        print(f"\n[ERROR] เกิดข้อผิดพลาด: {e}")
