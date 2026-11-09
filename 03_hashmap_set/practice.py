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
    print("==================================================")
    print("🚀 ผลการทดสอบโค้ดของคุณ (03_hashmap_set)")
    print("==================================================")

    # Test 1: frequency_counter
    try:
        items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
        res1 = frequency_counter(items)
        assert res1 == {"apple": 3, "banana": 2, "cherry": 1}, f"Expected {{'apple': 3, 'banana': 2, 'cherry': 1}}, got {res1}"
        print("[Pass] โจทย์ที่ 1: frequency_counter")
        print(f"       -> Items:         {items}")
        print(f"       -> Output ของคุณ: {res1} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 1: frequency_counter -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 1: {e}")

    print("--------------------------------------------------")

    # Test 2: has_duplicate
    try:
        res2_a = has_duplicate([1, 2, 3, 1])
        res2_b = has_duplicate([1, 2, 3, 4])
        assert res2_a is True, f"Array [1,2,3,1] Expected True, got {res2_a}"
        assert res2_b is False, f"Array [1,2,3,4] Expected False, got {res2_b}"
        print("[Pass] โจทย์ที่ 2: has_duplicate")
        print(f"       -> [1, 2, 3, 1] ผลลัพธ์: {res2_a} (ถูกต้อง!)")
        print(f"       -> [1, 2, 3, 4] ผลลัพธ์: {res2_b} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 2: has_duplicate -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 2: {e}")

    print("--------------------------------------------------")

    # Test 3: two_sum
    try:
        res3_a = two_sum([2, 7, 11, 15], 9)
        res3_b = two_sum([3, 2, 4], 6)
        assert res3_a == [0, 1], f"Expected [0, 1], got {res3_a}"
        assert res3_b == [1, 2], f"Expected [1, 2], got {res3_b}"
        print("[Pass] โจทย์ที่ 3: two_sum")
        print(f"       -> [2, 7, 11, 15], target=9 -> Output: {res3_a} (ถูกต้อง!)")
        print(f"       -> [3, 2, 4], target=6      -> Output: {res3_b} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 3: two_sum -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 3: {e}")

    print("--------------------------------------------------")

    # Test 4: is_anagram
    try:
        res4_a = is_anagram("anagram", "nagaram")
        res4_b = is_anagram("rat", "car")
        assert res4_a is True, f"('anagram', 'nagaram') Expected True, got {res4_a}"
        assert res4_b is False, f"('rat', 'car') Expected False, got {res4_b}"
        print("[Pass] โจทย์ที่ 4: is_anagram")
        print(f"       -> 'anagram' & 'nagaram': {res4_a} (ถูกต้อง!)")
        print(f"       -> 'rat' & 'car':         {res4_b} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 4: is_anagram -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 4: {e}")

    print("--------------------------------------------------")

    # Test 5: group_anagrams
    try:
        raw_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        res_groups = group_anagrams(raw_words)
        normalized = sorted([sorted(g) for g in (res_groups or [])])
        expected = sorted([["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])
        assert normalized == expected, f"Expected {expected}, got {res_groups}"
        print("[Pass] โจทย์ที่ 5: group_anagrams")
        print(f"       -> Input:         {raw_words}")
        print(f"       -> Output ของคุณ: {res_groups} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 5: group_anagrams -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 5: {e}")

    print("==================================================")
