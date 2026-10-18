# 04. Two Pointers & Sliding Window (สองตัวชี้ และ หน้าต่างเลื่อน)

สองรูปแบบที่ทรงอิทธิพลที่สุดในการแปลงลูปซ้อน $O(N^2)$ ให้กลายเป็นเส้นตรง $O(N)$

---

## 🧠 มโนทัศน์สำคัญ (Core Intuition)

### 1. Two Pointers (สองตัวชี้)
ใช้ตัวชี้ 2 ตัว วิ่งบน Array หรือ String:
- **วิ่งเข้าหากัน (Opposite Ends):** `left = 0, right = len - 1`
  - ใช้กับข้อมูลที่ **เรียงลำดับแล้ว (Sorted)** หรือการตรวจสอบความสมมาตร (Palindrome)
  - ขยับ `left += 1` เมื่อต้องการเพิ่มผลรวม หรือ `right -= 1` เมื่อต้องการลดผลรวม
- **วิ่งไปทิศเดียวกัน (Fast & Slow Pointers):**
  - Fast วิ่งสำรวจล่วงหน้า Slow คอยตามหลังเพื่อเก็บข้อมูลหรือเขียนทับ

### 2. Sliding Window (หน้าต่างเลื่อน)
ใช้หาคำตอบบน **Subarray หรือ Substring ที่ต่อเนื่องกัน (Contiguous)**:
- **Fixed Window (ขนาดคงที่ $K$):**
  - สร้างผลรวมของ $K$ ตัวแรกก่อน
  - จากนั้นเลื่อนหน้าต่าง: บวกตัวใหม่ทางขวาเข้า (`+ nums[i]`) และลบตัวเก่าทางซ้ายออก (`- nums[i - k]`)
- **Variable Window (ขยาย/หดได้ตามเงื่อนไข):**
  - ขยายขอบขวา (`right`) เพื่อดึงสมาชิกใหม่เข้าสู่หน้าต่าง
  - เมื่อหน้าต่าง **ไม่เป็นไปตามเงื่อนไข (Invalid)** -> ขยับขอบซ้าย (`left`) เพื่อบีบหน้าต่างให้กลับมาถูกต้อง
  - อัปเดตคำตอบที่ต้องการ (เช่น ความยาวมากสุด หรือผลรวมน้อยสุด)

```python
# โครงสร้างมาตรฐาน Variable Sliding Window
left = 0
for right in range(len(arr)):
    # 1. นำ arr[right] เข้าสู่ Window State
    
    # 2. ถ้า Window ขัดต่อเงื่อนไข ให้เลื่อนขอบซ้ายบีบเข้า
    while window_is_invalid:
        # ถอด arr[left] ออกจาก Window State
        left += 1
        
    # 3. อัปเดตคำตอบที่ดีที่สุด
    best_answer = max(best_answer, right - left + 1)
```

---

## 🎯 โจทย์ในโฟลเดอร์นี้
1. `is_palindrome(s)`: ตรวจสอบพาลินโดรมโดยไม่สนวรรคตอนและตัวพิมพ์เล็กใหญ่ (LeetCode 125)
2. `two_sum_sorted(nums, target)`: หาคู่บวกใน Sorted Array โดยใช้ Two Pointers (LeetCode 167)
3. `max_area_water(height)`: คำนวณพื้นที่กักเก็บน้ำมากที่สุด (LeetCode 11)
4. `max_sub_array_of_size_k(nums, k)`: หาผลรวมมากที่สุดของ Subarray ขนาดคงที่ $K$
5. `length_of_longest_substring(s)`: หาความยาวของ Substring ที่ไม่มีตัวอักษรซ้ำเลย (LeetCode 3)
6. `min_sub_array_len(target, nums)`: หาขนาด Subarray ที่สั้นที่สุดซึ่งมีผลรวม $\ge target$ (LeetCode 209)
