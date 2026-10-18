"""
04_two_pointers_sliding_window / practice.py
ไฟล์สำหรับฝึกเขียนโค้ดด้วยตัวเอง
คำแนะนำ: เขียนโค้ดในช่อง TODO โดยไม่เปิดดูเฉลย แล้วรัน 'python practice.py' เพื่อตรวจสอบ
"""

from typing import List


def is_palindrome(s: str) -> bool:
    """
    โจทย์ที่ 1: ตรวจสอบพาลินโดรม (LeetCode 125)
    - เปรียบเทียบตัวอักษรจากหัวและท้ายเข้ามาหากัน
    - ข้ามตัวที่ไม่ใช่ alphanumeric (ใช้ s[i].isalnum()) และไม่สนพิมพ์เล็กใหญ่ (ใช้ .lower())
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def two_sum_sorted(nums: List[int], target: int) -> List[int]:
    """
    โจทย์ที่ 2: Two Sum บน Sorted Array (LeetCode 167)
    - ใช้ left และ right วิ่งเข้าหากัน
    - ถ้า sum < target -> ขยับ left, ถ้า sum > target -> ขยับ right
    - คืนค่า index แบบ 1-based [left + 1, right + 1]
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def max_area_water(height: List[int]) -> int:
    """
    โจทย์ที่ 3: Container With Most Water (LeetCode 11)
    - พื้นที่ = (right - left) * min(height[left], height[right])
    - ตัดสินใจว่าจะขยับ left หรือ right โดยดูว่าเสาไหนเตี้ยกว่า
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def max_sub_array_of_size_k(nums: List[int], k: int) -> int:
    """
    โจทย์ที่ 4: Fixed Sliding Window ขนาด k
    - หาผลรวมที่มากที่สุดของ Subarray ขนาด k
    - คำนวณ k ตัวแรกก่อน แล้วลูปเลื่อน: +nums[i] - nums[i - k]
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def length_of_longest_substring(s: str) -> int:
    """
    โจทย์ที่ 5: Longest Substring Without Repeating Characters (LeetCode 3)
    - Variable Sliding Window: ขยายขอบขวาไปเรื่อยๆ
    - ถ้าเจอตัวซ้ำใน window ให้เลื่อน left ข้ามตำแหน่งตัวซ้ำเดิมนั้น
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def min_sub_array_len(target: int, nums: List[int]) -> int:
    """
    โจทย์ที่ 6: Minimum Size Subarray Sum (LeetCode 209)
    - หาความยาว Subarray ที่สั้นที่สุดที่มีผลรวม >= target
    - ขยายขอบขวาบวกเลขเข้าไป เมื่อ sum >= target ให้บีบขอบซ้ายและอัปเดตคำตอบ
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


# ==========================================
# 🧪 Test Cases ตรวจสอบผลลัพธ์
# ==========================================
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    print("Testing your practice implementations in 04_two_pointers_sliding_window...")

    try:
        # Test 1: is_palindrome
        assert is_palindrome("A man, a plan, a canal: Panama") is True, "Test 1.1 Failed"
        assert is_palindrome("race a car") is False, "Test 1.2 Failed"
        print("[Pass] Test 1: is_palindrome")

        # Test 2: two_sum_sorted
        assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2], "Test 2.1 Failed"
        assert two_sum_sorted([2, 3, 4], 6) == [1, 3], "Test 2.2 Failed"
        print("[Pass] Test 2: two_sum_sorted")

        # Test 3: max_area_water
        assert max_area_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, "Test 3 Failed"
        print("[Pass] Test 3: max_area_water")

        # Test 4: max_sub_array_of_size_k
        assert max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3) == 9, "Test 4 Failed"
        print("[Pass] Test 4: max_sub_array_of_size_k")

        # Test 5: length_of_longest_substring
        assert length_of_longest_substring("abcabcbb") == 3, "Test 5.1 Failed"
        assert length_of_longest_substring("bbbbb") == 1, "Test 5.2 Failed"
        assert length_of_longest_substring("pwwkew") == 3, "Test 5.3 Failed"
        print("[Pass] Test 5: length_of_longest_substring")

        # Test 6: min_sub_array_len
        assert min_sub_array_len(7, [2, 3, 1, 2, 4, 3]) == 2, "Test 6.1 Failed"
        assert min_sub_array_len(4, [1, 4, 4]) == 1, "Test 6.2 Failed"
        assert min_sub_array_len(11, [1, 1, 1, 1, 1]) == 0, "Test 6.3 Failed"
        print("[Pass] Test 6: min_sub_array_len")

        print("\n[EXCELLENT] All tests in 04_two_pointers_sliding_window passed!")
    except AssertionError as e:
        print(f"\n[FAIL] {e}")
        print("Tip: ทบทวนการขยับ pointer ซ้าย-ขวา ใน README.md / solutions.py")
    except Exception as e:
        print(f"\n[ERROR] เกิดข้อผิดพลาด: {e}")
