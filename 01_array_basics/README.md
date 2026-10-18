# 01. Array Traversal & Index Manipulation (พื้นฐาน Array และ Index)

พื้นฐานที่สำคัญที่สุดของ Data Structures & Algorithms เพราะโครงสร้างข้อมูลส่วนใหญ่ถูกสร้างต่อยอดมาจาก Array ถ้าจัดการ Index พลาดแม้แต่ 1 ตำแหน่ง (Off-by-one error) อัลกอริทึมทั้งหมดจะทำงานผิดพลาดทันที

---

## 🧠 มโนทัศน์สำคัญ (Core Intuition)

Array (ใน Python คือ `list`) เก็บข้อมูลเรียงต่อกันในหน่วยความจำ:
- เข้าถึงข้อมูลด้วย Index: $O(1)$ เพราะคอมพิวเตอร์คำนวณตำแหน่ง `base_address + (index * element_size)` ได้ทันที
- ค้นหาข้อมูลที่ยังไม่เรียงลำดับ: $O(N)$ ต้องไล่ดูทีละตัว
- แทรก/ลบข้อมูลด้านหน้าหรือตรงกลาง: $O(N)$ เพราะต้องเลื่อน (Shift) สมาชิกตัวอื่นทั้งหมด
- เพิ่ม/ลบข้อมูลด้านท้าย (`append()`, `pop()`): $O(1)$ amortized

---

## 🔑 รูปแบบการเขียนโค้ดที่ต้องจำให้ขึ้นใจ (Essential Idioms)

### 1. การวน Loop รูปแบบต่างๆ
```python
nums = [10, 20, 30, 40]

# แบบที่ 1: ต้องการทั้ง Index และ Value (แนะนำที่สุดในโจทย์สัมภาษณ์)
for i, val in enumerate(nums):
    print(f"Index {i} has value {val}")

# แบบที่ 2: วนตาม Index ปกติ
for i in range(len(nums)):
    print(nums[i])

# แบบที่ 3: วนจากท้ายมาหน้า (Reverse Traversal)
# range(start, stop, step) -> สิ้นสุดที่ 0 ต้องใส่ stop เป็น -1
for i in range(len(nums) - 1, -1, -1):
    print(nums[i])
```

### 2. การสลับค่าในตัวแปร / สมาชิกใน Array (In-place Swap)
ใน Python เราสามารถสลับค่าได้ในบรรทัดเดียวโดยไม่ต้องสร้างตัวแปรชั่วคราว (`temp`):
```python
nums[i], nums[j] = nums[j], nums[i]
```

### 3. การกลับด้าน Array ด้วยตัวเอง (In-place Reverse)
ใช้ Two Pointers ฝั่งซ้ายและขวา วิ่งเข้าหากันแล้วสลับค่า:
```python
left, right = 0, len(nums) - 1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
```

### 4. การหาค่ามากสุด/น้อยสุดแบบไม่พึ่งฟังก์ชันสำเร็จรูป
```python
max_val = nums[0]  # สมมุติให้ตัวแรกมากสุดไว้ก่อน
for num in nums:
    if num > max_val:
        max_val = num
```

---

## 🎯 โจทย์สำหรับฝึกในโฟลเดอร์นี้

1. **`find_max_min(nums)`**: หาค่าสูงสุดและต่ำสุดพร้อมกันในลูปเดียว $O(N)$ Time, $O(1)$ Space
2. **`reverse_array_inplace(nums)`**: กลับด้าน array โดยไม่สร้าง list ใหม่ (In-place)
3. **`move_zeroes(nums)`**: ย้ายเลข 0 ทั้งหมดไปไว้ท้าย array โดยรักษาลำดับของเลขที่ไม่ใช่ 0 ไว้ (LeetCode 283)
4. **`rotate_array(nums, k)`**: หมุนขยับ array ไปทางขวา $k$ ตำแหน่งแบบ In-place (LeetCode 189)

---

## ⏱️ ความซับซ้อน (Complexity Summary)
- ทุกข้อในหมวดนี้ต้องทำได้ใน **$O(N)$ Time Complexity**
- Space Complexity ต้องเป็น **$O(1)$ (In-place)** ไม่สร้าง Array ก้อนใหม่ขนาด $N$
