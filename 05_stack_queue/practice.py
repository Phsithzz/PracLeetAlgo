"""
05_stack_queue / practice.py
ไฟล์สำหรับฝึกเขียนโค้ดด้วยตัวเอง
คำแนะนำ: เขียนโค้ดในช่อง TODO โดยไม่เปิดดูเฉลย แล้วรัน 'python practice.py' เพื่อตรวจสอบ
"""

from typing import List
from collections import deque


def is_valid_parentheses(s: str) -> bool:
    """
    โจทย์ที่ 1: ตรวจสอบความถูกต้องของการจับคู่วงเล็บ (LeetCode 20)
    - รองรับวงเล็บสามแบบ: (), {}, []
    - ใช้ Stack เก็บวงเล็บเปิด และเมื่อเจอวงเล็บปิดให้ pop ตัวบนสุดมาเทียบ
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def eval_rpn(tokens: List[str]) -> int:
    """
    โจทย์ที่ 2: Reverse Polish Notation (LeetCode 150)
    - ประมวลผลจากซ้ายไปขวา: ถ้าเป็นตัวเลขให้ push เข้า stack
    - ถ้าเป็นเครื่องหมาย (+, -, *, /) ให้ pop ตัวเลข 2 ตัวมาคำนวณแล้ว push ผลลัพธ์กลับ
    - ระวัง: การหารให้ใช้ int(a / b) เพื่อตัดเศษทิ้งเข้าหา 0
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


class MinStack:
    """
    โจทย์ที่ 3: ออกแบบ Stack ที่สามารถดึงค่าต่ำสุดได้ใน O(1) (LeetCode 155)
    - ต้องมีเมธอด push(val), pop(), top(), getMin() ทั้งหมดทำงานใน O(1)
    - คำใบ้: ใช้ list 2 อัน (stack ปกติ และ min_stack ที่เก็บค่าน้อยสุดที่เคยพบ)
    """

    def __init__(self):
        # TODO: กำหนดโครงสร้างข้อมูล
        pass

    def push(self, val: int) -> None:
        # TODO: เพิ่มค่าเข้า stack
        pass

    def pop(self) -> None:
        # TODO: นำค่าบนสุดออกจาก stack
        pass

    def top(self) -> int:
        # TODO: ดูค่าบนสุดของ stack
        pass

    def getMin(self) -> int:
        # TODO: คืนค่าต่ำสุดใน stack ปัจจุบัน
        pass


class RecentCounter:
    """
    โจทย์ที่ 4: นับจำนวนการเรียกใช้งานล่าสุดในกรอบ 3000 ms (LeetCode 933)
    - เมื่อมีการเรียก ping(t) ให้เก็บ t ไว้
    - นำ request ที่เวลา < t - 3000 ออกจากคิว
    - คืนค่าจำนวน request ที่ยังเหลืออยู่ในช่วง [t - 3000, t]
    - เงื่อนไข: ใช้ collections.deque
    """

    def __init__(self):
        # TODO: กำหนดคิว
        pass

    def ping(self, t: int) -> int:
        # TODO: เขียนตรรกะการเพิ่มและคัดกรองเวลา
        pass


# ==========================================
# 🧪 Test Cases ตรวจสอบผลลัพธ์
# ==========================================
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    print("Testing your practice implementations in 05_stack_queue...")

    try:
        # Test 1: is_valid_parentheses
        assert is_valid_parentheses("()") is True, "Test 1.1 Failed"
        assert is_valid_parentheses("()[]{}") is True, "Test 1.2 Failed"
        assert is_valid_parentheses("(]") is False, "Test 1.3 Failed"
        assert is_valid_parentheses("([)]") is False, "Test 1.4 Failed"
        assert is_valid_parentheses("{[]}") is True, "Test 1.5 Failed"
        print("[Pass] Test 1: is_valid_parentheses")

        # Test 2: eval_rpn
        assert eval_rpn(["2", "1", "+", "3", "*"]) == 9, "Test 2.1 Failed"
        assert eval_rpn(["4", "13", "5", "/", "+"]) == 6, "Test 2.2 Failed"
        assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22, "Test 2.3 Failed"
        print("[Pass] Test 2: eval_rpn")

        # Test 3: MinStack
        ms = MinStack()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        assert ms.getMin() == -3, "Test 3.1 Failed"
        ms.pop()
        assert ms.top() == 0, "Test 3.2 Failed"
        assert ms.getMin() == -2, "Test 3.3 Failed"
        print("[Pass] Test 3: MinStack")

        # Test 4: RecentCounter
        rc = RecentCounter()
        assert rc.ping(1) == 1, "Test 4.1 Failed"
        assert rc.ping(100) == 2, "Test 4.2 Failed"
        assert rc.ping(3001) == 3, "Test 4.3 Failed"
        assert rc.ping(3002) == 3, "Test 4.4 Failed"
        print("[Pass] Test 4: RecentCounter")

        print("\n[EXCELLENT] All tests in 05_stack_queue passed!")
    except AssertionError as e:
        print(f"\n[FAIL] {e}")
        print("Tip: ตรวจสอบ LIFO สำหรับ Stack และ FIFO สำหรับ Deque ใน README.md / solutions.py")
    except Exception as e:
        print(f"\n[ERROR] เกิดข้อผิดพลาด: {e}")
