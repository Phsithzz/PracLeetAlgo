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
    print("==================================================")
    print("🚀 ผลการทดสอบโค้ดของคุณ (05_stack_queue)")
    print("==================================================")

    # Test 1: is_valid_parentheses
    try:
        res1_a = is_valid_parentheses("()")
        res1_b = is_valid_parentheses("()[]{}")
        res1_c = is_valid_parentheses("([)]")
        assert res1_a is True and res1_b is True and res1_c is False, "Bracket validation failed"
        print("[Pass] โจทย์ที่ 1: is_valid_parentheses")
        print(f"       -> '()'     : {res1_a} (ถูกต้อง!)")
        print(f"       -> '()[]{{}}': {res1_b} (ถูกต้อง!)")
        print(f"       -> '([)]'   : {res1_c} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 1: is_valid_parentheses -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 1: {e}")

    print("--------------------------------------------------")

    # Test 2: eval_rpn
    try:
        tokens2_a = ["2", "1", "+", "3", "*"]
        res2_a = eval_rpn(tokens2_a)
        tokens2_b = ["4", "13", "5", "/", "+"]
        res2_b = eval_rpn(tokens2_b)
        assert res2_a == 9, f"Tokens {tokens2_a} Expected 9, got {res2_a}"
        assert res2_b == 6, f"Tokens {tokens2_b} Expected 6, got {res2_b}"
        print("[Pass] โจทย์ที่ 2: eval_rpn")
        print(f"       -> ['2','1','+','3','*']   -> Output: {res2_a} (ถูกต้อง!)")
        print(f"       -> ['4','13','5','/','+']  -> Output: {res2_b} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 2: eval_rpn -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 2: {e}")

    print("--------------------------------------------------")

    # Test 3: MinStack
    try:
        ms = MinStack()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        m1 = ms.getMin()
        assert m1 == -3, f"Expected min -3, got {m1}"
        ms.pop()
        top_val = ms.top()
        m2 = ms.getMin()
        assert top_val == 0, f"Expected top 0, got {top_val}"
        assert m2 == -2, f"Expected min -2, got {m2}"
        print("[Pass] โจทย์ที่ 3: MinStack")
        print(f"       -> push(-2), push(0), push(-3) -> getMin(): {m1} (ถูกต้อง!)")
        print(f"       -> pop() -> top(): {top_val}, getMin(): {m2} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 3: MinStack -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 3: {e}")

    print("--------------------------------------------------")

    # Test 4: RecentCounter
    try:
        rc = RecentCounter()
        p1 = rc.ping(1)
        p2 = rc.ping(100)
        p3 = rc.ping(3001)
        p4 = rc.ping(3002)
        assert p1 == 1 and p2 == 2 and p3 == 3 and p4 == 3, f"RecentCounter expected [1, 2, 3, 3], got {[p1, p2, p3, p4]}"
        print("[Pass] โจทย์ที่ 4: RecentCounter")
        print(f"       -> ping(1): {p1}, ping(100): {p2}, ping(3001): {p3}, ping(3002): {p4} (ถูกต้อง!)")
    except AssertionError as e:
        print(f"[FAIL] โจทย์ที่ 4: RecentCounter -> {e}")
    except Exception as e:
        print(f"[ERROR] โจทย์ที่ 4: {e}")

    print("==================================================")
