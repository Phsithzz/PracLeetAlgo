# 📅 ตารางฝึกซ้อม & Checklist การฝึกเขียนอัลกอริทึม (Training Tracker)

> "การฝึกเขียนโค้ดสัมภาษณ์ ไม่ใช่การท่องจำทุกบรรทัด แต่เป็นการจำ **'โครงสร้างความคิด' (Mental Model)** และ **'เทมเพลตมาตรฐาน' (Code Template)**"

---

## 🧭 แผนภาพตัดสินใจเลือก Pattern (Pattern Recognition Decision Tree)

เมื่อเจอโจทย์สัมภาษณ์ ให้ถามคำถามตามลำดับดังนี้:

```text
โจทย์ถามเรื่องอะไร?
 ├── 1. ข้อมูลถูกจัดเรียงแล้ว (Sorted Array) หรือต้องการหาจุดตัด / ขอบเขต?
 │    ├── หาค่าเป้าหมาย หรือหาจุดเริ่ม/จบ ใน O(log N) -> [Binary Search] (โฟลเดอร์ 02)
 │    └── หาคู่ผลรวม (Pair Sum), เช็คสมมาตร, เปรียบเทียบสองฝั่ง -> [Two Pointers] (โฟลเดอร์ 04)
 │
 ├── 2. โจทย์ถามหา Subarray / Substring ต่อเนื่อง (Contiguous)?
 │    ├── ขนาดหน้าต่างคงที่ (Size K) หรือขยาย/หดตามเงื่อนไข (At most K distinct) -> [Sliding Window] (โฟลเดอร์ 04)
 │    └── ต้องการผลรวมช่วงข้อมูลหลายครั้ง หรือหา Subarray ที่มีผลรวมเท่ากับ K -> [Prefix Sum] (โฟลเดอร์ 06)
 │
 ├── 3. โจทย์ต้องการค้นหาไวๆ, นับความถี่, ตรวจสอบตัวซ้ำใน O(1)?
 │    └── เก็บ Key-Value หรือ Set -> [Hash Map / Hash Set] (โฟลเดอร์ 03)
 │
 ├── 4. ทำงานกับลำดับย้อนกลับ, การจับคู่วงเล็บ, หรือหาตัวถัดไปที่มากกว่า (Next Greater Element)?
 │    ├── เข้าทีหลัง ออกก่อน (LIFO) -> [Stack] (โฟลเดอร์ 05)
 │    └── เข้าก่อน ออกก่อน (FIFO), วิ่งเป็นลำดับขั้น (Level-by-Level) -> [Queue / Deque] (โฟลเดอร์ 05)
 │
 ├── 5. โจทย์ต้องการสร้างผลลัพธ์ที่เป็นไปได้ทั้งหมด (Subsets, Permutations, Combinations)?
 │    └── ลองเลือก -> เรียกตัวเอง -> ย้อนกลับ (Backtrack) -> [Backtracking] (โฟลเดอร์ 07)
 │
 ├── 6. ปัญหามีความสัมพันธ์แบบเครือข่าย, ลำดับชั้น, เกาะในตาราง 2D (Grid/Graph/Tree)?
 │    ├── สำรวจไปจนสุดสายทาง / ตรวจสอบความถูกต้องของเส้นทาง -> [DFS] (โฟลเดอร์ 08)
 │    └── หาเส้นทางที่สั้นที่สุด (Shortest Path) บน Graph แบบ Unweighted หรือไล่ทีละชั้น -> [BFS] (โฟลเดอร์ 08)
 │
 └── 7. ปัญหามีการคำนวณซ้ำซ้อน มีคำว่า "ค่ามากสุด", "ค่าน้อยสุด", "จำนวนวิธีทั้งหมด" (Optimization/Counting)?
      └── มี Overlapping Subproblems & Optimal Substructure -> [Dynamic Programming] (โฟลเดอร์ 09)
```

---

## 🗓️ ตารางฝึกซ้อม 4 สัปดาห์ (4-Week Mastery Schedule)

ตามคำแนะนำ: **70% แรก** ของเวลาให้เน้น Array, Hash Map, Two Pointers, Sliding Window, Stack และ Binary Search เพราะเจอบ่อยสุดและเป็นฐานรากของทุกหัวข้อ!

### 🟢 สัปดาห์ที่ 1: รากฐาน Array, Search และ Hash Map
- [ ] **Day 1:** `01_array_basics` — Loop, Index, In-place Swap, Reverse, Min/Max
- [ ] **Day 2:** `02_sorting_searching` (Part 1) — Bubble, Selection, Insertion Sort
- [ ] **Day 3:** `02_sorting_searching` (Part 2) — Counting Sort, Binary Search (Template มาตรฐาน)
- [ ] **Day 4:** `03_hashmap_set` — Frequency Counter, Two Sum Pattern, Duplicate Detection
- [ ] **Day 5:** ซ้อมเขียน `01`, `02`, `03` ในไฟล์ `practice.py` จากศูนย์โดยไม่เปิดดูเฉลย
- [ ] **Day 6-7:** พักสมอง หรือทบทวนข้อที่ยังเขียนติดขัด

