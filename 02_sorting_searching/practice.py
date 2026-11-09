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
    print("==================================================")
    print("🚀 ผลการทดสอบโค้ดของคุณ (02_sorting_searching)")
    print("==================================================")

    # Test 1: Bubble Sort
    try:
        arr1 = [64, 34, 25, 12, 22, 11, 90]
        before1 = list(arr1)
        res1 = bubble_sort(arr1)
        out1 = res1 if res1 is not None else arr1
        assert out1 == [11, 12, 22, 25, 34, 64, 90], f"Expected [11, 12, 22, 25, 34, 64, 90], got {out1}"
        print("[Pass] โจทย์ที่ 1: bubble_sort")
        print(f"       -> ก่อนเรียง:     {before1}")
        print(f"       -> Output ของคุณ: {out1} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 1: bubble_sort -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 1: {e}")

    print("--------------------------------------------------")

    # Test 2: Selection Sort
    try:
        arr2 = [29, 10, 14, 37, 13]
        before2 = list(arr2)
        res2 = selection_sort(arr2)
        out2 = res2 if res2 is not None else arr2
        assert out2 == [10, 13, 14, 29, 37], f"Expected [10, 13, 14, 29, 37], got {out2}"
        print("[Pass] โจทย์ที่ 2: selection_sort")
        print(f"       -> ก่อนเรียง:     {before2}")
        print(f"       -> Output ของคุณ: {out2} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 2: selection_sort -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 2: {e}")

    print("--------------------------------------------------")

    # Test 3: Insertion Sort
    try:
        arr3 = [12, 11, 13, 5, 6]
        before3 = list(arr3)
        res3 = insertion_sort(arr3)
        out3 = res3 if res3 is not None else arr3
        assert out3 == [5, 6, 11, 12, 13], f"Expected [5, 6, 11, 12, 13], got {out3}"
        print("[Pass] โจทย์ที่ 3: insertion_sort")
        print(f"       -> ก่อนเรียง:     {before3}")
        print(f"       -> Output ของคุณ: {out3} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 3: insertion_sort -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 3: {e}")

    print("--------------------------------------------------")

    # Test 4: Counting Sort
    try:
        arr4 = [4, 2, 2, 8, 3, 3, 1]
        before4 = list(arr4)
        res4 = counting_sort(arr4)
        out4 = res4 if res4 is not None else arr4
        assert out4 == [1, 2, 2, 3, 3, 4, 8], f"Expected [1, 2, 2, 3, 3, 4, 8], got {out4}"
        print("[Pass] โจทย์ที่ 4: counting_sort")
        print(f"       -> ก่อนเรียง:     {before4}")
        print(f"       -> Output ของคุณ: {out4} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 4: counting_sort -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 4: {e}")

    print("--------------------------------------------------")

    # Test 5: Binary Search
    try:
        sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
        res5_a = binary_search(sorted_arr, 23)
        res5_b = binary_search(sorted_arr, 50)
        assert res5_a == 5, f"หา 23 Expected 5, got {res5_a}"
        assert res5_b == -1, f"หา 50 Expected -1, got {res5_b}"
        print("[Pass] โจทย์ที่ 5: binary_search")
        print(f"       -> nums: {sorted_arr}")
        print(f"       -> ค้นหา 23 ได้ index: {res5_a} (ถูกต้อง!)")
        print(f"       -> ค้นหา 50 ได้ index: {res5_b} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 5: binary_search -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 5: {e}")

    print("--------------------------------------------------")

    # Test 6: Binary Search Left Bound
    try:
        repeated_arr = [1, 2, 4, 4, 4, 4, 5, 9]
        res6_a = binary_search_left_bound(repeated_arr, 4)
        res6_b = binary_search_left_bound(repeated_arr, 7)
        assert res6_a == 2, f"หา 4 ตัวแรก Expected index 2, got {res6_a}"
        assert res6_b == -1, f"หา 7 Expected -1, got {res6_b}"
        print("[Pass] โจทย์ที่ 6: binary_search_left_bound")
        print(f"       -> nums: {repeated_arr}")
        print(f"       -> ตำแหน่งแรกของ 4 คือ index: {res6_a} (ถูกต้อง!)")
        print(f"       -> ตำแหน่งแรกของ 7 คือ index: {res6_b} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 6: binary_search_left_bound -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 6: {e}")

    print("==================================================")
