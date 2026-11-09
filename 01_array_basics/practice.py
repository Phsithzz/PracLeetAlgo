"""
01_array_basics / practice.py
ไฟล์สำหรับฝึกเขียนโค้ดด้วยตัวเอง
คำแนะนำ: ลองเขียนโค้ดด้วยตัวเองโดยไม่เปิดดู solutions.py แล้วรัน 'python practice.py' เพื่อตรวจสอบ
"""

from typing import List, Tuple


def find_max_min(nums: List[int]) -> Tuple[int, int]:
    """
    โจทย์ที่ 1: หาค่าสูงสุดและต่ำสุดใน Array ในการวนลูปเที่ยวเดียว
    - Input: nums เช่น [3, 7, 2, 9, 1, 5]
    - Output: tuple (max_val, min_val) เช่น (9, 1)
    - เงื่อนไข: ห้ามใช้ฟังก์ชันสำเร็จรูป max() หรือ min()
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def reverse_array_inplace(nums: List[int]) -> None:
    """
    โจทย์ที่ 2: กลับด้าน Array แบบ In-place (ห้ามสร้าง list ใหม่)
    - Input: nums เช่น [1, 2, 3, 4, 5]
    - แก้ไข nums ให้กลายเป็น [5, 4, 3, 2, 1]
    - เงื่อนไข: ใช้ Two Pointers ฝั่งซ้ายและขวา สลับค่าเข้าหากัน
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def move_zeroes(nums: List[int]) -> None:
    """
    โจทย์ที่ 3: ย้ายเลข 0 ทั้งหมดไปไว้ท้าย Array โดยคงลำดับเดิมของตัวเลขอื่นไว้ (LeetCode 283)
    - Input: nums เช่น [0, 1, 0, 3, 12]
    - ผลลัพธ์: nums ถูกแก้ไขเป็น [1, 3, 12, 0, 0]
    - เงื่อนไข: In-place O(1) space
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def rotate_array(nums: List[int], k: int) -> None:
    """
    โจทย์ที่ 4: หมุน Array ไปทางขวา k ตำแหน่ง แบบ In-place (LeetCode 189)
    - Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    - ผลลัพธ์: nums กลายเป็น [5, 6, 7, 1, 2, 3, 4]
    - คำใบ้: ใช้วิธี Reverse 3 จังหวะ (ทั้งก้อน, k ตัวแรก, ตัวที่เหลือ)
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
    print("🚀 ผลการทดสอบโค้ดของคุณ (Your Practice Results)")
    print("==================================================")

    # Test 1: find_max_min
    try:
        sample1 = [3, 7, 2, 9, 1, 5]
        res1 = find_max_min(sample1)
        assert res1 == (9, 1), f"Expected (9, 1), got {res1}"
        print("[Pass] โจทย์ที่ 1: find_max_min")
        print(f"       -> Input:         {sample1}")
        print(f"       -> Output ของคุณ: {res1} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 1: find_max_min -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 1: {e}")

    print("--------------------------------------------------")

    # Test 2: reverse_array_inplace
    try:
        sample2 = [1, 2, 3, 4, 5]
        before2 = list(sample2)
        reverse_array_inplace(sample2)
        assert sample2 == [5, 4, 3, 2, 1], f"Expected [5, 4, 3, 2, 1], got {sample2}"
        print("[Pass] โจทย์ที่ 2: reverse_array_inplace")
        print(f"       -> ก่อนกลับด้าน:  {before2}")
        print(f"       -> Output ของคุณ: {sample2} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 2: reverse_array_inplace -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 2: {e}")

    print("--------------------------------------------------")

    # Test 3: move_zeroes
    try:
        sample3 = [0, 1, 0, 3, 12]
        before3 = list(sample3)
        move_zeroes(sample3)
        assert sample3 == [1, 3, 12, 0, 0], f"Expected [1, 3, 12, 0, 0], got {sample3}"
        print("[Pass] โจทย์ที่ 3: move_zeroes")
        print(f"       -> ก่อนย้ายเลข 0: {before3}")
        print(f"       -> Output ของคุณ: {sample3} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 3: move_zeroes (ยังไม่ได้เขียน หรือคำตอบยังไม่ตรง)")
        print(f"       -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 3: {e}")

    print("--------------------------------------------------")

    # Test 4: rotate_array
    try:
        sample4 = [1, 2, 3, 4, 5, 6, 7]
        before4 = list(sample4)
        rotate_array(sample4, 3)
        assert sample4 == [5, 6, 7, 1, 2, 3, 4], f"Expected [5, 6, 7, 1, 2, 3, 4], got {sample4}"
        print("[Pass] โจทย์ที่ 4: rotate_array")
        print(f"       -> ก่อนหมุน:      {before4}")
        print(f"       -> Output ของคุณ: {sample4} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 4: rotate_array (ยังไม่ได้เขียน หรือคำตอบยังไม่ตรง)")
        print(f"       -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 4: {e}")

    print("==================================================")
