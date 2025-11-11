"""
Author: Kauan Perdigão

Desenvolvido com ajuda de LLM (copilot)
"""

from BPlusTree import BPlusTree
import math


def _display(tree: BPlusTree):
    """Imprime uma visão simples da árvore: níveis e cadeia de folhas."""
    print("\n" + "="*60)
    print("B+ TREE STRUCTURE")
    print("="*60)

    # Imprimir níveis (BFS)
    level = [tree.root]
    depth = 0
    while level:
        print(f"\nLevel {depth}:", end=" ")
        next_level = []
        for node in level:
            if node.is_leaf:
                print(f"Leaf(keys={node.keys})", end=" ")
            else:
                print(f"Node(keys={node.keys})", end=" ")
                next_level.extend(node.children)
        print("")
        level = next_level
        depth += 1

    # Imprimir cadeia de folhas
    print("\nLeaf chain:")
    node = tree.root
    # desça até primeira folha
    while not node.is_leaf:
        node = node.children[0]
    idx = 0
    while node:
        print(f"  Leaf #{idx} keys: {node.keys}, values: {node.values}")
        node = node.next
        idx += 1


def test_basic_operations():
    print("\n" + "="*70)
    print("TEST 1: Basic Operations (Insert and Search)")
    print("="*70)

    t = BPlusTree(order=4)

    print("\nInserting keys: 1, 2, 3, 4...")
    t.insert(1, 100)
    print("  → Inserted (1, 100)")
    t.insert(2, 200)
    print("  → Inserted (2, 200)")
    t.insert(3, 300)
    print("  → Inserted (3, 300)")
    t.insert(4, 400)
    print("  → Inserted (4, 400)")

    _display(t)

    print("\nSearching for keys:")
    for key in [1, 2, 3, 4, 5]:
        result = t.search(key)
        print(f"  Key {key}: {result if result is not None else 'Not found'}")


def test_splits_and_growth():
    print("\n" + "="*70)
    print("TEST 2: Insertions Causing Splits and Growth")
    print("="*70)

    t = BPlusTree(order=3)
    keys = [10, 20, 5, 6, 12, 30, 7]
    print(f"\nInserting keys: {keys}")
    for k in keys:
        t.insert(k, k * 10)
        print(f"  → Inserted ({k}, {k*10})")

    _display(t)


def test_removal_and_merge():
    print("\n" + "="*70)
    print("TEST 3: Removal and Rebalancing")
    print("="*70)

    t = BPlusTree(order=4)
    print("\nInserting keys: 1-10...")
    for i in range(1, 11):
        t.insert(i, i * 100)
    _display(t)

    print("\nRemoving keys: 2, 4, 6, 8...")
    for key in [2, 4, 6, 8]:
        result = t.remove(key)
        print(f"  Removed key {key}: {result}")

    _display(t)

    print("\nSearching after removal:")
    for key in [1, 2, 3, 4, 5]:
        result = t.search(key)
        print(f"  Key {key}: {result if result is not None else 'Not found'}")


def test_random_sequence():
    print("\n" + "="*70)
    print("TEST 4: Complex Sequence (Simulating Real Usage)")
    print("="*70)

    t = BPlusTree(order=4)
    test_keys = [15, 7, 23, 4, 11, 30, 19, 2, 45, 8,
                 33, 12, 27, 50, 6, 41, 18, 3, 36, 25]

    print(f"\nInserting keys: {test_keys[:10]}...")
    for key in test_keys[:10]:
        t.insert(key, key * 10)
    _display(t)

    print(f"\nInserting more keys: {test_keys[10:]}...")
    for key in test_keys[10:]:
        t.insert(key, key * 10)
    _display(t)

    print("\nSearching for some keys:")
    search_keys = [15, 7, 100, 23, 99, 45]
    for key in search_keys:
        result = t.search(key)
        status = f"Found: {result}" if result is not None else "Not found"
        print(f"  Key {key}: {status}")

    print("\nRemoving some keys: [15, 7, 23, 4, 11]...")
    for key in [15, 7, 23, 4, 11]:
        t.remove(key)
    _display(t)


def test_update_values():
    print("\n" + "="*70)
    print("TEST 5: Updating Values")
    print("="*70)

    t = BPlusTree(order=4)
    print("\nInserting keys 1-5...")
    for i in range(1, 6):
        t.insert(i, i * 100)

    print("\nBefore update:")
    for i in range(1, 6):
        print(f"  Key {i}: {t.search(i)}")

    print("\nUpdating key 3 to new value 999...")
    t.insert(3, 999)

    print("\nAfter update:")
    for i in range(1, 6):
        print(f"  Key {i}: {t.search(i)}")

    _display(t)


def main():
    print("\n" + "#"*70)
    print("# B+ TREE - DEMONSTRATION AND TESTS")
    print("# Author: Kauan Perdigão")
    print("# Course: CSGBD - UFC")
    print("#"*70)

    test_basic_operations()
    test_splits_and_growth()
    test_removal_and_merge()
    test_random_sequence()
    test_update_values()

    print("\n" + "#"*70)
    print("# ALL TESTS COMPLETED")
    print("#"*70 + "\n")


if __name__ == "__main__":
    main()
