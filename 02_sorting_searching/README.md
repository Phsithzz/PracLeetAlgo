# 02. Sorting & Searching (การเรียงลำดับและการค้นหา)

หัวข้อคลาสสิกที่ใช้วัดความเข้าใจเรื่อง Time/Space Complexity และเป็นพื้นฐานในการแปลงโจทย์ $O(N^2)$ ให้กลายเป็น $O(N \log N)$ หรือ $O(\log N)$

---

## 🧠 สรุป Sorting Algorithms ที่ต้องรู้

| Algorithm | Best Time | Average Time | Worst Time | Space | In-Place? | Stable? | จุดเด่น / แนวคิด |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **Bubble Sort** | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | Yes | Yes | เปรียบเทียบคู่ติดกันแล้วสลับ ค่ามากสุดจะ "ลอย" ไปท้ายสุด |
| **Selection Sort** | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | Yes | No | หาค่าน้อยสุดในส่วนที่เหลือ แล้วสลับมาไว้ข้างหน้า |
| **Insertion Sort** | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | Yes | Yes | เหมือนจั่วไพ่แล้วหยิบมาเสียบในตำแหน่งที่ถูกต้อง เร็วมากกับข้อมูลเกือบเรียง |
| **Counting Sort** | $O(N + K)$ | $O(N + K)$ | $O(N + K)$ | $O(K)$ | No | Yes | ไม่ใช้การเปรียบเทียบแต่นับความถี่ เหมาะกับเลขจำนวนเต็มช่วงแคบๆ $K$ |

---

## 🔍 สรุป Searching Algorithms

### 1. Linear Search
- ไล่ดูทีละตัวตั้งแต่ช่องแรกจนช่องสุดท้าย
- Time: $O(N)$, Space: $O(1)$
- ใช้เมื่อข้อมูล **ยังไม่ถูกจัดเรียง (Unsorted)**

### 2. Binary Search (สำคัญระดับ 5 ดาว ⭐⭐⭐⭐⭐)
- ใช้เมื่อข้อมูล **ถูกจัดเรียงแล้ว (Sorted)**
- Time: $O(\log N)$, Space: $O(1)$
- **แม่แบบมาตรฐานที่ต้องจำให้ขึ้นใจ:**
```python
def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        # หลีกเลี่ยง integer overflow (ในภาษาอื่น) และหาจุดกึ่งกลาง
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1      # เป้าหมายอยู่ฝั่งขวา
        else:
            right = mid - 1     # เป้าหมายอยู่ฝั่งซ้าย
            
    return -1  # หาไม่พบ
```

### จุดสังเกตของ Binary Search ในโจทย์สัมภาษณ์:
- โจทย์ระบุว่า Array เรียงลำดับแล้ว (`sorted`)
- โจทย์ต้องการความเร็ว $O(\log N)$
- โจทย์ประเภท "หาค่าที่น้อยที่สุดที่เป็นไปได้" หรือ "หาค่ามากที่สุดที่ยังผ่านเงื่อนไข" (Binary Search on Answer)

---

## 🎯 โจทย์ในโฟลเดอร์นี้
1. `bubble_sort(nums)`
2. `selection_sort(nums)`
3. `insertion_sort(nums)`
4. `counting_sort(nums)`
5. `binary_search(nums, target)`
6. `binary_search_left_bound(nums, target)` (หาตำแหน่งแรกสุดที่เจอตัวเลข ในกรณีมีเลขซ้ำ)
