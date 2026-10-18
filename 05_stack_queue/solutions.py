"""
05_stack_queue / solutions.py
เฉลยตัวอย่างโค้ดที่ถูกต้องและสะอาด สำหรับ Stack และ Queue / Deque
"""

from typing import List
from collections import deque


def is_valid_parentheses(s: str) -> bool:
    """
    ตรวจสอบความถูกต้องของการจับคู่วงเล็บ (LeetCode 20)
    Time: O(N)
    Space: O(N)
    """
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in bracket_map:
            # เจอวงเล็บปิด: ต้องมีวงเล็บเปิดที่ตรงกันอยู่บนยอด Stack
            top_element = stack.pop() if stack else "#"
            if bracket_map[char] != top_element:
                return False
        else:
            # เจอวงเล็บเปิด: ดันเข้า Stack
            stack.append(char)

    return len(stack) == 0


def eval_rpn(tokens: List[str]) -> int:
    """
    คำนวณค่านิพจน์ Reverse Polish Notation (LeetCode 150)
    Time: O(N)
    Space: O(N)
    """
    stack = []

    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # สำคัญ: Python a // b ปัดลงทางลบ แต่โจทย์ต้องการตัดเศษทิ้งเข้าหา 0
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]


class MinStack:
    """
    Stack ที่รองรับ push, pop, top และ getMin() ได้ใน O(1) (LeetCode 155)
    แนวคิด: ใช้ min_stack คู่ขนานเก็บค่าต่ำสุด ณ จังหวะนั้นๆ
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # นำค่าน้อยสุดระหว่างตัวใหม่กับค่าน้อยสุดเดิมเข้า min_stack
        current_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class RecentCounter:
    """
    นับจำนวนคำขอที่เข้ามาในกรอบ 3000 ms ล่าสุด [t - 3000, t] (LeetCode 933)
    แนวคิด: ใช้ collections.deque บันทึกเวลา แล้ว popleft() ตัวที่เก่าเกิน 3000 ms ทิ้ง
    """

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        # ลบ request ที่หมดอายุ (อยู่นอกช่วง [t - 3000, t])
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)


# ==========================================
# 🧪 Test Cases ตรวจสอบความถูกต้อง
# ==========================================
if __name__ == "__main__":
    print("Testing 05_stack_queue solutions...")

    # Test 1: is_valid_parentheses
    assert is_valid_parentheses("()") is True, "Test 1.1 failed"
    assert is_valid_parentheses("()[]{}") is True, "Test 1.2 failed"
    assert is_valid_parentheses("(]") is False, "Test 1.3 failed"
    assert is_valid_parentheses("([)]") is False, "Test 1.4 failed"
    assert is_valid_parentheses("{[]}") is True, "Test 1.5 failed"

    # Test 2: eval_rpn
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9, "Test 2.1 failed"  # (2 + 1) * 3
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6, "Test 2.2 failed"  # 4 + (13 / 5)
    assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22, "Test 2.3 failed"

    # Test 3: MinStack
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3, "Test 3.1 failed"
    ms.pop()
    assert ms.top() == 0, "Test 3.2 failed"
    assert ms.getMin() == -2, "Test 3.3 failed"

    # Test 4: RecentCounter
    rc = RecentCounter()
    assert rc.ping(1) == 1, "Test 4.1 failed"
    assert rc.ping(100) == 2, "Test 4.2 failed"
    assert rc.ping(3001) == 3, "Test 4.3 failed"
    assert rc.ping(3002) == 3, "Test 4.4 failed"  # ping at 1 is discarded (3002 - 3000 = 2)

    print("[OK] All tests in 05_stack_queue passed successfully!")
