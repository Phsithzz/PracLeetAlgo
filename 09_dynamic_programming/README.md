# 09. Dynamic Programming (การโปรแกรมพลวัต - DP)

หัวข้อที่คนมักกลัวที่สุด แต่จริงๆ แล้ว DP คือ **"การจดบันทึกคำตอบของปัญหาย่อย เพื่อไม่ต้องคิดซ้ำ" (Remembering the past to not repeat it)**

---

## 🧠 มโนทัศน์สำคัญ (Core Intuition)

โจทย์ที่ใช้ DP มักมี 2 คุณสมบัติ:
1. **Overlapping Subproblems:** ปัญหาย่อยๆ มีการถูกเรียกคำนวณซ้ำไปซ้ำมา
2. **Optimal Substructure:** คำตอบที่ดีที่สุดของปัญหาใหญ่ สร้างขึ้นมาจากคำตอบที่ดีที่สุดของปัญหาย่อย

### 2 แนวทางหลักในการเขียน DP:

| คุณลักษณะ | Top-Down (Memoization) | Bottom-Up (Tabulation) |
|---|---|---|
| **รูปแบบ** | ใช้ **Recursion + Cache** | ใช้ **Loop + DP Array** |
| **ทิศทาง** | เริ่มจากปัญหาใหญ่ $N$ แตกย่อยลงไปถึง Base Case | เริ่มจาก Base Case $0, 1$ ค่อยๆ สะสมขึ้นมาถึง $N$ |
| **ข้อดี** | คิดง่าย ต่อเนื่องจาก Recursion ทันที | ไม่เปลือง Call Stack และประหยัด Memory ได้มากกว่า |

---

## 🔑 4 ขั้นตอนในการพิชิตโจทย์ DP (The 4-Step Framework)

1. **State Definition (นิยามสถานะ):** กำหนดว่า `dp[i]` แปลว่าอะไร? (เช่น `dp[i]` = จำนวนวิธีปีนบันได $i$ ขั้น)
2. **Base Cases (จุดเริ่มต้น):** กำหนดค่าเริ่มต้นที่รู้แน่นอน (เช่น `dp[1] = 1`, `dp[2] = 2`)
3. **Transition Function (สมการการเปลี่ยนสถานะ):** คำนวณ `dp[i]` จากช่องก่อนหน้าอย่างไร? (เช่น `dp[i] = dp[i-1] + dp[i-2]`)
4. **Order of Computation:** คำนวณจากไหนไปไหน (มักจะไล่จาก $i = 0 \to N$)

---

## 🎯 โจทย์ในโฟลเดอร์นี้
1. `climb_stairs(n)`: จำนวนวิธีปีนบันได $n$ ขั้น (ก้าวได้ 1 หรือ 2 ขั้น) (LeetCode 70)
2. `house_robber(nums)`: ขโมยบ้านโดยห้ามขโมยสองหลังติดกันเพื่อให้ได้เงินมากที่สุด (LeetCode 198)
3. `coin_change(coins, amount)`: หาจำนวนเหรียญที่น้อยที่สุดที่รวมได้เท่ากับ amount (LeetCode 322)
4. `length_of_lis(nums)`: ความยาวของ Longest Increasing Subsequence (LeetCode 300)
