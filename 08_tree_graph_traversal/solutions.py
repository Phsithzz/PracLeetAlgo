"""
08_tree_graph_traversal / solutions.py
เฉลยตัวอย่างโค้ดที่ถูกต้องและสะอาด สำหรับ Tree & Graph Traversal (DFS & BFS)
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
    หาความลึกสูงสุดของ Binary Tree ด้วย DFS (LeetCode 104)
    Time: O(N)
    Space: O(H) โดย H คือความสูงของ Tree
    """
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    ท่อง Binary Tree ทีละระดับชั้นด้วย BFS (LeetCode 102)
    Time: O(N)
    Space: O(N)
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


def graph_dfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """
    ท่อง Graph ด้วย DFS ผ่าน Recursion + Visited Set
    Time: O(V + E)
    Space: O(V)
    """
    visited = set()
    order = []

    def dfs(node: str):
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return order


def graph_bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """
    ท่อง Graph ด้วย BFS ผ่าน Queue + Visited Set
    Time: O(V + E)
    Space: O(V)
    """
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def num_islands(grid: List[List[str]]) -> int:
    """
    นับจำนวนเกาะ ('1' คือแผ่นดิน, '0' คือน้ำ) (LeetCode 200)
    Time: O(M * N)
    Space: O(M * N) Worst case call stack
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r: int, c: int):
        # ออกนอกตาราง หรือไม่ใช่แผ่นดิน
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return

        # จมเกาะ (เปลี่ยนเป็น '0' เพื่อป้องกันการนับซ้ำ)
        grid[r][c] = "0"

        # สำรวจ 4 ทิศทาง
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)

    return islands


def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """
    Flood Fill เปลี่ยนสีพิกเซลที่เชื่อมต่อกัน (LeetCode 733)
    Time: O(M * N)
    Space: O(M * N)
    """
    start_color = image[sr][sc]
    if start_color == color:
        return image

    rows, cols = len(image), len(image[0])

    def dfs(r: int, c: int):
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != start_color:
            return

        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image


# ==========================================
# 🧪 Test Cases ตรวจสอบความถูกต้อง
# ==========================================
if __name__ == "__main__":
    print("Testing 08_tree_graph_traversal solutions...")

    # สร้าง Binary Tree จำลอง:
    #        3
    #       / \
    #      9   20
    #         /  \
    #        15   7
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20, TreeNode(15), TreeNode(7))

    # Test 1: max_depth
    assert max_depth(tree) == 3, "Test 1 failed: depth should be 3"

    # Test 2: level_order
    assert level_order(tree) == [[3], [9, 20], [15, 7]], "Test 2 failed"

    # Test 3: graph_dfs & graph_bfs
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }
    dfs_result = graph_dfs(graph, "A")
    assert dfs_result == ["A", "B", "D", "E", "F", "C"], f"Test 3.1 failed: {dfs_result}"

    bfs_result = graph_bfs(graph, "A")
    assert bfs_result == ["A", "B", "C", "D", "E", "F"], f"Test 3.2 failed: {bfs_result}"

    # Test 4: num_islands
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands(grid1) == 3, "Test 4 failed"

    # Test 5: flood_fill
    img = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    filled = flood_fill(img, 1, 1, 2)
    assert filled == [[2, 2, 2], [2, 2, 0], [2, 0, 1]], "Test 5 failed"

    print("[OK] All tests in 08_tree_graph_traversal passed successfully!")
