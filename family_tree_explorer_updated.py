# ============================================================
# FAMILY TREE EXPLORER
# Data Structures and Algorithms - Assignment II
# Project 18
# 
# ============================================================

import random
import time
from collections import deque


# ============================================================
# 1. FAMILY DATA - EXACTLY 15 MEMBERS
# ============================================================

FAMILY_DATA = [
    (1, "Arun", None),
    (2, "Ravi", 1),
    (3, "Priya", 1),
    (4, "Karthik", 1),
    (5, "Kumar", 2),
    (6, "Meena", 2),
    (7, "Divya", 3),
    (8, "Sanjay", 3),
    (9, "Nila", 5),
    (10, "Rahul", 5),
    (11, "Aadhya", 6),
    (12, "Varun", 6),
    (13, "Isha", 7),
    (14, "Arjun", 8),
    (15, "Tara", 8)
]


# ============================================================
# 2. GENERAL TREE
# Insert, delete subtree, display and traversals
# ============================================================

class FamilyMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.parent = None
        self.children = []


class FamilyTree:
    def __init__(self):
        self.members = {}
        self.root = None

        for member_id, name, parent_id in FAMILY_DATA:
            self.members[member_id] = FamilyMember(member_id, name)

        for member_id, name, parent_id in FAMILY_DATA:
            member = self.members[member_id]

            if parent_id is None:
                self.root = member
            else:
                parent = self.members[parent_id]
                member.parent = parent
                parent.children.append(member)

    def add_member(self, parent_id, member_id, name):
        if member_id in self.members:
            print("Member ID already exists.")
            return

        if parent_id not in self.members:
            print("Parent not found.")
            return

        member = FamilyMember(member_id, name)
        parent = self.members[parent_id]
        member.parent = parent
        parent.children.append(member)
        self.members[member_id] = member
        print("Member added successfully.")

    def delete_subtree(self, member_id):
        if member_id == self.root.member_id:
            print("Root member cannot be deleted.")
            return

        if member_id not in self.members:
            print("Member not found.")
            return

        member = self.members[member_id]

        if member.parent:
            member.parent.children.remove(member)

        def remove(node):
            for child in node.children:
                remove(child)
            del self.members[node.member_id]

        remove(member)
        print("Subtree deleted successfully.")

    def display(self, node=None, level=0):
        if node is None:
            node = self.root

        print("  " * level + f"{node.name} (ID: {node.member_id})")

        for child in node.children:
            self.display(child, level + 1)

    def preorder(self, node=None):
        if node is None:
            node = self.root

        print(node.name, end=" ")

        for child in node.children:
            self.preorder(child)

    def postorder(self, node=None):
        if node is None:
            node = self.root

        for child in node.children:
            self.postorder(child)

        print(node.name, end=" ")

    def level_order(self):
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            print(node.name, end=" ")
            queue.extend(node.children)

    def iterative_preorder(self):
        stack = [self.root]

        while stack:
            node = stack.pop()
            print(node.name, end=" ")
            stack.extend(reversed(node.children))

    def iterative_postorder(self):
        stack1 = [self.root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)
            stack1.extend(node.children)

        while stack2:
            print(stack2.pop().name, end=" ")


# ============================================================
# 3. BINARY TREE AND LOWEST COMMON ANCESTOR
# Recursive and iterative traversals
# ============================================================

class BinaryNode:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.left = None
        self.right = None


