# 06. Prefix Sum (ผลรวมสะสม)

เทคนิคสุดเฉียบในการคำนวณผลรวมของช่วงข้อมูล (Range Sum Query) ได้ในเวลา $O(1)$ และเมื่อนำมารวมร่างกับ Hash Map จะสามารถแก้โจทย์ Subarray ที่ดูยากซับซ้อนได้ใน $O(N)$!

---

## 🧠 มโนทัศน์สำคัญ (Core Intuition)

### 1. การคำนวณผลรวมช่วง (Range Sum) ใน $O(1)$
สมมุติว่าเรามี Array `nums = [1, 2, 3, 4, 5]`
ถ้าเราต้องตอบคำถาม "ผลรวมตั้งแต่ index `left` ถึง `right` คือเท่าไร?" หลายๆ ครั้ง
- ถ้าวนลูปบวกทุกครั้ง: ใช้เวลา $O(N)$ ต่อคำถาม
- ถ้าสร้าง **Prefix Sum Array** ไว้ล่วงหน้า:
  - ให้ `prefix[i]` คือผลรวมตั้งแต่ index 0 ถึง `i-1` โดยกำหนด `prefix[0] = 0`
  - ผลรวมช่วง `[left, right]` = `prefix[right + 1] - prefix[left]` ในเวลาเพียง **$O(1)$**

```text
nums:    [ 1,  2,  3,  4,  5]
prefix:  [0,  1,  3,  6, 10, 15]

ผลรวม index 1 ถึง 3 (ค่าคือ 2 + 3 + 4 = 9):
prefix[3 + 1] - prefix[1] = prefix[4] - prefix[1] = 10 - 1 = 9  🎯
```

### 2. มนต์วิเศษ: Prefix Sum + Hash Map (โจทย์ระดับ Medium ที่ออกบ่อยมาก!)
โจทย์ถาม: *"มีกี่ Subarray ที่มีผลรวมเท่ากับ $K$?"* (LeetCode 560)
- ความสัมพันธ์ทางคณิตศาสตร์:
  $$\text{Current Prefix Sum} - \text{Previous Prefix Sum} = K$$
  $$\text{Previous Prefix Sum} = \text{Current Prefix Sum} - K$$
- **แนวคิด:** ในขณะที่เราเดินไปข้างหน้าและสะสมผลรวม `curr_sum` ให้ตรวจดูใน Hash Map ว่าเคยมีผลรวมเท่ากับ `curr_sum - K` มาก่อนหรือไม่ ถ้าเคยมี แสดงว่า Subarray ระหว่างจุดนั้นมาถึงจุดปัจจุบันมีผลรวมเท่ากับ $K$ แน่นอน!
- ⚠️ **กฎทอง:** ต้องกำหนดค่าเริ่มต้นให้ Hash Map เสมอคือ `{0: 1}` เพื่อรองรับกรณีที่ Subarray เริ่มต้นจาก index 0 พอดิบพอดี

---

## 🎯 โจทย์ในโฟลเดอร์นี้
1. `running_sum(nums)`: คำนวณผลรวมสะสมของ Array (LeetCode 1480)
2. `NumArray`: คลาสตอบผลรวมช่วง `sumRange(left, right)` ใน $O(1)$ (LeetCode 303)
3. `subarray_sum_equals_k(nums, k)`: นับจำนวน Subarray ที่บวกกันได้ $k$ (LeetCode 560)
4. `find_max_length_equal_0_1(nums)`: หา Subarray ที่ยาวที่สุดที่มีเลข 0 และ 1 จำนวนเท่ากัน (LeetCode 525)