### 🔵 สัปดาห์ที่ 2: สองยอดวิชา Two Pointers, Sliding Window & Stack/Queue
- [ ] **Day 8:** `04_two_pointers_sliding_window` (Part 1) — Two Pointers (Left-Right, Opposite ends)
- [ ] **Day 9:** `04_two_pointers_sliding_window` (Part 2) — Sliding Window (Fixed size & Variable size)
- [ ] **Day 10:** `05_stack_queue` (Part 1) — Stack: Valid Parentheses, Evaluate RPN, Min Stack
- [ ] **Day 11:** `05_stack_queue` (Part 2) — Queue & Deque: Moving Average, Recent Calls
- [ ] **Day 12:** `06_prefix_sum` — Running Sum, Range Sum Query, Subarray Sum Equals K
- [ ] **Day 13-14:** ซ้อมเขียน `04`, `05`, `06` ใน `practice.py` ซ้ำจนคล่อง

### 🟡 สัปดาห์ที่ 3: Recursion, Backtracking และ Trees & Graphs
- [ ] **Day 15:** `07_recursion_backtracking` (Part 1) — Call stack, Base case, Factorial, Fibonacci
- [ ] **Day 16:** `07_recursion_backtracking` (Part 2) — Subsets, Permutations, Combination Sum
- [ ] **Day 17:** `08_tree_graph_traversal` (Part 1) — Binary Tree DFS (Inorder, Preorder, Postorder) & BFS (Level-order)
- [ ] **Day 18:** `08_tree_graph_traversal` (Part 2) — Graph Adjacency List, Visited Set, Number of Islands
- [ ] **Day 19-21:** ซ้อมเขียน `07` และ `08` ตั้งสมาธิเรื่อง Base Case และ Visited Check

### 🔴 สัปดาห์ที่ 4: Dynamic Programming & การสอบจำลองสัมภาษณ์จริง
- [ ] **Day 22:** `09_dynamic_programming` (Part 1) — Memoization vs Tabulation, Climbing Stairs
- [ ] **Day 23:** `09_dynamic_programming` (Part 2) — House Robber, Coin Change
- [ ] **Day 24:** `10_mixed_interview_patterns` (ข้อ 1-3) — ฝึกอ่านโจทย์แล้วระบุ Pattern ด้วยตัวเอง
- [ ] **Day 25:** `10_mixed_interview_patterns` (ข้อ 4-6) — จับเวลาทำเหมือนสัมภาษณ์จริง (ข้อละ 25 นาที)
- [ ] **Day 26-28:** Comprehensive Review — วนกลับมาเขียน `practice.py` ของทุกหัวข้อ

---

## ✅ ตารางติดตามความแม่นยำ (Mastery Checklist)

| หัวข้อ | Pass 1: อ่านเข้าใจ | Pass 2: เขียนตามเฉลย | Pass 3: เขียนเองจากศูนย์ | ซ้ำรอบ 2 (3 วันผ่านไป) | ซ้ำรอบ 3 (7 วันผ่านไป) | ระดับความมั่นใจ (1-5 ⭐) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| 01. Array Basics | [ ] | [ ] | [ ] | [ ] | [ ] | |
| 02. Sorting & Binary Search | [ ] | [ ] | [ ] | [ ] | [ ] | |
| 03. Hash Map & Set | [ ] | [ ] | [ ] | [ ] | [ ] | |
| 04. Two Pointers & Window | [ ] | [ ] | [ ] | [ ] | [ ] | |
| 05. Stack & Queue | [ ] | [ ] | [ ] | [ ] | [ ] | |
| 06. Prefix Sum | [ ] | [ ] | [ ] | [ ] | [ ] | |
| 07. Recursion & Backtracking | [ ] | [ ] | [ ] | [ ] | [ ] | |
| 08. Trees & Graphs | [ ] | [ ] | [ ] | [ ] | [ ] | |
| 09. Dynamic Programming | [ ] | [ ] | [ ] | [ ] | [ ] | |
| 10. Mixed Interview Mock | [ ] | [ ] | [ ] | [ ] | [ ] | |

---

## 💡 4 ขั้นตอนเวลาทำโจทย์สัมภาษณ์จริง (UMPIRE Technique)

1. **Understand (เข้าใจโจทย์):** ทวนโจทย์กับผู้สัมภาษณ์ ตรวจสอบขนาด Input, มีค่าติดลบหรือไม่, เป็นตัวเลขว่างได้ไหม (Edge Cases)
2. **Match (จับคู่ Pattern):** ใช้ Decision Tree ด้านบนเพื่อวิเคราะห์ว่าโจทย์นี้คล้ายโจทย์ข้อไหนที่เคยฝึกมา
3. **Plan (วางแผนแบบภาษาคน):** อธิบายไอเดียคร่าวๆ และบอก Time/Space Complexity ให้ผู้สัมภาษณ์เห็นด้วยก่อนเริ่มพิมพ์โค้ด
4. **Implement & Review (ลงมือโค้ดและตรวจทาน):** เขียนโค้ดให้อ่านง่าย แล้วสมมุติตัวเลขทดสอบทีละบรรทัด (Dry run)
