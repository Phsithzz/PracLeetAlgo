"""
03_hashmap_set / solutions.py
เฉลยตัวอย่างโค้ดที่ถูกต้องและสะอาด สำหรับ Hash Map & Set Patterns
"""

from typing import Dict, List, Any
from collections import defaultdict


def frequency_counter(items: List[Any]) -> Dict[Any, int]:
    """
    นับความถี่ของสมาชิกแต่ละตัวใน List
    Time: O(N)
    Space: O(U) โดย U คือจำนวนสมาชิกที่ไม่ซ้ำกัน
    """
    counts: Dict[Any, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def has_duplicate(nums: List[int]) -> bool:
    """
    ตรวจสอบว่ามีตัวเลขซ้ำใน Array หรือไม่ (LeetCode 217)
    ใช้ Set ในการตรวจจับสิ่งที่เคยเจอแล้วใน O(1)
    Time: O(N)
    Space: O(N)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    ค้นหา Index สองตำแหน่งที่ค่ารวมกันได้ target (LeetCode 1)
    แนวคิด: เก็บ {ค่าตัวเลข: index} แล้วเช็คว่า (target - num) เคยมีใน map หรือไม่
    Time: O(N)
    Space: O(N)
    """
    num_to_idx = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_idx:
            return [num_to_idx[complement], i]
        num_to_idx[num] = i
    return []


def is_anagram(s: str, t: str) -> bool:
    """
    ตรวจสอบว่า t เป็น Anagram ของ s หรือไม่ (LeetCode 242)
    แนวคิด: นับความถี่ตัวอักษรของทั้งสองคำแล้วเทียบกัน
    Time: O(N)
    Space: O(1) เนื่องจากตัวอักษรภาษาอังกฤษมีจำกัดเพียง 26 ตัว
    """
    if len(s) != len(t):
        return False

    counts: Dict[str, int] = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1

    return True


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    จัดกลุ่มคำที่เป็น Anagram กัน (LeetCode 49)
    แนวคิด: ใช้คำที่เรียงตัวอักษรแล้ว (sorted string) เป็น Key ของ Dict
    Time: O(N * K log K) โดย K คือความยาวเฉลี่ยของคำ
    Space: O(N * K)
    """
    grouped = defaultdict(list)
    for word in strs:
        sorted_key = "".join(sorted(word))
        grouped[sorted_key].append(word)

    return list(grouped.values())


# ==========================================
# 🧪 Test Cases ตรวจสอบความถูกต้อง
# ==========================================
if __name__ == "__main__":
    print("Testing 03_hashmap_set solutions...")

    # Test 1: frequency_counter
    items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    fc = frequency_counter(items)
    assert fc == {"apple": 3, "banana": 2, "cherry": 1}, "Test 1 failed"

    # Test 2: has_duplicate
    assert has_duplicate([1, 2, 3, 1]) is True, "Test 2.1 failed"
    assert has_duplicate([1, 2, 3, 4]) is False, "Test 2.2 failed"

    # Test 3: two_sum
    assert two_sum([2, 7, 11, 15], 9) == [0, 1], "Test 3.1 failed"
    assert two_sum([3, 2, 4], 6) == [1, 2], "Test 3.2 failed"

    # Test 4: is_anagram
    assert is_anagram("anagram", "nagaram") is True, "Test 4.1 failed"
    assert is_anagram("rat", "car") is False, "Test 4.2 failed"

    # Test 5: group_anagrams
    raw_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res_groups = group_anagrams(raw_words)
    # Sort groups for comparison
    normalized = sorted([sorted(g) for g in res_groups])
    expected = sorted([["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])
    assert normalized == expected, f"Test 5 failed: got {normalized}"

    print("[OK] All tests in 03_hashmap_set passed successfully!")
