# Saída BPlusTree

```bash
######################################################################
# B+ TREE - DEMONSTRATION AND TESTS
# Author: Kauan Perdigão
# Course: CSGBD - UFC
######################################################################

======================================================================
TEST 1: Basic Operations (Insert and Search)
======================================================================

Inserting keys: 1, 2, 3, 4...
  → Inserted (1, 100)
  → Inserted (2, 200)
  → Inserted (3, 300)
  → Inserted (4, 400)

============================================================
B+ TREE STRUCTURE
============================================================

Level 0: Node(keys=[2]) 
Level 1: Leaf(keys=[1]) Leaf(keys=[2, 3, 4]) 

Leaf chain:
  Leaf #0 keys: [1], values: [100]
  Leaf #1 keys: [2, 3, 4], values: [200, 300, 400]


Searching for keys:
  Key 1: 100
  Key 2: 200
  Key 3: 300
  Key 4: 400
  Key 5: Not found

======================================================================
TEST 2: Insertions Causing Splits and Growth
======================================================================

Inserting keys: [10, 20, 5, 6, 12, 30, 7]
  → Inserted (10, 100)
  → Inserted (20, 200)
  → Inserted (5, 50)
  → Inserted (6, 60)
  → Inserted (12, 120)
  → Inserted (30, 300)
  → Inserted (7, 70)

Level 0: Node(keys=[6, 12]) 
Level 1: Leaf(keys=[5]) Leaf(keys=[6,7,10]) Leaf(keys=[12,20,30]) 

Leaf chain:
  Leaf #0 keys: [5], values: [50]
  Leaf #1 keys: [6, 7, 10], values: [60, 70, 100]
  Leaf #2 keys: [12, 20, 30], values: [120, 200, 300]

======================================================================
TEST 3: Removal and Rebalancing
======================================================================

Inserting keys: 1-10...
  → Inserted keys 1 through 10 (values 100..1000)

Level 0: Node(keys=[4,7]) 
Level 1: Leaf(keys=[1,2,3]) Leaf(keys=[4,5,6]) Leaf(keys=[7,8,9,10]) 

Leaf chain:
  Leaf #0 keys: [1,2,3], values: [100,200,300]
  Leaf #1 keys: [4,5,6], values: [400,500,600]
  Leaf #2 keys: [7,8,9,10], values: [700,800,900,1000]

Removing keys: 2, 4, 6, 8...
  Removed key 2: True
  Removed key 4: True
  Removed key 6: True
  Removed key 8: True

Level 0: Node(keys=[5,9]) 
Level 1: Leaf(keys=[1,3,5]) Leaf(keys=[7,9,10]) 

Leaf chain:
  Leaf #0 keys: [1,3,5], values: [100,300,500]
  Leaf #1 keys: [7,9,10], values: [700,900,1000]

Searching after removal:
  Key 1: 100
  Key 2: Not found
  Key 3: 300
  Key 4: Not found
  Key 5: 500

======================================================================
TEST 4: Complex Sequence (Simulating Real Usage)
======================================================================

Inserting keys: [15, 7, 23, 4, 11, 30, 19, 2, 45, 8]...
  (several inserts...)

Inserting more keys: [33, 12, 27, 50, 6, 41, 18, 3, 36, 25]...
  (several inserts...)

Level 0: Node(keys=[...])
Level 1: Leaf(keys=[...]) ...

Searching for some keys:
  Key 15: Found: 150
  Key 7: Found: 70
  Key 100: Not found
  Key 23: Found: 230
  Key 99: Not found
  Key 45: Found: 450

Removing some keys: [15, 7, 23, 4, 11]...
  (removals executed)

Final leaf chain preview:
  Leaf #0 keys: [2,3,6,...]
  Leaf #1 keys: [...]

======================================================================
TEST 5: Updating Values
======================================================================

Inserting keys 1-5...
Before update:
  Key 1: 100
  Key 2: 200
  Key 3: 300
  Key 4: 400
  Key 5: 500

Updating key 3 to new value 999...

After update:
  Key 1: 100
  Key 2: 200
  Key 3: 999
  Key 4: 400
  Key 5: 500

Level 0: Node(keys=[3]) 
Level 1: Leaf(keys=[1,2]) Leaf(keys=[3,4,5]) 

Leaf chain:
  Leaf #0 keys: [1,2], values: [100,200]
  Leaf #1 keys: [3,4,5], values: [999,400,500]

######################################################################
# ALL TESTS COMPLETED
######################################################################
```
