"""
01_array_basics / solutions.py
เฉลยตัวอย่างโค้ดที่ถูกต้องและสะอาด สำหรับหัวข้อ Array Traversal & Index Manipulation
"""

from typing import List, Tuple


def find_max_min(nums: List[int]) -> Tuple[int, int]:
    """
    หาค่าสูงสุดและต่ำสุดใน Array ด้วยการวนลูปเที่ยวเดียว
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if not nums:
        raise ValueError("nums list must not be empty")

    current_max = nums[0]
    current_min = nums[0]

    for num in nums[1:]:
        if num > current_max:
            current_max = num
        elif num < current_min:
            current_min = num

    return current_max, current_min


def reverse_array_inplace(nums: List[int]) -> None:
    """
    กลับด้าน Array แบบ In-place โดยใช้ Two Pointers ฝั่งซ้ายและขวา
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        # In-place swap ใน Python
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def move_zeroes(nums: List[int]) -> None:
    """
    ย้าย 0 ทั้งหมดไปไว้ท้าย Array โดยคงลำดับเดิมของตัวเลขอื่นไว้ (LeetCode 283)
    แนวคิด: Two Pointers (Slow pointer ชี้ตำแหน่งว่างที่จะวางเลขที่ไม่ใช่ 0)
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    insert_pos = 0

    # สเต็ป 1: ย้ายเลขที่ไม่ใช่ 0 มาไว้ข้างหน้า
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    # สเต็ป 2: เติม 0 ในตำแหน่งที่เหลือทั้งหมด
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1


def rotate_array(nums: List[int], k: int) -> None:
    """
    หมุน Array ไปทางขวา k ตำแหน่ง แบบ In-place (LeetCode 189)
    เทคนิค 3 Reversals:
    1. Reverse ทั้งหมด
    2. Reverse ช่วง 0 ถึง k-1
    3. Reverse ช่วง k ถึง n-1
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    n = len(nums)
    if n == 0:
        return
    k = k % n  # ป้องกันกรณี k มากกว่าขนาด array

    def reverse_range(arr: List[int], start: int, end: int) -> None:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # 1. กลับด้านทั้ง Array
    reverse_range(nums, 0, n - 1)
    # 2. กลับด้าน k ตัวแรก
    reverse_range(nums, 0, k - 1)
    # 3. กลับด้านตัวที่เหลือ
    reverse_range(nums, k, n - 1)


# ==========================================
# 🧪 Test Cases ตรวจสอบความถูกต้อง
# ==========================================
if __name__ == "__main__":
    print("Testing 01_array_basics solutions...")

    # Test 1: find_max_min
    sample1 = [3, 7, 2, 9, 1, 5]
    assert find_max_min(sample1) == (9, 1), "Test 1 failed: find_max_min"

    # Test 2: reverse_array_inplace
    sample2 = [1, 2, 3, 4, 5]
    reverse_array_inplace(sample2)
    assert sample2 == [5, 4, 3, 2, 1], "Test 2 failed: reverse_array_inplace"

    # Test 3: move_zeroes
    sample3 = [0, 1, 0, 3, 12]
    move_zeroes(sample3)
    assert sample3 == [1, 3, 12, 0, 0], "Test 3 failed: move_zeroes"

    # Test 4: rotate_array
    sample4 = [1, 2, 3, 4, 5, 6, 7]
    rotate_array(sample4, 3)
    assert sample4 == [5, 6, 7, 1, 2, 3, 4], "Test 4 failed: rotate_array"

    print("[OK] All tests in 01_array_basics passed successfully!")
