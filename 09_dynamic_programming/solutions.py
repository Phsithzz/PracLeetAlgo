"""
09_dynamic_programming / solutions.py
เฉลยตัวอย่างโค้ดที่ถูกต้องและสะอาด สำหรับ Dynamic Programming Patterns
"""

from typing import List


def climb_stairs(n: int) -> int:
    """
    จำนวนวิธีปีนบันได n ขั้น (ก้าวละ 1 หรือ 2 ขั้น) (LeetCode 70)
    State: dp[i] = จำนวนวิธีปีนบันได i ขั้น
    Transition: dp[i] = dp[i-1] + dp[i-2]
    Time: O(N)
    Space: O(1) (ใช้ตัวแปร 2 ตัว prev1, prev2)
    """
    if n <= 2:
        return n

    prev2 = 1  # 1 ขั้น: 1 วิธี
    prev1 = 2  # 2 ขั้น: 2 วิธี

    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


def house_robber(nums: List[int]) -> int:
    """
    House Robber (LeetCode 198): ขโมยบ้านโดยห้ามขโมยสองหลังติดกัน
    State: dp[i] = เงินมากที่สุดที่ได้จากการพิจารณาบ้านถึงหลังที่ i
    Transition: dp[i] = max(ขโมยหลังนี้ + dp[i-2], ไม่ขโมยหลังนี้ + dp[i-1])
    Time: O(N)
    Space: O(1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2 = 0
    prev1 = 0

    for num in nums:
        # ทางเลือกระหว่าง (ขโมยบ้านหลังนี้ + เงินที่ได้ก่อนหน้า 2 หลัง) เทียบกับ (ข้ามบ้านหลังนี้)
        curr = max(prev2 + num, prev1)
        prev2 = prev1
        prev1 = curr

    return prev1


def coin_change(coins: List[int], amount: int) -> int:
    """
    Coin Change (LeetCode 322): หาจำนวนเหรียญน้อยที่สุดที่รวมได้เท่ากับ amount
    State: dp[a] = จำนวนเหรียญน้อยที่สุดที่ทอนเงินมูลค่า a ได้
    Transition: dp[a] = min(dp[a], 1 + dp[a - coin])
    Time: O(amount * len(coins))
    Space: O(amount)
    """
    # กำหนดค่าเริ่มต้นด้วยค่าที่เป็นไปไม่ได้ (amount + 1)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # เงิน 0 บาท ใช้ 0 เหรียญ

    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])

    return dp[amount] if dp[amount] != amount + 1 else -1


def length_of_lis(nums: List[int]) -> int:
    """
    Longest Increasing Subsequence (LeetCode 300)
    State: dp[i] = ความยาว LIS ที่สิ้นสุดที่ index i
    Transition: dp[i] = max(1 + dp[j]) สำหรับทุก j < i ที่ nums[j] < nums[i]
    Time: O(N^2) (สามารถปรับเป็น O(N log N) ด้วย Binary Search)
    Space: O(N)
    """
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)


# ==========================================
# 🧪 Test Cases ตรวจสอบความถูกต้อง
# ==========================================
if __name__ == "__main__":
    print("Testing 09_dynamic_programming solutions...")

    # Test 1: climb_stairs
    assert climb_stairs(2) == 2, "Test 1.1 failed"
    assert climb_stairs(3) == 3, "Test 1.2 failed"
    assert climb_stairs(5) == 8, "Test 1.3 failed"

    # Test 2: house_robber
    assert house_robber([1, 2, 3, 1]) == 4, "Test 2.1 failed: rob house 0 and 2 -> 1 + 3 = 4"
    assert house_robber([2, 7, 9, 3, 1]) == 12, "Test 2.2 failed: 2 + 9 + 1 = 12"

    # Test 3: coin_change
    assert coin_change([1, 2, 5], 11) == 3, "Test 3.1 failed: 5 + 5 + 1"
    assert coin_change([2], 3) == -1, "Test 3.2 failed: impossible"
    assert coin_change([1], 0) == 0, "Test 3.3 failed"

    # Test 4: length_of_lis
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4, "Test 4.1 failed: [2, 3, 7, 101]"
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4, "Test 4.2 failed: [0, 1, 2, 3]"
    assert length_of_lis([7, 7, 7, 7, 7]) == 1, "Test 4.3 failed"

    print("[OK] All tests in 09_dynamic_programming passed successfully!")
