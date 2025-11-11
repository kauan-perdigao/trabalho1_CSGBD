from __future__ import annotations
from typing import List, Optional, Any


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