class BinaryFamilyTree:
    def __init__(self):
        self.root = BinaryNode(1, "Arun")

        self.root.left = BinaryNode(2, "Ravi")
        self.root.right = BinaryNode(3, "Priya")

        self.root.left.left = BinaryNode(5, "Kumar")
        self.root.left.right = BinaryNode(6, "Meena")

        self.root.right.left = BinaryNode(7, "Divya")
        self.root.right.right = BinaryNode(8, "Sanjay")

        self.root.left.left.left = BinaryNode(9, "Nila")
        self.root.left.left.right = BinaryNode(10, "Rahul")

        self.root.left.right.left = BinaryNode(11, "Aadhya")
        self.root.left.right.right = BinaryNode(12, "Varun")

        self.root.right.left.left = BinaryNode(13, "Isha")
        self.root.right.left.left.right = BinaryNode(4, "Karthik")
        self.root.right.right.left = BinaryNode(14, "Arjun")
        self.root.right.right.right = BinaryNode(15, "Tara")

    def inorder_recursive(self, node):
        if node:
            self.inorder_recursive(node.left)
            print(node.name, end=" ")
            self.inorder_recursive(node.right)

    def preorder_recursive(self, node):
        if node:
            print(node.name, end=" ")
            self.preorder_recursive(node.left)
            self.preorder_recursive(node.right)

    def postorder_recursive(self, node):
        if node:
            self.postorder_recursive(node.left)
            self.postorder_recursive(node.right)
            print(node.name, end=" ")

    def level_recursive_helper(self, node, level):
        if node is None:
            return

        if level == 1:
            print(node.name, end=" ")
        else:
            self.level_recursive_helper(node.left, level - 1)
            self.level_recursive_helper(node.right, level - 1)

    def height(self, node):
        if node is None:
            return 0
        maximum = 0
        stack = [(node, 1)]
        while stack:
            current, level = stack.pop()
            maximum = max(maximum, level)
            if current.left:
                stack.append((current.left, level + 1))
            if current.right:
                stack.append((current.right, level + 1))
        return maximum

    def level_recursive(self):
        for level in range(1, self.height(self.root) + 1):
            self.level_recursive_helper(self.root, level)

    def inorder_iterative(self):
        stack = []
        current = self.root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            print(current.name, end=" ")
            current = current.right

    def preorder_iterative(self):
        stack = [self.root]

        while stack:
            node = stack.pop()
            print(node.name, end=" ")

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def postorder_iterative(self):
        first = [self.root]
        second = []

        while first:
            node = first.pop()
            second.append(node)

            if node.left:
                first.append(node.left)
            if node.right:
                first.append(node.right)

        while second:
            print(second.pop().name, end=" ")

    def level_iterative(self):
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            print(node.name, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def find_node(self, node, member_id):
        if node is None:
            return None
        if node.member_id == member_id:
            return node

        result = self.find_node(node.left, member_id)
        if result:
            return result

        return self.find_node(node.right, member_id)

    def lca(self, node, id1, id2):
        if node is None:
            return None

        if node.member_id == id1 or node.member_id == id2:
            return node

        left = self.lca(node.left, id1, id2)
        right = self.lca(node.right, id1, id2)

        if left and right:
            return node

        return left if left else right

    def lowest_common_ancestor(self, id1, id2):
        if not self.find_node(self.root, id1):
            print("First member not found.")
            return

        if not self.find_node(self.root, id2):
            print("Second member not found.")
            return

        result = self.lca(self.root, id1, id2)

        if result:
            print("Lowest Common Ancestor:", result.name)


# ============================================================
# 4. BINARY SEARCH TREE
# Insert, search, delete, min/max, successor, predecessor
# ============================================================

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_node(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self.insert_node(node.left, key)
        elif key > node.key:
            node.right = self.insert_node(node.right, key)
        return node

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
            return
        current = self.root
        while True:
            if key == current.key:
                return
            if key < current.key:
                if current.left is None:
                    current.left = BSTNode(key)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = BSTNode(key)
                    return
                current = current.right

    def search(self, key):
        current = self.root

        while current:
            if key == current.key:
                return True
            if key < current.key:
                current = current.left
            else:
                current = current.right

        return False

    def minimum_node(self, node):
        while node and node.left:
            node = node.left
        return node

    def maximum_node(self, node):
        while node and node.right:
            node = node.right
        return node

    def delete_node(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self.delete_node(node.left, key)
        elif key > node.key:
            node.right = self.delete_node(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self.minimum_node(node.right)
            node.key = successor.key
            node.right = self.delete_node(node.right, successor.key)

        return node

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def successor(self, key):
        current = self.root
        answer = None

        while current:
            if current.key > key:
                answer = current
                current = current.left
            else:
                current = current.right

        return answer.key if answer else None

    def predecessor(self, key):
        current = self.root
        answer = None

        while current:
            if current.key < key:
                answer = current
                current = current.right
            else:
                current = current.left

        return answer.key if answer else None

    def range_query(self, node, low, high):
        if node:
            if node.key > low:
                self.range_query(node.left, low, high)

            if low <= node.key <= high:
                print(node.key, end=" ")

            if node.key < high:
                self.range_query(node.right, low, high)


# ============================================================
# 5. AVL TREE
# Insert, delete, rotations and verification
# ============================================================

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None
        self.rotation_trace = []

    def get_height(self, node):
        return node.height if node else 0

    def balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def update_height(self, node):
        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

    def right_rotate(self, y):
        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        self.update_height(y)
        self.update_height(x)

        self.rotation_trace.append("Right Rotation")
        return x

    def left_rotate(self, x):
        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        self.update_height(x)
        self.update_height(y)

        self.rotation_trace.append("Left Rotation")
        return y

    def insert_node(self, node, key):
        if node is None:
            return AVLNode(key)

        if key < node.key:
            node.left = self.insert_node(node.left, key)
        elif key > node.key:
            node.right = self.insert_node(node.right, key)
        else:
            return node

        self.update_height(node)
        b = self.balance(node)

        if b > 1 and key < node.left.key:
            self.rotation_trace.append("LL Case")
            return self.right_rotate(node)

        if b < -1 and key > node.right.key:
            self.rotation_trace.append("RR Case")
            return self.left_rotate(node)

        if b > 1 and key > node.left.key:
            self.rotation_trace.append("LR Case")
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if b < -1 and key < node.right.key:
            self.rotation_trace.append("RL Case")
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def insert(self, key):
        self.root = self.insert_node(self.root, key)
        self.verify()

    def minimum(self, node):
        while node.left:
            node = node.left
        return node

    def delete_node(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self.delete_node(node.left, key)
        elif key > node.key:
            node.right = self.delete_node(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            temp = self.minimum(node.right)
            node.key = temp.key
            node.right = self.delete_node(node.right, temp.key)

        self.update_height(node)
        b = self.balance(node)

        if b > 1 and self.balance(node.left) >= 0:
            self.rotation_trace.append("LL Delete Case")
            return self.right_rotate(node)

        if b > 1 and self.balance(node.left) < 0:
            self.rotation_trace.append("LR Delete Case")
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if b < -1 and self.balance(node.right) <= 0:
            self.rotation_trace.append("RR Delete Case")
            return self.left_rotate(node)

        if b < -1 and self.balance(node.right) > 0:
            self.rotation_trace.append("RL Delete Case")
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def delete(self, key):
        self.root = self.delete_node(self.root, key)
        self.verify()

    def verify(self):
        def check(node, low, high):
            if node is None:
                return 0

            if not (low < node.key < high):
                raise ValueError("BST property violated.")

            left_height = check(node.left, low, node.key)
            right_height = check(node.right, node.key, high)

            expected = 1 + max(left_height, right_height)

            if node.height != expected:
                raise ValueError("Stored height is incorrect.")

            if abs(left_height - right_height) > 1:
                raise ValueError("AVL balance property violated.")

            return expected

        check(self.root, float("-inf"), float("inf"))
        return True

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def height(self):
        return self.get_height(self.root)


# ============================================================
# 6. EXPRESSION TREE
# Postfix input, evaluation and infix conversion
# ============================================================

class ExpressionNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ExpressionTree:
    OPERATORS = {"+", "-", "*", "/"}

    def build(self, postfix):
        stack = []

        for token in postfix.split():
            if token in self.OPERATORS:
                if len(stack) < 2:
                    raise ValueError("Operand shortage in postfix expression.")

                node = ExpressionNode(token)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
            else:
                try:
                    float(token)
                except ValueError:
                    raise ValueError("Invalid operand: " + token)

                stack.append(ExpressionNode(token))

        if len(stack) != 1:
            raise ValueError("Invalid postfix expression.")

        return stack[0]

    def evaluate(self, node):
        if node.left is None and node.right is None:
            return float(node.value)

        a = self.evaluate(node.left)
        b = self.evaluate(node.right)

        if node.value == "+":
            return a + b
        if node.value == "-":
            return a - b
        if node.value == "*":
            return a * b
        if node.value == "/":
            if b == 0:
                raise ZeroDivisionError("Division by zero.")
            return a / b

    def infix(self, node):
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

        def render(current):
            if current.left is None and current.right is None:
                return current.value, 3
            left_text, left_prec = render(current.left)
            right_text, right_prec = render(current.right)
            op, prec = current.value, precedence[current.value]
            if left_prec < prec:
                left_text = "(" + left_text + ")"
            if right_prec < prec or (right_prec == prec and op in ("-", "/")):
                right_text = "(" + right_text + ")"
            return left_text + " " + op + " " + right_text, prec

        return render(node)[0]


class FamilyGraph:
    def __init__(self, directed=False, weighted=False):
        self.directed = directed
        self.weighted = weighted
        self.vertices = {}
        self.adj = {}
        self.representation = "list"

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = True
            self.adj[vertex] = []

    def add_edge(self, u, v, weight=1):
        self.add_vertex(u)
        self.add_vertex(v)

        self.adj[u].append((v, weight))

        if not self.directed:
            self.adj[v].append((u, weight))

    def adjacency_matrix(self):
        nodes = list(self.vertices)
        matrix = [[0 for _ in nodes] for _ in nodes]

        for i, u in enumerate(nodes):
            for v, weight in self.adj[u]:
                j = nodes.index(v)
                matrix[i][j] = weight

        return nodes, matrix

    def set_representation(self, mode):
        if mode not in ("list", "matrix"):
            raise ValueError("Choose list or matrix.")
        self.representation = mode
        print("Graph representation switched to", mode.upper())

    def show_current_representation(self):
        if self.representation == "matrix":
            self.show_matrix()
        else:
            self.show_list()

    def memory_comparison(self):
        nodes, matrix = self.adjacency_matrix()
        matrix_cells = len(nodes) * len(nodes)
        list_entries = sum(len(edges) for edges in self.adj.values())
        print("Adjacency matrix cells:", matrix_cells)
        print("Adjacency-list edge entries:", list_entries)
        print("Space complexity: matrix O(V^2), list O(V + E)")
        return matrix_cells, list_entries

    def show_matrix(self):
        nodes, matrix = self.adjacency_matrix()
        print("Vertices:", nodes)

        for row in matrix:
            print(row)

    def show_list(self):
        for vertex in self.adj:
            print(vertex, "->", self.adj[vertex])

    def bfs(self, start, target=None):
        if start not in self.adj:
            print("Starting member not found.")
            return []

        queue = deque([start])
        visited = {start}
        parent = {start: None}
        order = []

        while queue:
            u = queue.popleft()
            order.append(u)

            if u == target:
                break

            for v, weight in self.adj[u]:
                if v not in visited:
                    visited.add(v)
                    parent[v] = u
                    queue.append(v)

        print("BFS order:", order)

        if target is not None:
            if target not in parent:
                print("No route found.")
            else:
                path = []
                current = target

                while current is not None:
                    path.append(current)
                    current = parent[current]

                path.reverse()
                print("Fewest-stop route:", path)
                print("Number of edges:", len(path) - 1)

        return order

    def dfs(self, start):
        visited = set()
        discovery = {}
        finish = {}
        parent = {}
        edge_types = []
        clock = [0]

        def visit(u):
            visited.add(u)
            clock[0] += 1
            discovery[u] = clock[0]

            for v, weight in self.adj[u]:
                if v not in visited:
                    parent[v] = u
                    edge_types.append((u, v, "Tree"))
                    visit(v)
                elif v not in finish:
                    edge_types.append((u, v, "Back"))
                elif discovery[u] < discovery[v]:
                    edge_types.append((u, v, "Forward/Cross"))
                else:
                    edge_types.append((u, v, "Cross"))

            clock[0] += 1
            finish[u] = clock[0]

        if start in self.adj:
            visit(start)

        for vertex in self.adj:
            if vertex not in visited:
                visit(vertex)

        print("Discovery times:", discovery)
        print("Finish times:", finish)
        print("DFS edges:", edge_types)

        return visited

    def connected_components(self):
        visited = set()
        components = []

        for vertex in self.adj:
            if vertex not in visited:
                component = []
                queue = deque([vertex])
                visited.add(vertex)

                while queue:
                    u = queue.popleft()
                    component.append(u)

                    for v, weight in self.adj[u]:
                        if v not in visited:
                            visited.add(v)
                            queue.append(v)

                components.append(component)

        print("Connected components:", components)
        return components

    def strongly_connected_components(self):
        visited = set()
        order = []

        def dfs1(u):
            visited.add(u)
            for v, w in self.adj[u]:
                if v not in visited:
                    dfs1(v)
            order.append(u)

        for vertex in self.adj:
            if vertex not in visited:
                dfs1(vertex)

        reverse = {v: [] for v in self.adj}

        for u in self.adj:
            for v, w in self.adj[u]:
                reverse[v].append(u)

        visited.clear()
        components = []

        def dfs2(u, component):
            visited.add(u)
            component.append(u)

            for v in reverse[u]:
                if v not in visited:
                    dfs2(v, component)

        for u in reversed(order):
            if u not in visited:
                component = []
                dfs2(u, component)
                components.append(component)

        print("Strongly connected components:", components)
        return components

    def dijkstra(self, start, target):
        vertices = list(self.adj)

        if start not in self.adj or target not in self.adj:
            print("Invalid member.")
            return

        if any(weight < 0 for edges in self.adj.values() for _, weight in edges):
            print("Dijkstra cannot handle negative edge weights.")
            return None

        distance = {v: float("inf") for v in vertices}
        parent = {v: None for v in vertices}
        visited = set()
        distance[start] = 0

        for step in range(len(vertices)):
            current = None
            best = float("inf")

            for v in vertices:
                if v not in visited and distance[v] < best:
                    best = distance[v]
                    current = v

            if current is None:
                break

            visited.add(current)

            for neighbour, weight in self.adj[current]:
                if weight < 0:
                    print("Dijkstra cannot handle negative weights.")
                    return

                new_distance = distance[current] + weight

                if new_distance < distance[neighbour]:
                    distance[neighbour] = new_distance
                    parent[neighbour] = current

            print("Step", step + 1, ":", distance)

        if distance[target] == float("inf"):
            print("No route exists.")
            return

        path = []
        current = target

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()
        print("Shortest path:", path)
        print("Total distance:", distance[target])

    def prim(self):
        vertices = list(self.adj)
        visited = set()
        forest = []
        total = 0

        for start in vertices:
            if start in visited:
                continue

            visited.add(start)

            while True:
                best_edge = None
                best_weight = float("inf")

                for u in visited:
                    for v, weight in self.adj[u]:
                        if v not in visited and weight < best_weight:
                            best_weight = weight
                            best_edge = (u, v, weight)

                if best_edge is None:
                    break

                u, v, weight = best_edge
                visited.add(v)
                forest.append(best_edge)
                total += weight

        print("Prim minimum spanning forest:", forest)
        print("Prim total cost:", total)
        return total

    def kruskal(self):
        vertices = list(self.adj)
        parent = {v: v for v in vertices}
        rank = {v: 0 for v in vertices}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            if rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            elif rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            else:
                parent[root_b] = root_a
                rank[root_a] += 1

            return True

        edges = []

        for u in self.adj:
            for v, weight in self.adj[u]:
                if self.directed:
                    continue
                if str(u) < str(v):
                    edges.append((weight, u, v))

        # Own insertion sort for edges
        for i in range(1, len(edges)):
            key = edges[i]
            j = i - 1

            while j >= 0 and edges[j][0] > key[0]:
                edges[j + 1] = edges[j]
                j -= 1

            edges[j + 1] = key

        result = []
        total = 0

        for weight, u, v in edges:
            if union(u, v):
                result.append((u, v, weight))
                total += weight

        print("Kruskal minimum spanning forest:", result)
        print("Kruskal total cost:", total)
        return total


# ============================================================
# 8. SAMPLE FAMILY RELATIONSHIP GRAPH
# ============================================================

def create_family_graph():
    graph = FamilyGraph(directed=False, weighted=True)

    for member_id, name, parent_id in FAMILY_DATA:
        graph.add_vertex(name)

    for member_id, name, parent_id in FAMILY_DATA:
        if parent_id is not None:
            parent_name = next(
                item[1] for item in FAMILY_DATA if item[0] == parent_id
            )
            graph.add_edge(parent_name, name, 1)

    # A disconnected family branch for testing connectivity
    graph.add_vertex("Unknown Relative")
    graph.add_vertex("Distant Cousin")
    graph.add_edge("Unknown Relative", "Distant Cousin", 2)

    return graph


# ============================================================
# 9. TOPOLOGICAL SORT
# Kahn's algorithm and DFS method
# ============================================================

def topological_kahn(graph):
    indegree = {v: 0 for v in graph.adj}

    for u in graph.adj:
        for v, weight in graph.adj[u]:
            indegree[v] += 1

    queue = deque([v for v in indegree if indegree[v] == 0])
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)

        for v, weight in graph.adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    if len(order) != len(graph.adj):
        print("Cycle detected. Topological order is not possible.")
    else:
        print("Kahn topological order:", order)

    return order


def topological_dfs(graph):
    visited = set()
    active = set()
    order = []
    cycle_found = False

    def visit(u):
        nonlocal cycle_found

        visited.add(u)
        active.add(u)

        for v, weight in graph.adj[u]:
            if v in active:
                cycle_found = True
            elif v not in visited:
                visit(v)

        active.remove(u)
        order.append(u)

    for vertex in graph.adj:
        if vertex not in visited:
            visit(vertex)

    if cycle_found:
        print("Cycle detected by DFS.")
        return []

    order.reverse()
    print("DFS topological order:", order)
    return order


# ============================================================
# 10. TESTING - 21 AUTOMATED TESTS
# ============================================================

def run_tests():
    print("\\n========== AUTOMATED TESTS ==========")
    passed = 0
    total = 21

    def test(condition, description):
        nonlocal passed
        if condition:
            print("PASS:", description)
            passed += 1
        else:
            print("FAIL:", description)

    family = FamilyTree()
    test(len(family.members) == 15, "Exactly 15 family members")
    test(family.root.name == "Arun", "Root member is Arun")
    test(len(family.root.children) == 3, "Root has three children")

    binary = BinaryFamilyTree()
    test(binary.height(binary.root) > 0, "Binary tree height")
    test(binary.find_node(binary.root, 15).name == "Tara", "Binary tree member search")
    test(all(binary.find_node(binary.root, i) for i in range(1, 16)),
         "All 15 members exist in binary tree")
    test(binary.lca(binary.root, 9, 10).member_id == 5, "Lowest common ancestor")

    bst = BinarySearchTree()
    for x in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(x)
    test(bst.search(40), "BST search existing key")
    test(not bst.search(100), "BST search missing key")
    bst.delete(20)
    test(not bst.search(20), "BST delete leaf")
    bst.delete(30)
    test(not bst.search(30), "BST delete one-child node")
    bst.delete(70)
    test(not bst.search(70), "BST delete two-child node")
    test(bst.minimum_node(bst.root).key == 40 and
         bst.maximum_node(bst.root).key == 80, "BST minimum and maximum")

    avl = AVLTree()
    for x in [30, 20, 10, 40, 50, 25]:
        avl.insert(x)
    test(avl.verify(), "AVL verification after insertion")
    avl.delete(20)
    test(avl.verify(), "AVL verification after deletion")

    graph = FamilyGraph()
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    test(len(graph.bfs("A")) == 3, "BFS traversal")
    graph.set_representation("matrix")
    test(len(graph.adjacency_matrix()[1]) == 3, "Adjacency matrix conversion")

    expr = ExpressionTree()
    test(expr.evaluate(expr.build("5 3 +")) == 8, "Expression tree evaluation")
    test(expr.infix(expr.build("2 3 4 * +")) == "2 + 3 * 4",
         "Minimal-parentheses infix")

    directed = FamilyGraph(directed=True)
    directed.add_edge("A", "B")
    directed.add_edge("B", "A")
    test(len(topological_kahn(directed)) == 0, "Topological cycle detection")

    mst = FamilyGraph()
    mst.add_edge("A", "B", 1)
    mst.add_edge("B", "C", 2)
    mst.add_edge("A", "C", 4)
    test(mst.prim() == mst.kruskal(), "Prim and Kruskal MST costs agree")

    print("\\nTests passed:", passed, "/", total)
    print("Tests failed:", total - passed)


def random_avl_test():
    print("\nRunning 10,000 random AVL operations...")

    random.seed(42)
    tree = AVLTree()
    values = list(range(1, 10001))
    random.shuffle(values)

    for value in values:
        tree.insert(value)

    for value in values[:5000]:
        tree.delete(value)

    print("AVL random test completed.")
    print("AVL verification:", tree.verify())
    print("Final AVL height:", tree.height())


# ============================================================
# 12. BST VS AVL HEIGHT EXPERIMENT
# ============================================================

def height_experiment():
    print("\n========== HEIGHT COMPARISON ==========")

    bst = BinarySearchTree()
    avl = AVLTree()

    for key in range(1, 1001):
        bst.insert(key)
        avl.insert(key)

    print("Number of sorted keys: 1000")
    print("BST height:", bst.height(bst.root))
    print("AVL height:", avl.height())


# ============================================================
# 13. TIMING EXPERIMENT
# ============================================================

def timing_experiment():
    print("\n========== TIMING EXPERIMENT ==========")

    for size in [1000, 5000, 20000]:
        values = list(range(size))
        random.seed(42)
        random.shuffle(values)

        tree = AVLTree()
        start = time.perf_counter()

        for value in values:
            tree.insert(value)

        elapsed = time.perf_counter() - start

        print("AVL insertion:", size, "keys")
        print("Time:", round(elapsed, 6), "seconds")
        print("Height:", tree.height())


# ============================================================
# 14. EXPRESSION TREE DEMONSTRATION
# ============================================================

def expression_demo():
    print("\n========== EXPRESSION TREE ==========")

    print("Example postfix expression: 10 5 * 2 +")

    tree = ExpressionTree()
    root = tree.build("10 5 * 2 +")

    print("Infix expression:", tree.infix(root))
    print("Evaluated result:", tree.evaluate(root))


# ============================================================
# 15. MAIN MENU
# ============================================================

def main():
    family = FamilyTree()
    binary = BinaryFamilyTree()
    bst = BinarySearchTree()
    avl = AVLTree()
    graph = create_family_graph()

    # Add the 15 family member IDs to BST and AVL
    for member_id, name, parent_id in FAMILY_DATA:
        bst.insert(member_id)
        avl.insert(member_id)

    while True:
        print("\n======================================")
        print("       FAMILY TREE EXPLORER")
        print("======================================")
        print("1. Display Family Tree")
        print("2. Add Family Member")
        print("3. Delete Family Subtree")
        print("4. General Tree Traversals")
        print("5. Binary Tree Traversals")
        print("6. Lowest Common Ancestor")
        print("7. BST Operations")
        print("8. AVL Operations")
        print("9. BFS Relationship Distance")
        print("10. DFS Connected Branches")
        print("11. Show Graph Representations")
        print("12. Dijkstra Shortest Route")
        print("13. Prim and Kruskal")
        print("14. Expression Tree")
        print("15. Topological Sort Demonstration")
        print("16. Run Automated Tests")
        print("17. Run Random AVL Test")
        print("18. BST vs AVL Height")
        print("19. Timing Experiment")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            family.display()

        elif choice == "2":
            parent_id = int(input("Enter parent ID: "))
            member_id = int(input("Enter new member ID: "))
            name = input("Enter member name: ")
            family.add_member(parent_id, member_id, name)

            # Keep indexes updated
            if member_id in family.members:
                bst.insert(member_id)
                avl.insert(member_id)

        elif choice == "3":
            member_id = int(input("Enter member ID to delete: "))

            if member_id == 1:
                print("Root cannot be deleted.")
            elif member_id not in family.members:
                print("Member not found.")
            else:
                to_delete = []

                def collect(node):
                    to_delete.append(node.member_id)
                    for child in node.children:
                        collect(child)

                collect(family.members[member_id])
                family.delete_subtree(member_id)

                for deleted_id in to_delete:
                    bst.delete(deleted_id)
                    avl.delete(deleted_id)

                print("Deleted members:", to_delete)

        elif choice == "4":
            print("1. Recursive preorder")
            print("2. Recursive postorder")
            print("3. Level order")
            print("4. Iterative preorder")
            print("5. Iterative postorder")

            sub = input("Choose traversal: ")

            if sub == "1":
                family.preorder()
            elif sub == "2":
                family.postorder()
            elif sub == "3":
                family.level_order()
            elif sub == "4":
                family.iterative_preorder()
            elif sub == "5":
                family.iterative_postorder()

            print()

        elif choice == "5":
            print("1. Recursive inorder")
            print("2. Recursive preorder")
            print("3. Recursive postorder")
            print("4. Recursive level order")
            print("5. Iterative inorder")
            print("6. Iterative preorder")
            print("7. Iterative postorder")
            print("8. Iterative level order")

            sub = input("Choose traversal: ")

            if sub == "1":
                binary.inorder_recursive(binary.root)
            elif sub == "2":
                binary.preorder_recursive(binary.root)
            elif sub == "3":
                binary.postorder_recursive(binary.root)
            elif sub == "4":
                binary.level_recursive()
            elif sub == "5":
                binary.inorder_iterative()
            elif sub == "6":
                binary.preorder_iterative()
            elif sub == "7":
                binary.postorder_iterative()
            elif sub == "8":
                binary.level_iterative()

            print()

        elif choice == "6":
            id1 = int(input("Enter first member ID: "))
            id2 = int(input("Enter second member ID: "))
            binary.lowest_common_ancestor(id1, id2)

        elif choice == "7":
            print("1. Search")
            print("2. Delete")
            print("3. Minimum and Maximum")
            print("4. Successor and Predecessor")
            print("5. Range Query")
            print("6. Display inorder")

            sub = input("Choose BST operation: ")

            if sub == "1":
                key = int(input("Enter ID: "))
                print("Found" if bst.search(key) else "Not found")

            elif sub == "2":
                key = int(input("Enter ID: "))
                bst.delete(key)
                print("Deleted if the ID existed.")

            elif sub == "3":
                if bst.root:
                    print("Minimum:", bst.minimum_node(bst.root).key)
                    print("Maximum:", bst.maximum_node(bst.root).key)

            elif sub == "4":
                key = int(input("Enter ID: "))
                print("Successor:", bst.successor(key))
                print("Predecessor:", bst.predecessor(key))

            elif sub == "5":
                low = int(input("Enter lower ID: "))
                high = int(input("Enter upper ID: "))
                bst.range_query(bst.root, low, high)
                print()

            elif sub == "6":
                bst.inorder(bst.root)
                print()

        elif choice == "8":
            print("1. Insert AVL member ID")
            print("2. Delete AVL member ID")
            print("3. Display inorder")
            print("4. Verify AVL")
            print("5. Show rotation trace")

            sub = input("Choose AVL operation: ")

            if sub == "1":
                key = int(input("Enter ID: "))
                avl.insert(key)
                print("Inserted.")

            elif sub == "2":
                key = int(input("Enter ID: "))
                avl.delete(key)
                print("Deleted.")

            elif sub == "3":
                avl.inorder(avl.root)
                print()

            elif sub == "4":
                print("AVL valid:", avl.verify())

            elif sub == "5":
                print(avl.rotation_trace)

        elif choice == "9":
            start = input("Enter starting member name: ")
            target = input("Enter target member name: ")
            graph.bfs(start, target)

        elif choice == "10":
            start = input("Enter starting member name: ")
            graph.dfs(start)
            graph.connected_components()

        elif choice == "11":
            print("Current representation:", graph.representation.upper())
            print("1. Switch to Adjacency List")
            print("2. Switch to Adjacency Matrix")
            print("3. Display Current Representation")
            print("4. Compare Storage")
            sub = input("Choose option: ")
            if sub == "1":
                graph.set_representation("list")
                graph.show_current_representation()
            elif sub == "2":
                graph.set_representation("matrix")
                graph.show_current_representation()
            elif sub == "3":
                graph.show_current_representation()
            elif sub == "4":
                graph.memory_comparison()

        elif choice == "12":
            start = input("Enter source member: ")
            target = input("Enter destination member: ")
            graph.dijkstra(start, target)

        elif choice == "13":
            prim_cost = graph.prim()
            kruskal_cost = graph.kruskal()

            print("MST costs match:", prim_cost == kruskal_cost)

        elif choice == "14":
            expression_demo()

        elif choice == "15":
            schedule = FamilyGraph(directed=True)
            schedule.add_edge("Birth", "Child")
            schedule.add_edge("Child", "Grandchild")
            schedule.add_edge("Birth", "Relative")
            topological_kahn(schedule)
            topological_dfs(schedule)

        elif choice == "16":
            run_tests()

        elif choice == "17":
            random_avl_test()

        elif choice == "18":
            height_experiment()

        elif choice == "19":
            timing_experiment()

        elif choice == "0":
            print("Thank you for using Family Tree Explorer!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
