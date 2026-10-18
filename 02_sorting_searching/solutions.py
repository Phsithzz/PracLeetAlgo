"""
02_sorting_searching / solutions.py
เฉลยตัวอย่างโค้ดที่ถูกต้องและสะอาด สำหรับ Sorting & Searching Algorithms
"""

from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    """
    Bubble Sort: เปรียบเทียบคู่ติดกันแล้วสลับ พร้อม Early Exit Flag
    Time: O(N) Best, O(N^2) Worst
    Space: O(1) In-place
    """
    n = len(nums)
    for i in range(n):
        swapped = False
        # ตัวท้ายสุด i ตัวจะเรียงเรียบร้อยแล้ว จึงไม่ต้องตรวจซ้ำ
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        # ถ้าไม่มีการสลับเลย แสดงว่าเรียงเสร็จแล้ว หยุดได้ทันที
        if not swapped:
            break
    return nums


def selection_sort(nums: List[int]) -> List[int]:
    """
    Selection Sort: วนหาค่าน้อยสุดในส่วนที่ยังไม่เรียง แล้วนำมาวางไว้หน้าสุด
    Time: O(N^2)
    Space: O(1) In-place
    """
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        # สลับค่าน้อยสุดมาไว้ที่ตำแหน่ง i
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


def insertion_sort(nums: List[int]) -> List[int]:
    """
    Insertion Sort: หยิบสมาชิกทีละตัว แล้วแทรกเข้าไปในตำแหน่งที่ถูกต้องของฝั่งซ้ายที่เรียงแล้ว
    Time: O(N) Best, O(N^2) Worst
    Space: O(1) In-place
    """
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        # เลื่อนสมาชิกฝั่งซ้ายที่มากกว่า key ไปทางขวา 1 ตำแหน่ง
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


def counting_sort(nums: List[int]) -> List[int]:
    """
    Counting Sort: นับความถี่ของตัวเลข เหมาะกับเลขจำนวนเต็มช่วงแคบๆ
    Time: O(N + K) โดย K คือช่วงของตัวเลข (max - min + 1)
    Space: O(K)
    """
    if not nums:
        return nums

    min_val = min(nums)
    max_val = max(nums)
    range_k = max_val - min_val + 1

    counts = [0] * range_k
    for num in nums:
        counts[num - min_val] += 1

    # สร้างผลลัพธ์กลับคืนใส่ nums
    idx = 0
    for offset, count in enumerate(counts):
        val = offset + min_val
        for _ in range(count):
            nums[idx] = val
            idx += 1

    return nums


def binary_search(nums: List[int], target: int) -> int:
    """
    Binary Search มาตรฐาน: ค้นหา target ใน Sorted Array
    Time: O(log N)
    Space: O(1)
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_left_bound(nums: List[int], target: int) -> int:
    """
    Binary Search หา Left Boundary: หาตำแหน่งแรกสุดของ target กรณีมีเลขซ้ำ
    Time: O(log N)
    Space: O(1)
    """
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            result = mid
            right = mid - 1  # ยังไม่หยุด บีบขอบขวาเข้ามาหาฝั่งซ้ายต่อ
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


# ==========================================
# 🧪 Test Cases ตรวจสอบความถูกต้อง
# ==========================================
if __name__ == "__main__":
    print("Testing 02_sorting_searching solutions...")

    # Test 1: Bubble Sort
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    assert bubble_sort(arr1) == [11, 12, 22, 25, 34, 64, 90], "Test 1 failed: bubble_sort"

    # Test 2: Selection Sort
    arr2 = [29, 10, 14, 37, 13]
    assert selection_sort(arr2) == [10, 13, 14, 29, 37], "Test 2 failed: selection_sort"

    # Test 3: Insertion Sort
    arr3 = [12, 11, 13, 5, 6]
    assert insertion_sort(arr3) == [5, 6, 11, 12, 13], "Test 3 failed: insertion_sort"

    # Test 4: Counting Sort
    arr4 = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(arr4) == [1, 2, 2, 3, 3, 4, 8], "Test 4 failed: counting_sort"

    # Test 5: Binary Search
    sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    assert binary_search(sorted_arr, 23) == 5, "Test 5 failed: binary_search found"
    assert binary_search(sorted_arr, 50) == -1, "Test 5 failed: binary_search not found"

    # Test 6: Binary Search Left Bound
    repeated_arr = [1, 2, 4, 4, 4, 4, 5, 9]
    assert binary_search_left_bound(repeated_arr, 4) == 2, "Test 6 failed: left bound"
    assert binary_search_left_bound(repeated_arr, 7) == -1, "Test 6 failed: left bound not found"

    print("[OK] All tests in 02_sorting_searching passed successfully!")
