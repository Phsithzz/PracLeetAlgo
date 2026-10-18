"""
02_sorting_searching / practice.py
ไฟล์สำหรับฝึกเขียนโค้ดด้วยตัวเอง
คำแนะนำ: เขียนโค้ดในช่อง TODO โดยไม่เปิดดูเฉลย แล้วรัน 'python practice.py' เพื่อตรวจสอบ
"""

from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    """
    โจทย์ที่ 1: เขียน Bubble Sort (In-place) พร้อม Swapped Flag เพื่อหยุดลูปก่อนกำหนดถ้าข้อมูลเรียงแล้ว
    - เปรียบเทียบคู่ติดกัน nums[j] กับ nums[j+1]
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def selection_sort(nums: List[int]) -> List[int]:
    """
    โจทย์ที่ 2: เขียน Selection Sort (In-place)
    - วนหา index ของค่าน้อยที่สุดในส่วนที่เหลือ แล้วสลับกับตำแหน่งปัจจุบัน
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def insertion_sort(nums: List[int]) -> List[int]:
    """
    โจทย์ที่ 3: เขียน Insertion Sort (In-place)
    - วนหยิบ key และเลื่อนตัวทางซ้ายที่มากกว่า key ไปทางขวา
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def counting_sort(nums: List[int]) -> List[int]:
    """
    โจทย์ที่ 4: เขียน Counting Sort สำหรับเลขจำนวนเต็ม
    - สร้าง array counts สำหรับนับความถี่ แล้วนำกลับมาเขียนทับ nums
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def binary_search(nums: List[int], target: int) -> int:
    """
    โจทย์ที่ 5: เขียน Binary Search มาตรฐาน
    - ข้อมูล nums เรียงจากน้อยไปมากแล้ว
    - คืนค่า index ของ target ถ้าพบ หรือคืนค่า -1 ถ้าไม่พบ
    - ข้อกำหนด: O(log N) Time Complexity
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def binary_search_left_bound(nums: List[int], target: int) -> int:
    """
    โจทย์ที่ 6: เขียน Binary Search หาตำแหน่งแรกสุด (Leftmost Index) ของ target ในกรณีมีตัวเลขซ้ำกัน
    - ตัวอย่าง nums = [1, 2, 4, 4, 4, 4, 5, 9], target = 4 -> คืนค่า index 2
    - คืนค่า -1 ถ้าไม่พบ
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


# ==========================================
# 🧪 Test Cases ตรวจสอบผลลัพธ์
# ==========================================
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    print("Testing your practice implementations in 02_sorting_searching...")

    try:
        # Test 1: Bubble Sort
        arr1 = [64, 34, 25, 12, 22, 11, 90]
        res1 = bubble_sort(arr1)
        assert res1 == [11, 12, 22, 25, 34, 64, 90], f"Test 1 Failed: {res1}"
        print("[Pass] Test 1: bubble_sort")

        # Test 2: Selection Sort
        arr2 = [29, 10, 14, 37, 13]
        res2 = selection_sort(arr2)
        assert res2 == [10, 13, 14, 29, 37], f"Test 2 Failed: {res2}"
        print("[Pass] Test 2: selection_sort")

        # Test 3: Insertion Sort
        arr3 = [12, 11, 13, 5, 6]
        res3 = insertion_sort(arr3)
        assert res3 == [5, 6, 11, 12, 13], f"Test 3 Failed: {res3}"
        print("[Pass] Test 3: insertion_sort")

        # Test 4: Counting Sort
        arr4 = [4, 2, 2, 8, 3, 3, 1]
        res4 = counting_sort(arr4)
        assert res4 == [1, 2, 2, 3, 3, 4, 8], f"Test 4 Failed: {res4}"
        print("[Pass] Test 4: counting_sort")

        # Test 5: Binary Search
        sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
        assert binary_search(sorted_arr, 23) == 5, "Test 5 Failed: target 23"
        assert binary_search(sorted_arr, 50) == -1, "Test 5 Failed: target 50"
        print("[Pass] Test 5: binary_search")

        # Test 6: Binary Search Left Bound
        repeated_arr = [1, 2, 4, 4, 4, 4, 5, 9]
        assert binary_search_left_bound(repeated_arr, 4) == 2, "Test 6 Failed: target 4"
        assert binary_search_left_bound(repeated_arr, 7) == -1, "Test 6 Failed: target 7"
        print("[Pass] Test 6: binary_search_left_bound")

        print("\n[EXCELLENT] All tests in 02_sorting_searching passed!")
    except AssertionError as e:
        print(f"\n[FAIL] {e}")
        print("Tip: ทบทวนเงื่อนไขขอบเขต (Boundary) และการอัปเดต pointer ใน README.md / solutions.py")
    except Exception as e:
        print(f"\n[ERROR] เกิดข้อผิดพลาด: {e}")
