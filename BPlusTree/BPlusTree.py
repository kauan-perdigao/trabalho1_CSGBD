from __future__ import annotations
from typing import List, Optional, Any, Tuple
import math


class _Node:
    def __init__(self, is_leaf: bool = False):
        self.is_leaf = is_leaf
        self.keys: List[int] = []
        self.values: List[Any] = [] 
        self.children: List[_Node] = [] 
        self.next: Optional[_Node] = None  


class BPlusTree:
    
    def __init__(self, order: int = 4):
        if order < 3:
            raise ValueError("order deve ser >= 3")
        self.order = order
        self.root = _Node(is_leaf=True)

    def _find_leaf(self, key: int) -> _Node:
        node = self.root
        while not node.is_leaf:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            node = node.children[i]
        return node

    def search(self, key: int) -> Optional[Any]:
        """Retorna o valor associado à chave, ou None se não existir."""
        leaf = self._find_leaf(key)
        for i, k in enumerate(leaf.keys):
            if k == key:
                return leaf.values[i]
        return None

    def insert(self, key: int, value: Any):
        leaf = self._find_leaf(key)
        for i, k in enumerate(leaf.keys):
            if k == key:
                leaf.values[i] = value
                return
            if key < k:
                leaf.keys.insert(i, key)
                leaf.values.insert(i, value)
                break
        else:
            leaf.keys.append(key)
            leaf.values.append(value)

        if len(leaf.keys) > self.order:
            self._split_leaf(leaf)

    def _split_leaf(self, leaf: _Node):
        mid = (len(leaf.keys) + 1) // 2
        new_leaf = _Node(is_leaf=True)
        new_leaf.keys = leaf.keys[mid:]
        new_leaf.values = leaf.values[mid:]
        leaf.keys = leaf.keys[:mid]
        leaf.values = leaf.values[:mid]
        new_leaf.next = leaf.next
        leaf.next = new_leaf

        promote_key = new_leaf.keys[0]
        self._insert_in_parent(leaf, promote_key, new_leaf)

    def _insert_in_parent(self, node: _Node, key: int, new_node: _Node):
        if node is self.root:
            new_root = _Node(is_leaf=False)
            new_root.keys = [key]
            new_root.children = [node, new_node]
            self.root = new_root
            return

        parent, parent_index = self._find_parent(self.root, node)
        insert_pos = parent_index + 1
        parent.children.insert(insert_pos, new_node)
        parent.keys.insert(parent_index, key)

        if len(parent.keys) > self.order:
            self._split_internal(parent)

    def _split_internal(self, node: _Node):
        mid_index = len(node.keys) // 2
        promote_key = node.keys[mid_index]

        new_node = _Node(is_leaf=False)
        new_node.keys = node.keys[mid_index + 1 :]
        new_node.children = node.children[mid_index + 1 :]

        node.keys = node.keys[:mid_index]
        node.children = node.children[: mid_index + 1]

        if node is self.root:
            new_root = _Node(is_leaf=False)
            new_root.keys = [promote_key]
            new_root.children = [node, new_node]
            self.root = new_root
            return

        parent, parent_index = self._find_parent(self.root, node)
        parent_index_insert = parent_index + 1
        parent.children.insert(parent_index_insert, new_node)
        parent.keys.insert(parent_index, promote_key)

        if len(parent.keys) > self.order:
            self._split_internal(parent)

    def _find_parent(self, current: _Node, child: _Node) -> Tuple[_Node, int]:
        """Retorna (parent_node, index_of_child_in_parent.children)"""
        if current.is_leaf or current.children[0].is_leaf and current.children[0] is child:
            for i, c in enumerate(current.children):
                if c is child:
                    return current, i

        for i, c in enumerate(current.children):
            if c is child:
                return current, i
            if not c.is_leaf:
                res = self._find_parent(c, child)
                if res is not None:
                    return res

        for i, c in enumerate(current.children):
            if not c.is_leaf:
                parent = self._search_parent_recursive(c, child)
                if parent is not None:
                    return parent

        raise RuntimeError("Parent not found")

    def _search_parent_recursive(self, node: _Node, child: _Node) -> Optional[Tuple[_Node, int]]:
        for i, c in enumerate(node.children):
            if c is child:
                return node, i
            if not c.is_leaf:
                res = self._search_parent_recursive(c, child)
                if res:
                    return res
        return None

    def remove(self, key: int) -> bool:
        leaf = self._find_leaf(key)
        for i, k in enumerate(leaf.keys):
            if k == key:
                del leaf.keys[i]
                del leaf.values[i]
                self._rebalance_after_delete(leaf)
                return True
        return False

    def _rebalance_after_delete(self, node: _Node):
        if node is self.root:
            if not node.is_leaf and len(node.children) == 1:
                self.root = node.children[0]
            return

        min_keys = math.ceil(self.order / 2)
        if node.is_leaf:
            if len(node.keys) >= min_keys:
                return
        else:
            min_children = math.ceil((self.order + 1) / 2)
            if len(node.children) >= min_children:
                return

        parent, idx = self._find_parent(self.root, node)

        left_sib = parent.children[idx - 1] if idx - 1 >= 0 else None
        right_sib = parent.children[idx + 1] if idx + 1 < len(parent.children) else None

        if left_sib and self._can_lend(left_sib):
            self._borrow_from_left(parent, idx, left_sib, node)
            return
        if right_sib and self._can_lend(right_sib):
            self._borrow_from_right(parent, idx, right_sib, node)
            return

        if left_sib:
            self._merge_nodes(parent, idx - 1)
        elif right_sib:
            self._merge_nodes(parent, idx)

    def _can_lend(self, node: _Node) -> bool:
        if node.is_leaf:
            return len(node.keys) > math.ceil(self.order / 2)
        else:
            return len(node.children) > math.ceil((self.order + 1) / 2)
