"""
09_dynamic_programming / practice.py
ไฟล์สำหรับฝึกเขียนโค้ดด้วยตัวเอง
คำแนะนำ: เขียนโค้ดในช่อง TODO โดยไม่เปิดดูเฉลย แล้วรัน 'python practice.py' เพื่อตรวจสอบ
"""

from typing import List


def climb_stairs(n: int) -> int:
    """
    โจทย์ที่ 1: Climbing Stairs (LeetCode 70)
    - แต่ละครั้งก้าวได้ 1 หรือ 2 ขั้น มีกี่วิธีในการขึ้นถึงขั้นที่ n
    - คำใบ้: วิธีขึ้นถึงขั้นที่ i คือ วิธีขึ้นถึงขั้นที่ i-1 บวกกับ ขั้นที่ i-2
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def house_robber(nums: List[int]) -> int:
    """
    โจทย์ที่ 2: House Robber (LeetCode 198)
    - หาเงินมากที่สุดโดยห้ามขโมยสองหลังติดกัน
    - ทางเลือก: max(ขโมยหลังนี้ + ผลรวมก่อนหน้าสองหลัง, ข้ามหลังนี้ + ผลรวมหลังก่อนหน้า)
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def coin_change(coins: List[int], amount: int) -> int:
    """
    โจทย์ที่ 3: Coin Change (LeetCode 322)
    - หาจำนวนเหรียญที่น้อยที่สุดที่รวมได้เท่ากับ amount (ถ้าเป็นไปไม่ได้คืนค่า -1)
    - DP state: dp[a] = min(dp[a], 1 + dp[a - coin])
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def length_of_lis(nums: List[int]) -> int:
    """
    โจทย์ที่ 4: Longest Increasing Subsequence (LeetCode 300)
    - หาความยาวของ Subsequence ที่ตัวเลขเรียงจากน้อยไปมากที่ยาวที่สุด
    - ให้ dp[i] = 1 เริ่มต้น แล้ววนลูปดู j < i ทั้งหมด
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


# ==========================================
# 🧪 Test Cases ตรวจสอบผลลัพธ์
# ==========================================
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    print("Testing your practice implementations in 09_dynamic_programming...")

    try:
        # Test 1: climb_stairs
        assert climb_stairs(2) == 2, "Test 1.1 Failed"
        assert climb_stairs(3) == 3, "Test 1.2 Failed"
        assert climb_stairs(5) == 8, "Test 1.3 Failed"
        print("[Pass] Test 1: climb_stairs")

        # Test 2: house_robber
        assert house_robber([1, 2, 3, 1]) == 4, "Test 2.1 Failed"
        assert house_robber([2, 7, 9, 3, 1]) == 12, "Test 2.2 Failed"
        print("[Pass] Test 2: house_robber")

        # Test 3: coin_change
        assert coin_change([1, 2, 5], 11) == 3, "Test 3.1 Failed"
        assert coin_change([2], 3) == -1, "Test 3.2 Failed"
        assert coin_change([1], 0) == 0, "Test 3.3 Failed"
        print("[Pass] Test 3: coin_change")

        # Test 4: length_of_lis
        assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4, "Test 4.1 Failed"
        assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4, "Test 4.2 Failed"
        assert length_of_lis([7, 7, 7, 7, 7]) == 1, "Test 4.3 Failed"
        print("[Pass] Test 4: length_of_lis")

        print("\n[EXCELLENT] All tests in 09_dynamic_programming passed!")
    except AssertionError as e:
        print(f"\n[FAIL] {e}")
        print("Tip: ตรวจสอบ State Definition และ Base Case ใน README.md / solutions.py")
    except Exception as e:
        print(f"\n[ERROR] เกิดข้อผิดพลาด: {e}")
