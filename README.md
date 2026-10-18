# 🚀 Algorithm & LeetCode Pattern Mastery (Python 3)
คลังฝึกเขียนโค้ดอัลกอริทึมและโครงสร้างข้อมูลจากศูนย์ สู่การจำและเข้าใจ Pattern สำหรับ Technical Interview

---

## 🎯 เป้าหมายของหลักสูตรนี้
1. **เข้าใจแก่น (Intuition & Mental Model):** รู้ว่าทำไมอัลกอริทึมนี้ถึงแก้ปัญหานี้ได้ดีที่สุด
2. **จำรูปแบบได้ (Pattern Recognition):** เห็นโจทย์ปุ๊บ รู้ปั๊บว่าต้องใช้เทคนิคไหน (Two Pointers, Sliding Window, DP, etc.)
3. **เขียนโค้ดจากศูนย์ได้เอง (Coding from Scratch):** ไม่ต้องพึ่งการท่องจำบรรทัดต่อบรรทัด แต่เขียนได้จากโครงสร้างความคิด
4. **มีสนามฝึกในตัว:** แต่ละหัวข้อมีทฤษฎี (`README.md`), โค้ดเฉลยละเอียด (`solutions.py`), และไฟล์ว่างพร้อมโจทย์+เทสต์ให้ซ้อมพิมพ์ (`practice.py`)

---

## 🧭 แผนผังโฟลเดอร์ (Directory Structure)

```text
leetAlgo/
├── README.md                           # คู่มือภาพรวมและสารบัญหลัก
├── TRAINING_SCHEDULE.md                # ตารางฝึกซ้อม 4 สัปดาห์ + Checklist ติดตามผล
│
├── 01_array_basics/                    # 1. การวน Loop, Index, Swap, Min/Max, Reverse
│   ├── README.md
│   ├── solutions.py
│   └── practice.py
│
├── 02_sorting_searching/               # 2. Bubble, Selection, Insertion, Counting, Binary Search
│   ├── README.md
│   ├── solutions.py
│   └── practice.py
│
├── 03_hashmap_set/                     # 3. Frequency Counter, Two Sum, Anagram, Lookups
│   ├── README.md
│   ├── solutions.py
│   └── practice.py
│
├── 04_two_pointers_sliding_window/     # 4. Two Pointers & Sliding Window Patterns
│   ├── README.md
│   ├── solutions.py
│   └── practice.py
│
├── 05_stack_queue/                     # 5. Stack (LIFO), Queue & Deque (FIFO), Monotonic Stack
│   ├── README.md
│   ├── solutions.py
│   └── practice.py
│
├── 06_prefix_sum/                      # 6. Range Query, Subarray Sum Equals K
│   ├── README.md
│   ├── solutions.py
│   └── practice.py
│
├── 07_recursion_backtracking/          # 7. Call Stack, Subsets, Permutations, Combination Sum
│   ├── README.md
│   ├── solutions.py
│   └── practice.py
│
├── 08_tree_graph_traversal/            # 8. DFS, BFS, Binary Tree, Visited Set, Islands
│   ├── README.md
│   ├── solutions.py
│   └── practice.py
│
├── 09_dynamic_programming/             # 9. Memoization, Tabulation, Knapsack, Coin Change
│   ├── README.md
│   ├── solutions.py
│   └── practice.py
│
└── 10_mixed_interview_patterns/        # 10. โจทย์คละสไตล์สัมภาษณ์จริง (ฝึกแยก Pattern เอง)
    ├── README.md
    ├── solutions.py
    └── practice.py
```

---

## 🛠️ วิธีการฝึกฝนที่มีประสิทธิภาพสูงสุด (3-Pass Method)

1. **Pass 1: อ่านทำความเข้าใจ (`README.md`)**
   - อ่านแนวคิด หัวใจสำคัญ และ Big-O Time & Space Complexity
   - สังเกต "Keyword สัญญาณเตือน" ที่บอกว่าโจทย์แบบไหนต้องใช้ Pattern นี้
2. **Pass 2: ศึกษาโค้ดเฉลย (`solutions.py`)**
   - รันโค้ดดูผลลัพธ์: `python solutions.py`
   - ดูโครงสร้างการตั้งตัวแปร (Pointers, Hash Map, Visited set) และลูปการทำงาน
3. **Pass 3: ฝึกเขียนเองจากศูนย์ (`practice.py`)**
   - เปิดไฟล์ `practice.py` ซึ่งมีเฉพาะโจทย์, Type Hints และ Unit Test
   - ลุยเขียนโค้ดลงในช่อง `# TODO` โดยไม่เปิดดูเฉลย
   - รันตรวจสอบความถูกต้อง: `python practice.py`
   - ถ้าติดขัด ให้แอบดูแนวคิดใน `README.md` หรือ `solutions.py` แล้วปิดทันที แล้วเขียนต่อด้วยมือตัวเอง
4. **ทำซ้ำแบบ Spaced Repetition:** กลับมาเขียน `practice.py` ซ้ำในอีก 3 วัน และ 7 วันถัดไป จนเขียนได้ลื่นไหลโดยไม่ต้องคิดนาน!

---

## 📊 ตารางติดตามการฝึกซ้อม
ดูรายละเอียดตารางฝึกซ้อมรายวัน เทคนิคการสัมภาษณ์ และ Checklists ได้ที่ [TRAINING_SCHEDULE.md](file:///C:/Important_university/prac/leetAlgo/TRAINING_SCHEDULE.md)
