"""
08_tree_graph_traversal / practice.py
ไฟล์สำหรับฝึกเขียนโค้ดด้วยตัวเอง
คำแนะนำ: เขียนโค้ดในช่อง TODO โดยไม่เปิดดูเฉลย แล้วรัน 'python practice.py' เพื่อตรวจสอบ
"""

from typing import List, Optional, Dict
from collections import deque


class TreeNode:
    """นิยาม Node ของ Binary Tree"""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    """
    โจทย์ที่ 1: Maximum Depth of Binary Tree (LeetCode 104)
    - Base Case: ถ้าไม่มี root คืน 0
    - คืนค่า 1 + max(ความลึกฝั่งซ้าย, ความลึกฝั่งขวา)
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    โจทย์ที่ 2: Binary Tree Level Order Traversal (LeetCode 102)
    - ใช้ collections.deque สำหรับคิว
    - วนลูปทีละระดับ: วน popleft() ตามจำนวนโหนดในชั้นนั้น (len(queue)) แล้ว push ลูกซ้ายขวาเข้าคิว
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def graph_dfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """
    โจทย์ที่ 3: DFS บน Graph
    - ท่องกราฟแบบลงลึกจนสุดทางก่อน
    - ใช้ visited = set() ป้องกันการวนกลับมาที่เดิม
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def graph_bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """
    โจทย์ที่ 4: BFS บน Graph
    - ท่องกราฟแบบกระจายตัวรอบทิศทีละสเต็ป
    - ใช้ queue = deque([start]) และ visited = {start}
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def num_islands(grid: List[List[str]]) -> int:
    """
    โจทย์ที่ 5: Number of Islands (LeetCode 200)
    - แผ่นดินคือ '1' น้ำคือ '0'
    - วนลูปดูทุกช่องในตาราง เมื่อเจอ '1' ให้นับเกาะเพิ่ม 1 แล้วเรียก DFS/BFS จมเกาะนั้นเป็น '0'
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """
    โจทย์ที่ 6: Flood Fill (LeetCode 733)
    - เปลี่ยนสีเริ่มต้นที่จุด (sr, sc) และพิกเซลข้างเคียงที่เชื่อมต่อกันและมีสีเดิม ให้กลายเป็น color
    """
    # TODO: เขียนโค้ดของคุณที่นี่
    pass


# ==========================================
# 🧪 Test Cases ตรวจสอบผลลัพธ์
# ==========================================
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    print("Testing your practice implementations in 08_tree_graph_traversal...")

    try:
        # สร้าง Binary Tree
        tree = TreeNode(3)
        tree.left = TreeNode(9)
        tree.right = TreeNode(20, TreeNode(15), TreeNode(7))

        # Test 1: max_depth
        assert max_depth(tree) == 3, "Test 1 Failed: max_depth"
        print("[Pass] Test 1: max_depth")

        # Test 2: level_order
        res_lo = level_order(tree)
        assert res_lo == [[3], [9, 20], [15, 7]], f"Test 2 Failed: {res_lo}"
        print("[Pass] Test 2: level_order")

        # Test 3 & 4: graph_dfs & graph_bfs
        graph = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": ["F"],
            "D": [],
            "E": ["F"],
            "F": [],
        }
        assert graph_dfs(graph, "A") == ["A", "B", "D", "E", "F", "C"], "Test 3 Failed: graph_dfs"
        print("[Pass] Test 3: graph_dfs")

        assert graph_bfs(graph, "A") == ["A", "B", "C", "D", "E", "F"], "Test 4 Failed: graph_bfs"
        print("[Pass] Test 4: graph_bfs")

        # Test 5: num_islands
        grid1 = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        assert num_islands(grid1) == 3, "Test 5 Failed: num_islands"
        print("[Pass] Test 5: num_islands")

        # Test 6: flood_fill
        img = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        filled = flood_fill(img, 1, 1, 2)
        assert filled == [[2, 2, 2], [2, 2, 0], [2, 0, 1]], "Test 6 Failed: flood_fill"
        print("[Pass] Test 6: flood_fill")

        print("\n[EXCELLENT] All tests in 08_tree_graph_traversal passed!")
    except AssertionError as e:
        print(f"\n[FAIL] {e}")
        print("Tip: ทบทวน base case ของ DFS และการใช้ deque ใน BFS จาก README.md / solutions.py")
    except Exception as e:
        print(f"\n[ERROR] เกิดข้อผิดพลาด: {e}")
