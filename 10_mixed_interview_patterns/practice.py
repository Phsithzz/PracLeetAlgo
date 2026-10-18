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
    print("Testing your practice implementations in 10_mixed_interview_patterns...")

    try:
        # Test 1: product_except_self
        assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6], "Test 1 Failed"
        print("[Pass] Test 1: product_except_self")

        # Test 2: three_sum
        res2 = three_sum([-1, 0, 1, 2, -1, -4])
        norm2 = sorted([sorted(x) for x in (res2 or [])])
        assert norm2 == [[-1, -1, 2], [-1, 0, 1]], f"Test 2 Failed: got {res2}"
        print("[Pass] Test 2: three_sum")

        # Test 3: daily_temperatures
        assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0], "Test 3 Failed"
        print("[Pass] Test 3: daily_temperatures")

        # Test 4: merge_intervals
        assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]], "Test 4 Failed"
        print("[Pass] Test 4: merge_intervals")

        # Test 5: word_search
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        assert word_search(board, "ABCCED") is True, "Test 5.1 Failed"
        assert word_search(board, "SEE") is True, "Test 5.2 Failed"
        assert word_search(board, "ABCB") is False, "Test 5.3 Failed"
        print("[Pass] Test 5: word_search")

        # Test 6: top_k_frequent
        tk = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
        assert sorted(tk or []) == [1, 2], f"Test 6 Failed: got {tk}"
        print("[Pass] Test 6: top_k_frequent")

        print("\n[EXCELLENT] All tests in 10_mixed_interview_patterns passed!")
    except AssertionError as e:
        print(f"\n[FAIL] {e}")
        print("Tip: ทบทวนการวิเคราะห์โจทย์และการเลือกใช้ Pattern ใน README.md / solutions.py")
    except Exception as e:
        print(f"\n[ERROR] เกิดข้อผิดพลาด: {e}")
