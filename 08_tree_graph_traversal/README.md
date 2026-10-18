# 08. Tree & Graph Traversal (การท่องต้นไม้และกราฟ - DFS & BFS)

หัวข้อที่แยกผู้เขียนโปรแกรมทั่วไปออกจากวิศวกรซอฟต์แวร์ระดับมืออาชีพ Tree และ Graph คือหัวใจของระบบโครงสร้างข้อมูลทั่วโลก เช่น แผนที่ GPS, ระบบเครือข่ายเน็ตเวิร์ก, โครงสร้างไฟล์ใน OS และ DOM ในเว็บเบราว์เซอร์

---

## 🧠 มโนทัศน์สำคัญ (Core Intuition)

### 1. Depth-First Search (DFS - สำรวจแนวดิ่ง)
- ดำดิ่งไปจนสุดทางก่อน เมื่อไปต่อไม่ได้จึงค่อยย้อนกลับ (ใช้ Stack หรือ System Call Stack ผ่าน Recursion)
- **การท่องใน Binary Tree:**
  - **Preorder (Root -> Left -> Right):** ประมวลผล Node ปัจจุบันก่อน แล้วลงไปซ้ายและขวา
  - **Inorder (Left -> Root -> Right):** ถ้าใช้กับ Binary Search Tree (BST) จะได้ข้อมูลที่ **เรียงจากน้อยไปมากเสมอ!**
  - **Postorder (Left -> Right -> Root):** ลงไปคำนวณลูกซ้ายและขวาให้เสร็จก่อน แล้วค่อยนำผลกลับมาคำนวณที่ Root (เหมาะกับการหาความสูง หรือลบ Node)

### 2. Breadth-First Search (BFS - สำรวจแนวกว้าง)
- สำรวจสมาชิกที่อยู่ระยะห่างเท่ากันให้ครบก่อนเป็นระลอกคลื่น (Level-by-Level)
- **ต้องใช้ Queue (`collections.deque`) เสมอ**
- **คุณสมบัติพิเศษ:** บน Unweighted Graph หรือตาราง Grid ก้าวละ 1 ช่อง BFS จะรับประกันว่าค้นพบ **"เส้นทางที่สั้นที่สุด" (Shortest Path)** เสมอ

### 3. Grid Traversal (ตาราง 2 มิติ คือ Graph แบบหนึ่ง)
ตาราง $M \times N$ สามารถมองว่าแต่ละช่อง $(r, c)$ คือ Node หนึ่งตัว และมีเส้นเชื่อมไปยังช่องข้างเคียง 4 ทิศ:
```python
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # บน, ล่าง, ซ้าย, ขวา
for dr, dc in directions:
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols:  # ตรวจสอบขอบเขต
        # ดำเนินการต่อ
```

---

## 🎯 โจทย์ในโฟลเดอร์นี้
1. `max_depth(root)`: หาความลึกสูงสุดของ Binary Tree ด้วย DFS (LeetCode 104)
2. `level_order(root)`: ท่อง Binary Tree ทีละชั้นด้วย BFS (LeetCode 102)
3. `graph_dfs(graph, start)` & `graph_bfs(graph, start)`: ท่อง Graph ด้วย Visited Set
4. `num_islands(grid)`: นับจำนวนเกาะในแผนที่ 2 มิติ (LeetCode 200)
5. `flood_fill(image, sr, sc, color)`: เทสีระบายภาพแบบ Paint Bucket (LeetCode 733)
