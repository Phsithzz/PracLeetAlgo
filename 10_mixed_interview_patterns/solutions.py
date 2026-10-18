"""
10_mixed_interview_patterns / solutions.py
เฉลยตัวอย่างโค้ดที่ถูกต้องและสะอาด สำหรับโจทย์คละสไตล์ Technical Interview จริง
พร้อมคำอธิบายการระบุ Pattern (Pattern Deduction) ในแต่ละข้อ
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    โจทย์ที่ 1: ผลคูณของสมาชิกทุกตัวยกเว้นตัวเอง โดยห้ามใช้การหาร (LeetCode 238)
    ---------------------------------------------------------
    🔍 วิธีแกะ Pattern:
       ผลคูณของทุกตัวยกเว้น nums[i] = (ผลคูณฝั่งซ้ายของ i) * (ผลคูณฝั่งขวาของ i)
       นี่คือรูปแบบ [Prefix / Suffix Accumulation]
    Time: O(N)
    Space: O(1) ไม่นับ Output Array
    """
    n = len(nums)
    res = [1] * n

    # สะสมผลคูณจากฝั่งซ้าย (Prefix Product)
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    # สะสมผลคูณจากฝั่งขวา (Suffix Product) คูณทับเข้าไป
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    โจทย์ที่ 2: หาเลข 3 ตัวที่บวกกันได้ 0 (LeetCode 15)
    ---------------------------------------------------------
    🔍 วิธีแกะ Pattern:
       ต้องการหา a + b + c = 0 หรือ b + c = -a
       เมื่อ Sort Array แล้ว ปัญหานี้จะลดรูปลงเหลือ [Two Pointers] บน Sorted Array
    Time: O(N^2)
    Space: O(1) หรือ O(N) จากการ sort
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        # ข้ามตัวซ้ำตัวแรก
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        left = i + 1
        right = n - 1

        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                # ข้ามตัวซ้ำของ left และ right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif two_sum < target:
                left += 1
            else:
                right -= 1

    return result


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    โจทย์ที่ 3: ต้องรอกี่วันกว่าจะเจอวันที่อุณหภูมิอุ่นกว่า (LeetCode 739)
    ---------------------------------------------------------
    🔍 วิธีแกะ Pattern:
       โจทย์ถามหา "สมาชิกตัวถัดไปที่มากกว่า" (Next Greater Element)
       นี่คือสัญญาณเตือนของ [Monotonic Decreasing Stack] โดยตรง!
    Time: O(N)
    Space: O(N)
    """
    n = len(temperatures)
    ans = [0] * n
    stack = []  # เก็บ index ของวันที่อุณหภูมิยังไม่เจอวันที่อุ่นกว่า

    for curr_day, curr_temp in enumerate(temperatures):
        # ถ้าอุณหภูมิวันนี้ ร้อนกว่าวันที่อยู่บนยอด Stack -> เคลียร์ยอด Stack
        while stack and curr_temp > temperatures[stack[-1]]:
            prev_day = stack.pop()
            ans[prev_day] = curr_day - prev_day
        stack.append(curr_day)

    return ans


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    โจทย์ที่ 4: รวมช่วงเวลาที่ทับซ้อนกัน (LeetCode 56)
    ---------------------------------------------------------
    🔍 วิธีแกะ Pattern:
       การจัดการช่วงเวลา (Intervals) ให้เรียงลำดับตามจุดเริ่มต้น (Start Time) ก่อนเสมอ
       จากนั้นตรวจดูว่าจุดเริ่มต้นของช่วงใหม่ <= จุดสิ้นสุดของช่วงปัจจุบันหรือไม่
    Time: O(N log N)
    Space: O(N)
    """
    if not intervals:
        return []

    # เรียงลำดับตาม start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        prev = merged[-1]
        # ถ้าเริ่มทับซ้อนกัน (current.start <= prev.end)
        if current[0] <= prev[1]:
            # ขยายขอบเขตสิ้นสุดให้ครอบคลุม
            prev[1] = max(prev[1], current[1])
        else:
            # ไม่ทับซ้อน เพิ่มเป็นช่วงใหม่
            merged.append(current)

    return merged


def word_search(board: List[List[str]], word: str) -> bool:
    """
    โจทย์ที่ 5: ค้นหาคำศัพท์ในตาราง 2 มิติ (LeetCode 79)
    ---------------------------------------------------------
    🔍 วิธีแกะ Pattern:
       เดินสำรวจ 4 ทิศ และห้ามใช้ตัวอักษรเดิมซ้ำในคำเดียวกัน
       นี่คือ [Grid DFS with Backtracking]
    Time: O(M * N * 3^L) โดย L คือความยาว word
    Space: O(L)
    """
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, idx: int) -> bool:
        # เจอตัวอักษรครบทุกตัวแล้ว
        if idx == len(word):
            return True

        # ออกนอกตาราง หรือตัวอักษรไม่ตรง
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False

        # Choose: ทำเครื่องหมายว่ามาเยือนแล้ว
        temp = board[r][c]
        board[r][c] = "#"

        # Explore: สำรวจ 4 ทิศ
        found = (
            dfs(r + 1, c, idx + 1)
            or dfs(r - 1, c, idx + 1)
            or dfs(r, c + 1, idx + 1)
            or dfs(r, c - 1, idx + 1)
        )

        # Unchoose: คืนค่าตัวอักษรเดิมเพื่อลองทางอื่น (Backtrack)
        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True

    return False


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    โจทย์ที่ 6: หาเลข k ตัวที่ปรากฏบ่อยที่สุด ในเวลา O(N) (LeetCode 347)
    ---------------------------------------------------------
    🔍 วิธีแกะ Pattern:
       นับความถี่ด้วย Hash Map แล้วจัดกลุ่มด้วย [Bucket Sort]
       โดยใช้ "ความถี่" เป็น Index ของ Bucket (ความถี่มีได้ตั้งแต่ 0 ถึง N)
    Time: O(N)
    Space: O(N)
    """
    # 1. นับความถี่
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # 2. Bucket Sort: bucket[freq] = list ของตัวเลขที่มีความถี่เท่ากับ freq
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)

    # 3. หยิบจากความถี่มากสุดย้อนลงมา
    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result

    return result


# ==========================================
# 🧪 Test Cases ตรวจสอบความถูกต้อง
# ==========================================
if __name__ == "__main__":
    print("Testing 10_mixed_interview_patterns solutions...")

    # Test 1: product_except_self
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6], "Test 1 failed"
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0], "Test 1.2 failed"

    # Test 2: three_sum
    res2 = three_sum([-1, 0, 1, 2, -1, -4])
    norm2 = sorted([sorted(x) for x in res2])
    assert norm2 == [[-1, -1, 2], [-1, 0, 1]], f"Test 2 failed: {res2}"

    # Test 3: daily_temperatures
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0], "Test 3 failed"

    # Test 4: merge_intervals
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]], "Test 4 failed"

    # Test 5: word_search
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert word_search(board, "ABCCED") is True, "Test 5.1 failed"
    assert word_search(board, "SEE") is True, "Test 5.2 failed"
    assert word_search(board, "ABCB") is False, "Test 5.3 failed"

    # Test 6: top_k_frequent
    tk = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    assert sorted(tk) == [1, 2], f"Test 6 failed: {tk}"

    print("[OK] All tests in 10_mixed_interview_patterns passed successfully!")
