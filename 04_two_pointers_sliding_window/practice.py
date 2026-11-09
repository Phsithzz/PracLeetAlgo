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
    print("==================================================")
    print("🚀 ผลการทดสอบโค้ดของคุณ (04_two_pointers_sliding_window)")
    print("==================================================")

    # Test 1: is_palindrome
    try:
        res1_a = is_palindrome("A man, a plan, a canal: Panama")
        res1_b = is_palindrome("race a car")
        assert res1_a is True, f"Expected True, got {res1_a}"
        assert res1_b is False, f"Expected False, got {res1_b}"
        print("[Pass] โจทย์ที่ 1: is_palindrome")
        print(f"       -> 'A man, a plan, a canal: Panama' -> {res1_a} (ถูกต้อง!)")
        print(f"       -> 'race a car'                     -> {res1_b} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 1: is_palindrome -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 1: {e}")

    print("--------------------------------------------------")

    # Test 2: two_sum_sorted
    try:
        res2_a = two_sum_sorted([2, 7, 11, 15], 9)
        res2_b = two_sum_sorted([2, 3, 4], 6)
        assert res2_a == [1, 2], f"Expected [1, 2], got {res2_a}"
        assert res2_b == [1, 3], f"Expected [1, 3], got {res2_b}"
        print("[Pass] โจทย์ที่ 2: two_sum_sorted")
        print(f"       -> [2, 7, 11, 15], target=9 -> Output (1-based): {res2_a} (ถูกต้อง!)")
        print(f"       -> [2, 3, 4], target=6      -> Output (1-based): {res2_b} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 2: two_sum_sorted -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 2: {e}")

    print("--------------------------------------------------")

    # Test 3: max_area_water
    try:
        heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        res3 = max_area_water(heights)
        assert res3 == 49, f"Expected 49, got {res3}"
        print("[Pass] โจทย์ที่ 3: max_area_water")
        print(f"       -> Heights:       {heights}")
        print(f"       -> Output ของคุณ: {res3} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 3: max_area_water -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 3: {e}")

    print("--------------------------------------------------")

    # Test 4: max_sub_array_of_size_k
    try:
        nums4 = [2, 1, 5, 1, 3, 2]
        res4 = max_sub_array_of_size_k(nums4, 3)
        assert res4 == 9, f"Expected 9, got {res4}"
        print("[Pass] โจทย์ที่ 4: max_sub_array_of_size_k")
        print(f"       -> nums: {nums4}, k=3")
        print(f"       -> Output ของคุณ: {res4} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 4: max_sub_array_of_size_k -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 4: {e}")

    print("--------------------------------------------------")

    # Test 5: length_of_longest_substring
    try:
        res5_a = length_of_longest_substring("abcabcbb")
        res5_b = length_of_longest_substring("bbbbb")
        res5_c = length_of_longest_substring("pwwkew")
        assert res5_a == 3, f"'abcabcbb' Expected 3, got {res5_a}"
        assert res5_b == 1, f"'bbbbb' Expected 1, got {res5_b}"
        assert res5_c == 3, f"'pwwkew' Expected 3, got {res5_c}"
        print("[Pass] โจทย์ที่ 5: length_of_longest_substring")
        print(f"       -> 'abcabcbb' -> {res5_a} (ถูกต้อง!)")
        print(f"       -> 'bbbbb'    -> {res5_b} (ถูกต้อง!)")
        print(f"       -> 'pwwkew'   -> {res5_c} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 5: length_of_longest_substring -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 5: {e}")

    print("--------------------------------------------------")

    # Test 6: min_sub_array_len
    try:
        res6_a = min_sub_array_len(7, [2, 3, 1, 2, 4, 3])
        res6_b = min_sub_array_len(4, [1, 4, 4])
        res6_c = min_sub_array_len(11, [1, 1, 1, 1, 1])
        assert res6_a == 2, f"Target 7 Expected 2, got {res6_a}"
        assert res6_b == 1, f"Target 4 Expected 1, got {res6_b}"
        assert res6_c == 0, f"Target 11 Expected 0, got {res6_c}"
        print("[Pass] โจทย์ที่ 6: min_sub_array_len")
        print(f"       -> target=7, [2, 3, 1, 2, 4, 3] -> {res6_a} (ถูกต้อง!)")
        print(f"       -> target=4, [1, 4, 4]          -> {res6_b} (ถูกต้อง!)")
        print(f"       -> target=11, [1, 1, 1, 1, 1]   -> {res6_c} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 6: min_sub_array_len -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 6: {e}")

    print("==================================================")
