# 10. Mixed Interview Patterns (จำลองสถานการณ์สัมภาษณ์จริง - โจทย์คละหัวข้อ)

ในห้องสัมภาษณ์จริง **ไม่มีใครบอกคุณว่าข้อนี้ต้องใช้ Two Pointers หรือ Dynamic Programming** ผู้สัมภาษณ์จะให้เฉพาะโจทย์และตัวอย่าง คุณต้องสืบหา Pattern ที่ซ่อนอยู่ด้วยตัวเอง!

---

## 🕵️ เคล็ดลับการวิเคราะห์ Pattern จากขนาดของข้อมูล (Constraint Analysis)

ขนาดของข้อมูล $N$ ในโจทย์ คือ **คำบอกใบ้ชิ้นโต** ที่บอกว่าวิธีแก้ของคุณควรมี Time Complexity เท่าใด:

| ขนาดข้อมูล ($N$) | Time Complexity ที่ยอมรับได้ | อัลกอริทึมที่ควรนึกถึงเป็นอันดับแรก |
|---|:---:|---|
| $N \le 10 - 15$ | $O(N!)$ หรือ $O(2^N)$ | Backtracking, Permutations, Exhaustive Search |
| $N \le 100 - 500$ | $O(N^3)$ | Floyd-Warshall, 3-nested Loops, Matrix DP |
| $N \le 1,000 - 2,000$ | $O(N^2)$ | 2-nested Loops, 2D Dynamic Programming |
| $N \le 10^5$ | $O(N \log N)$ หรือ $O(N)$ | Sorting, Binary Search, Sliding Window, Two Pointers, Hash Map, Heap, Stack |
| $N \ge 10^6 - 10^9$ | $O(\log N)$ หรือ $O(1)$ | Binary Search, Math, Prefix Sum Query, Bit Manipulation |

---

## 🎯 6 โจทย์ท้าทายในโฟลเดอร์นี้ (ฝึกอ่านโจทย์แล้วเดา Pattern)

ลองอ่านโจทย์ทั้ง 6 ข้อด้านล่าง แล้วทายในใจก่อนเปิดดูเฉลยว่าแต่ละข้อใช้ Pattern อะไร:

1. **`product_except_self(nums)`**: คำนวณผลคูณของสมาชิกทุกตัวยกเว้นตัวเองใน $O(N)$ โดย **ห้ามใช้เครื่องหมายหาร `/`** (LeetCode 238)
2. **`three_sum(nums)`**: หาเลข 3 ตัวใน Array ที่รวมกันได้เท่ากับ 0 โดยไม่เอาผลลัพธ์ซ้ำ (LeetCode 15)
3. **`daily_temperatures(temperatures)`**: หาว่าต้องรอกี่วันกว่าจะเจอวันที่อุณหภูมิอุ่นขึ้นกว่าวันนี้ (LeetCode 739)
4. **`merge_intervals(intervals)`**: รวมช่วงเวลาที่ทับซ้อนกัน (Overlap) ให้เป็นช่วงเดียว (LeetCode 56)
5. **`word_search(board, word)`**: ค้นหาว่ามีคำศัพท์ที่กำหนดเรียงต่อกันในตารางอักษร 2 มิติหรือไม่ (LeetCode 79)
6. **`top_k_frequent(nums, k)`**: หาตัวเลข $k$ ตัวที่ปรากฏบ่อยที่สุด เร็วกว่า $O(N \log N)$ (LeetCode 347)
