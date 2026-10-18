# 07. Recursion & Backtracking (การเรียกตัวเอง และ แบ็คแทร็กกิง)

หัวใจสำคัญของการสร้างผลลัพธ์ที่เป็นไปได้ทั้งหมด (Exhaustive Search / Combinatorics) เช่น การจัดหมู่ การสลับเปลี่ยน และการแก้ปริศนาอย่างเขาวงกตหรือ Sudoku

---

## 🧠 มโนทัศน์สำคัญ (Core Intuition)

### 1. Recursion (ฟังก์ชันเรียกตัวเอง)
การแก้ปัญหาใหญ่ด้วยการแบ่งเป็นปัญหาย่อยที่มีโครงสร้างเหมือนเดิม โดยต้องมี 2 ส่วนเสมอ:
1. **Base Case (จุดหยุด):** เงื่อนไขที่ง่ายที่สุดที่รู้คำตอบทันที โดยไม่ต้องเรียกตัวเองซ้ำ (ถ้าลืมข้อนี้ จะเกิด `RecursionError: maximum recursion depth exceeded`)
2. **Recursive Step (การเรียกซ้ำ):** ปรับขนาด Input ให้เล็กลงแล้วส่งต่อให้ตัวเอง

```python
def factorial(n: int) -> int:
    # 1. Base Case
    if n <= 1:
        return 1
    # 2. Recursive Step
    return n * factorial(n - 1)
```

### 2. Backtracking Template (โครงสร้างแม่แบบ 3 สเต็ป)
เมื่อต้องสำรวจ "ทุกเส้นทางที่เป็นไปได้" แต่ถ้าเจอทางตัน ให้ "ถอยกลับ":

$$\text{Choose (เลือก)} \longrightarrow \text{Explore (สำรวจต่อ)} \longrightarrow \text{Unchoose (ยกเลิกการเลือกเพื่อลองทางอื่น)}$$

```python
def backtrack(start_index, current_path):
    # 1. Base Case: ถ้าทางเลือกนี้ครบตามเงื่อนไข ให้บันทึกคำตอบ
    if is_valid_solution(current_path):
        result.append(list(current_path))  # ต้อง copy list เสมอ!
        return

    # 2. วนลูปสำรวจทุกตัวเลือกที่เป็นไปได้
    for i in range(start_index, len(candidates)):
        # (Optional) Pruning: ข้ามตัวเลือกที่ไม่สอดคล้อง
        if not is_promising(candidates[i]):
            continue

        # Step 1: Choose (หยิบเข้า)
        current_path.append(candidates[i])

        # Step 2: Explore (ดำดิ่งลงไป)
        backtrack(i + 1, current_path)

        # Step 3: Unchoose (ดึงออก เพื่อลองตัวถัดไป)
        current_path.pop()
```

---

## 🎯 โจทย์ในโฟลเดอร์นี้
1. `factorial(n)`: คำนวณค่า $N!$ ด้วย Recursion
2. `fibonacci(n)`: คำนวณลำดับ Fibonacci ตัวที่ $n$
3. `subsets(nums)`: หา Subsets ทั้งหมดที่เป็นไปได้ (Power Set) ขนาด $2^N$ (LeetCode 78)
4. `permutations(nums)`: หาการเรียงสับเปลี่ยนทั้งหมด ขนาด $N!$ (LeetCode 46)
5. `combination_sum(candidates, target)`: หาชุดตัวเลขที่บวกกันได้ target (ใช้เลขซ้ำได้) (LeetCode 39)
