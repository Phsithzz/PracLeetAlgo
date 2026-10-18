# 03. Hash Map & Set (การใช้งาน Dictionary และ Set)

ถ้าต้องเลือกโครงสร้างข้อมูลที่ **"ทรงพลังและเจอบ่อยที่สุดในการสัมภาษณ์งาน"** คำตอบคือ **Hash Map (Python `dict`) และ Hash Set (Python `set`)** เพราะช่วยลด Time Complexity จาก $O(N^2)$ เหลือเพียง $O(N)$

---

## 🧠 มโนทัศน์สำคัญ (Core Intuition)

- **กลไกภายใน:** ใช้ฟังก์ชันแฮช (`hash()`) เพื่อแปลง Key ให้เป็น Index ในหน่วยความจำโดยตรง ทำให้การค้นหา (`in`), การอ่านค่า (`dict[k]`), และการแทรก (`dict[k] = v`) ทำงานได้ใน **$O(1)$ Average Time Complexity**
- **ความต่างระหว่าง Dict กับ Set:**
  - `dict`: เก็บข้อมูลแบบคู่ Key-Value (เหมาะสำหรับนับความถี่, จับคู่ค่ากับ Index)
  - `set`: เก็บเฉพาะ Key ที่ไม่ซ้ำกัน (เหมาะสำหรับเช็คว่าเคยเจอตัวนี้หรือยัง ใน $O(1)$)

---

## 🔑 รูปแบบการใช้งานยอดนิยม (Must-Know Patterns)

### 1. การนับความถี่ (Frequency Counter)
```python
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1
```

### 2. เทคนิค Two Sum (ค้นหาส่วนเติมเต็ม Complement)
แทนที่จะใช้ลูปซ้อนกันสองชั้นเพื่อหาคู่ที่บวกกันได้ `target` ซึ่งใช้ $O(N^2)$ เราจำเลขที่เคยเจอไว้ใน Map พร้อม Index ของมัน:
```python
seen = {}  # {ตัวเลข: index}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

### 3. การจัดกลุ่มด้วย Categorization Key (เช่น Group Anagrams)
แปลงสมาชิกให้กลายเป็น Key มาตรฐาน เช่น คำว่า `"eat"`, `"tea"`, `"ate"` เมื่อถูก Sort ตัวอักษรจะได้ `"aet"` เหมือนกันทั้งหมด จึงใช้ `"aet"` เป็น Key รวมกลุ่มได้

---

## 🎯 โจทย์ในโฟลเดอร์นี้
1. `frequency_counter(items)`: ฟังก์ชันนับจำนวนความถี่ของสมาชิก
2. `has_duplicate(nums)`: ตรวจสอบว่าใน Array มีตัวเลขซ้ำหรือไม่ (LeetCode 217)
3. `two_sum(nums, target)`: คืน Index ของเลขสองตัวที่บวกกันได้ target (LeetCode 1)
4. `is_anagram(s, t)`: ตรวจสอบว่าสอง String มีตัวอักษรและจำนวนเท่ากันเป๊ะหรือไม่ (LeetCode 242)
5. `group_anagrams(strs)`: จัดกลุ่มคำที่เป็น Anagram กันเข้าไว้ใน List เดียวกัน (LeetCode 49)
