"""
03_hashmap_set / practice.py
ไฟล์สำหรับฝึกเขียนโค้ดด้วยตัวเอง
คำแนะนำ: เขียนโค้ดในช่อง TODO โดยไม่เปิดดูเฉลย แล้วรัน 'python practice.py' เพื่อตรวจสอบ
"""

from typing import Dict, List, Any
from collections import defaultdict


def frequency_counter(items: List[Any]) -> Dict[Any, int]:
    """
    โจทย์ที่ 1: เขียนฟังก์ชันนับความถี่ของสมาชิกแต่ละตัวใน List
    - ตัวอย่าง items = ["apple", "banana", "apple"] -> {"apple": 2, "banana": 1}
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def has_duplicate(nums: List[int]) -> bool:
    """
    โจทย์ที่ 2: ตรวจสอบว่าใน Array มีตัวเลขซ้ำหรือไม่ (LeetCode 217)
    - คืนค่า True ถ้ามีตัวเลขซ้ำอย่างน้อย 1 ตัว, คืนค่า False ถ้าทุกตัวไม่ซ้ำเลย
    - เงื่อนไข: ใช้ Set เพื่อให้ได้ Time O(N)
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    โจทย์ที่ 3: ค้นหา Index ของเลขสองตัวที่บวกกันได้ target (LeetCode 1)
    - ตัวอย่าง nums = [2, 7, 11, 15], target = 9 -> [0, 1]
    - เงื่อนไข: Time O(N) โดยใช้ Dict เก็บ complement (target - num)
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def is_anagram(s: str, t: str) -> bool:
    """
    โจทย์ที่ 4: ตรวจสอบว่า t เป็น Anagram ของ s หรือไม่ (LeetCode 242)
    - Anagram คือคำที่มีตัวอักษรเหมือนกันและจำนวนเท่ากันเป๊ะ แต่เรียงสลับที่กันได้
    - ตัวอย่าง s = "anagram", t = "nagaram" -> True
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    โจทย์ที่ 5: จัดกลุ่มคำที่เป็น Anagram กัน (LeetCode 49)
    - ตัวอย่าง strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    - ผลลัพธ์: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]] (ลำดับกลุ่มไม่สำคัญ)
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


# ==========================================
# 🧪 Test Cases ตรวจสอบผลลัพธ์
# ==========================================
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    print("Testing your practice implementations in 03_hashmap_set...")

    try:
        # Test 1: frequency_counter
        items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
        res1 = frequency_counter(items)
        assert res1 == {"apple": 3, "banana": 2, "cherry": 1}, f"Test 1 Failed: {res1}"
        print("[Pass] Test 1: frequency_counter")

        # Test 2: has_duplicate
        assert has_duplicate([1, 2, 3, 1]) is True, "Test 2.1 Failed"
        assert has_duplicate([1, 2, 3, 4]) is False, "Test 2.2 Failed"
        print("[Pass] Test 2: has_duplicate")

        # Test 3: two_sum
        assert two_sum([2, 7, 11, 15], 9) == [0, 1], "Test 3.1 Failed"
        assert two_sum([3, 2, 4], 6) == [1, 2], "Test 3.2 Failed"
        print("[Pass] Test 3: two_sum")

        # Test 4: is_anagram
        assert is_anagram("anagram", "nagaram") is True, "Test 4.1 Failed"
        assert is_anagram("rat", "car") is False, "Test 4.2 Failed"
        print("[Pass] Test 4: is_anagram")

        # Test 5: group_anagrams
        raw_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        res_groups = group_anagrams(raw_words)
        normalized = sorted([sorted(g) for g in (res_groups or [])])
        expected = sorted([["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])
        assert normalized == expected, f"Test 5 Failed: got {normalized}"
        print("[Pass] Test 5: group_anagrams")

        print("\n[EXCELLENT] All tests in 03_hashmap_set passed!")
    except AssertionError as e:
        print(f"\n[FAIL] {e}")
        print("Tip: ทบทวนการใช้ dict.get() หรือ complement ใน README.md / solutions.py")
    except Exception as e:
        print(f"\n[ERROR] เกิดข้อผิดพลาด: {e}")
