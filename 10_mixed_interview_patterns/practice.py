"""
10_mixed_interview_patterns / practice.py
ไฟล์สำหรับฝึกเขียนโค้ดด้วยตัวเอง (สถานการณ์จำลองสัมภาษณ์จริง)
คำแนะนำ: อ่านโจทย์แล้ววิเคราะห์ว่าควรใช้ Pattern อะไร จากนั้นลงมือเขียนในช่อง TODO แล้วรัน 'python practice.py'
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    โจทย์ที่ 1: Product of Array Except Self (LeetCode 238)
    - คำนวณผลคูณของตัวเลขทุกตัวยกเว้น nums[i] โดยห้ามใช้การหาร
    - ข้อกำหนด: O(N) Time, O(1) Extra Space (ไม่นับ output list)
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    โจทย์ที่ 2: 3Sum (LeetCode 15)
    - หา triplet [nums[i], nums[j], nums[k]] ที่ i != j != k และ nums[i] + nums[j] + nums[k] == 0
    - ห้ามมีชุดคำตอบที่ซ้ำกัน
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    โจทย์ที่ 3: Daily Temperatures (LeetCode 739)
    - หาจำนวนวันที่ต้องรอเพื่อให้เจอวันที่อุณหภูมิอุ่นขึ้น ถ้าไม่มีวันไหนอุ่นกว่า ให้ใส่ 0
    - ตัวอย่าง [73, 74, 75, 71, 69, 72, 76, 73] -> [1, 1, 4, 2, 1, 1, 0, 0]
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    โจทย์ที่ 4: Merge Intervals (LeetCode 56)
    - รวมช่วงเวลาที่ทับซ้อนกันให้เป็นช่วงเดียว
    - ตัวอย่าง [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def word_search(board: List[List[str]], word: str) -> bool:
    """
    โจทย์ที่ 5: Word Search (LeetCode 79)
    - ค้นหาว่ามี word ในตารางตัวอักษร 2 มิติหรือไม่ (เดินได้ 4 ทิศ และห้ามใช้ตัวอักษรช่องเดิมซ้ำ)
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    โจทย์ที่ 6: Top K Frequent Elements (LeetCode 347)
    - หาเลข k ตัวที่ปรากฏบ่อยที่สุด ในเวลา O(N)
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
    print("🚀 ผลการทดสอบโค้ดของคุณ (10_mixed_interview_patterns)")
    print("==================================================")

    # Test 1: product_except_self
    try:
        sample1 = [1, 2, 3, 4]
        res1 = product_except_self(sample1)
        assert res1 == [24, 12, 8, 6], f"Expected [24, 12, 8, 6], got {res1}"
        print("[Pass] โจทย์ที่ 1: product_except_self")
        print(f"       -> Input:         {sample1}")
        print(f"       -> Output ของคุณ: {res1} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 1: product_except_self -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 1: {e}")

    print("--------------------------------------------------")

    # Test 2: three_sum
    try:
        sample2 = [-1, 0, 1, 2, -1, -4]
        res2 = three_sum(sample2)
        norm2 = sorted([sorted(x) for x in (res2 or [])])
        expected2 = sorted([[-1, -1, 2], [-1, 0, 1]])
        assert norm2 == expected2, f"Expected {expected2}, got {res2}"
        print("[Pass] โจทย์ที่ 2: three_sum")
        print(f"       -> Input:         {sample2}")
        print(f"       -> Output ของคุณ: {res2} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 2: three_sum -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 2: {e}")

    print("--------------------------------------------------")

    # Test 3: daily_temperatures
    try:
        temps = [73, 74, 75, 71, 69, 72, 76, 73]
        res3 = daily_temperatures(temps)
        assert res3 == [1, 1, 4, 2, 1, 1, 0, 0], f"Expected [1, 1, 4, 2, 1, 1, 0, 0], got {res3}"
        print("[Pass] โจทย์ที่ 3: daily_temperatures")
        print(f"       -> Temps:         {temps}")
        print(f"       -> รอวันอุ่นขึ้น: {res3} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 3: daily_temperatures -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 3: {e}")

    print("--------------------------------------------------")

    # Test 4: merge_intervals
    try:
        sample4 = [[1, 3], [2, 6], [8, 10], [15, 18]]
        res4 = merge_intervals(sample4)
        assert res4 == [[1, 6], [8, 10], [15, 18]], f"Expected [[1, 6], [8, 10], [15, 18]], got {res4}"
        print("[Pass] โจทย์ที่ 4: merge_intervals")
        print(f"       -> ก่อนรวม:       {sample4}")
        print(f"       -> Output ของคุณ: {res4} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 4: merge_intervals -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 4: {e}")

    print("--------------------------------------------------")

    # Test 5: word_search
    try:
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        r5_a = word_search(board, "ABCCED")
        r5_b = word_search(board, "SEE")
        r5_c = word_search(board, "ABCB")
        assert r5_a is True and r5_b is True and r5_c is False, "Word search result mismatch"
        print("[Pass] โจทย์ที่ 5: word_search")
        print(f"       -> หา 'ABCCED': {r5_a} (ถูกต้อง!)")
        print(f"       -> หา 'SEE'   : {r5_b} (ถูกต้อง!)")
        print(f"       -> หา 'ABCB'  : {r5_c} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 5: word_search -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 5: {e}")

    print("--------------------------------------------------")

    # Test 6: top_k_frequent
    try:
        nums6 = [1, 1, 1, 2, 2, 3]
        tk = top_k_frequent(nums6, 2)
        assert sorted(tk or []) == [1, 2], f"Expected [1, 2], got {tk}"
        print("[Pass] โจทย์ที่ 6: top_k_frequent")
        print(f"       -> nums: {nums6}, k=2")
        print(f"       -> ตัวที่เจอบ่อยสุด: {tk} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 6: top_k_frequent -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 6: {e}")

    print("==================================================")
