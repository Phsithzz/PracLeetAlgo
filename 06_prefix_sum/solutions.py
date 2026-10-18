"""
06_prefix_sum / solutions.py
เฉลยตัวอย่างโค้ดที่ถูกต้องและสะอาด สำหรับ Prefix Sum Patterns
"""

from typing import List


def running_sum(nums: List[int]) -> List[int]:
    """
    คำนวณผลรวมสะสม (LeetCode 1480)
    Time: O(N)
    Space: O(1) ถ้าไม่นับ array ผลลัพธ์
    """
    result = []
    current_sum = 0
    for num in nums:
        current_sum += num
        result.append(current_sum)
    return result


class NumArray:
    """
    Range Sum Query - Immutable (LeetCode 303)
    คำนวณ Prefix Sum Array ล่วงหน้า เพื่อตอบ sumRange(left, right) ใน O(1)
    """

    def __init__(self, nums: List[int]):
        # prefix[i] เก็บผลรวม nums ตั้งแต่ 0 ถึง i-1 โดย prefix[0] = 0
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        """
        ผลรวมช่วง [left, right]
        Time: O(1)
        """
        return self.prefix[right + 1] - self.prefix[left]


def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """
    นับจำนวน Subarray ที่มีผลรวมเท่ากับ k (LeetCode 560)
    แนวคิด: Prefix Sum + Hash Map {prefix_sum: frequency}
    Time: O(N)
    Space: O(N)
    """
    # กำหนด {0: 1} เพื่อรองรับกรณีที่ current_sum == k พอดี (เริ่มจาก index 0)
    prefix_counts = {0: 1}
    current_sum = 0
    total_subarrays = 0

    for num in nums:
        current_sum += num

        # ถ้าเคยมี prefix_sum ที่ทำให้ current_sum - target == k
        target = current_sum - k
        if target in prefix_counts:
            total_subarrays += prefix_counts[target]

        # บันทึกความถี่ของ current_sum ปัจจุบันลงใน Map
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    return total_subarrays


def find_max_length_equal_0_1(nums: List[int]) -> int:
    """
    หาความยาว Subarray ที่ยาวที่สุดที่มีจำนวน 0 และ 1 เท่ากัน (LeetCode 525)
    แนวคิด: มอง 0 เป็น -1 และ 1 เป็น +1
    ดังนั้น subarray ที่มี 0 และ 1 เท่ากัน จะมีผลรวมเป็น 0 พอดิบพอดี!
    ใช้ Hash Map จำ {prefix_sum: first_seen_index}
    Time: O(N)
    Space: O(N)
    """
    # จำว่า prefix sum เป็น 0 ปรากฏก่อนเริ่ม array (index -1)
    seen = {0: -1}
    current_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        # แปลง 0 เป็น -1 และ 1 เป็น +1
        current_sum += 1 if num == 1 else -1

        if current_sum in seen:
            # ถ้าเคยเจอ sum นี้มาก่อน ผลรวมระหว่างจุดเดิมกับจุดนี้คือ 0!
            max_len = max(max_len, i - seen[current_sum])
        else:
            # บันทึกเฉพาะ index แรกสุดที่เจอ เพื่อให้ได้ subarray ที่ยาวที่สุด
            seen[current_sum] = i

    return max_len


# ==========================================
# 🧪 Test Cases ตรวจสอบความถูกต้อง
# ==========================================
if __name__ == "__main__":
    print("Testing 06_prefix_sum solutions...")

    # Test 1: running_sum
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10], "Test 1 failed"

    # Test 2: NumArray
    na = NumArray([-2, 0, 3, -5, 2, -1])
    assert na.sumRange(0, 2) == 1, "Test 2.1 failed: -2 + 0 + 3 = 1"
    assert na.sumRange(2, 5) == -1, "Test 2.2 failed: 3 + (-5) + 2 + (-1) = -1"
    assert na.sumRange(0, 5) == -3, "Test 2.3 failed"

    # Test 3: subarray_sum_equals_k
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2, "Test 3.1 failed"
    assert subarray_sum_equals_k([1, 2, 3], 3) == 2, "Test 3.2 failed: [1, 2] and [3]"
    assert subarray_sum_equals_k([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4, "Test 3.3 failed"

    # Test 4: find_max_length_equal_0_1
    assert find_max_length_equal_0_1([0, 1]) == 2, "Test 4.1 failed"
    assert find_max_length_equal_0_1([0, 1, 0]) == 2, "Test 4.2 failed"
    assert find_max_length_equal_0_1([0, 1, 1, 0, 1, 1, 1, 0]) == 4, "Test 4.3 failed"

    print("[OK] All tests in 06_prefix_sum passed successfully!")
