"""
04_two_pointers_sliding_window / solutions.py
เฉลยตัวอย่างโค้ดที่ถูกต้องและสะอาด สำหรับ Two Pointers และ Sliding Window
"""

from typing import List


def is_palindrome(s: str) -> bool:
    """
    ตรวจสอบว่าเป็น Palindrome หรือไม่ โดยข้ามอักขระพิเศษและไม่สนตัวพิมพ์เล็กใหญ่ (LeetCode 125)
    Time: O(N)
    Space: O(1)
    """
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def two_sum_sorted(nums: List[int], target: int) -> List[int]:
    """
    หาคู่ผลรวมใน Sorted Array โดยใช้ Two Pointers (LeetCode 167 - คืน index 1-based)
    Time: O(N)
    Space: O(1)
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1  # ผลรวมน้อยไป ขยับซ้ายขึ้นเพื่อเพิ่มค่า
        else:
            right -= 1  # ผลรวมมากไป ขยับขวาลงเพื่อลดค่า

    return []


def max_area_water(height: List[int]) -> int:
    """
    หาพื้นที่เก็บน้ำมากที่สุด (LeetCode 11 - Container With Most Water)
    แนวคิด: กว้างสุดเริ่มที่สองฝั่งสุด แล้วขยับเสาต้นที่เตี้ยกว่าเข้ามา
    Time: O(N)
    Space: O(1)
    """
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        current_water = width * h
        max_water = max(max_water, current_water)

        # ขยับเสาข้างที่เตี้ยกว่า เพราะการขยับเสาสูงไม่มีทางได้พื้นที่มากกว่าเดิม
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


def max_sub_array_of_size_k(nums: List[int], k: int) -> int:
    """
    Sliding Window ขนาดคงที่: หาผลรวมมากที่สุดของ Subarray ขนาด k
    Time: O(N)
    Space: O(1)
    """
    if len(nums) < k or k <= 0:
        return 0

    # คำนวณผลรวมของ window แรก
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # เลื่อน window ไปทีละ 1 ช่อง
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def length_of_longest_substring(s: str) -> int:
    """
    หาความยาวของ Substring ที่ไม่มีตัวอักษรซ้ำเลย (LeetCode 3)
    แนวคิด: Sliding Window + Dict จำตำแหน่งล่าสุดของตัวอักษร
    Time: O(N)
    Space: O(min(N, alphabet_size))
    """
    char_index_map = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        # ถ้าเจอตัวอักษรซ้ำ และตำแหน่งที่ซ้ำอยู่ใน window ปัจจุบัน
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1

        char_index_map[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


def min_sub_array_len(target: int, nums: List[int]) -> int:
    """
    หาขนาด Subarray ที่สั้นที่สุดที่ผลรวม >= target (LeetCode 209)
    แนวคิด: Variable Sliding Window ขยายขวา บีบซ้ายเมื่อผลรวมถึงเป้าหมาย
    Time: O(N)
    Space: O(1)
    """
    left = 0
    current_sum = 0
    min_len = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]

        # เมื่อผลรวม >= target ให้ลองบีบขอบซ้ายเข้ามา
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len != float("inf") else 0


# ==========================================
# 🧪 Test Cases ตรวจสอบความถูกต้อง
# ==========================================
if __name__ == "__main__":
    print("Testing 04_two_pointers_sliding_window solutions...")

    # Test 1: is_palindrome
    assert is_palindrome("A man, a plan, a canal: Panama") is True, "Test 1.1 failed"
    assert is_palindrome("race a car") is False, "Test 1.2 failed"

    # Test 2: two_sum_sorted
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2], "Test 2.1 failed"
    assert two_sum_sorted([2, 3, 4], 6) == [1, 3], "Test 2.2 failed"

    # Test 3: max_area_water
    assert max_area_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, "Test 3 failed"

    # Test 4: max_sub_array_of_size_k
    assert max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3) == 9, "Test 4 failed"

    # Test 5: length_of_longest_substring
    assert length_of_longest_substring("abcabcbb") == 3, "Test 5.1 failed"
    assert length_of_longest_substring("bbbbb") == 1, "Test 5.2 failed"
    assert length_of_longest_substring("pwwkew") == 3, "Test 5.3 failed"

    # Test 6: min_sub_array_len
    assert min_sub_array_len(7, [2, 3, 1, 2, 4, 3]) == 2, "Test 6.1 failed"
    assert min_sub_array_len(4, [1, 4, 4]) == 1, "Test 6.2 failed"
    assert min_sub_array_len(11, [1, 1, 1, 1, 1]) == 0, "Test 6.3 failed"

    print("[OK] All tests in 04_two_pointers_sliding_window passed successfully!")
