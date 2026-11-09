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
    print("==================================================")
    print("🚀 ผลการทดสอบโค้ดของคุณ (09_dynamic_programming)")
    print("==================================================")

    # Test 1: climb_stairs
    try:
        r1_a = climb_stairs(2)
        r1_b = climb_stairs(3)
        r1_c = climb_stairs(5)
        assert r1_a == 2 and r1_b == 3 and r1_c == 8, f"Expected (2, 3, 8), got ({r1_a}, {r1_b}, {r1_c})"
        print("[Pass] โจทย์ที่ 1: climb_stairs")
        print(f"       -> บันได 2 ขั้น: {r1_a} วิธี (ถูกต้อง!)")
        print(f"       -> บันได 3 ขั้น: {r1_b} วิธี (ถูกต้อง!)")
        print(f"       -> บันได 5 ขั้น: {r1_c} วิธี (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 1: climb_stairs -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 1: {e}")

    print("--------------------------------------------------")

    # Test 2: house_robber
    try:
        houses1 = [1, 2, 3, 1]
        houses2 = [2, 7, 9, 3, 1]
        r2_a = house_robber(houses1)
        r2_b = house_robber(houses2)
        assert r2_a == 4, f"Houses {houses1} Expected 4, got {r2_a}"
        assert r2_b == 12, f"Houses {houses2} Expected 12, got {r2_b}"
        print("[Pass] โจทย์ที่ 2: house_robber")
        print(f"       -> {houses1} ได้เงินมากสุด: {r2_a} (ถูกต้อง!)")
        print(f"       -> {houses2} ได้เงินมากสุด: {r2_b} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 2: house_robber -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 2: {e}")

    print("--------------------------------------------------")

    # Test 3: coin_change
    try:
        r3_a = coin_change([1, 2, 5], 11)
        r3_b = coin_change([2], 3)
        r3_c = coin_change([1], 0)
        assert r3_a == 3, f"Expected 3, got {r3_a}"
        assert r3_b == -1, f"Expected -1, got {r3_b}"
        assert r3_c == 0, f"Expected 0, got {r3_c}"
        print("[Pass] โจทย์ที่ 3: coin_change")
        print(f"       -> coins=[1,2,5], amount=11 -> ใช้ {r3_a} เหรียญ (ถูกต้อง!)")
        print(f"       -> coins=[2], amount=3      -> ทอนไม่ได้ ({r3_b}) (ถูกต้อง!)")
        print(f"       -> coins=[1], amount=0      -> ใช้ {r3_c} เหรียญ (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 3: coin_change -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 3: {e}")

    print("--------------------------------------------------")

    # Test 4: length_of_lis
    try:
        nums_lis = [10, 9, 2, 5, 3, 7, 101, 18]
        r4 = length_of_lis(nums_lis)
        assert r4 == 4, f"Expected 4, got {r4}"
        print("[Pass] โจทย์ที่ 4: length_of_lis")
        print(f"       -> Input:         {nums_lis}")
        print(f"       -> Output ของคุณ: ความยาว LIS คือ {r4} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 4: length_of_lis -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 4: {e}")

    print("==================================================")
