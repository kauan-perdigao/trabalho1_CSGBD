
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

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491463776 keys=[1] values=[100] len=1 next_id=None

Leaf details in physical order:
  [0] id=3491463776 keys=[1] values=[100] count=1

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (2, 200)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491463776 keys=[1, 2] values=[100, 200] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491463776 keys=[1, 2] values=[100, 200] count=2

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (3, 300)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491463776 keys=[1, 2, 3] values=[100, 200, 300] len=3 next_id=None

Leaf details in physical order:
  [0] id=3491463776 keys=[1, 2, 3] values=[100, 200, 300] count=3

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (4, 400)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491463776 keys=[1, 2, 3, 4] values=[100, 200, 300, 400] len=4 next_id=None

Leaf details in physical order:
  [0] id=3491463776 keys=[1, 2, 3, 4] values=[100, 200, 300, 400] count=4

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


============================================================
B+ TREE STRUCTURE
============================================================

Level 0: Leaf(keys=[1, 2, 3, 4]) 

Leaf chain:
  Leaf #0 keys: [1, 2, 3, 4], values: [100, 200, 300, 400]

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

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491463776 keys=[10] values=[100] len=1 next_id=None

Leaf details in physical order:
  [0] id=3491463776 keys=[10] values=[100] count=1

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (20, 200)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 20
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491463776 keys=[10, 20] values=[100, 200] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491463776 keys=[10, 20] values=[100, 200] count=2

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (5, 50)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491463776 keys=[5, 10, 20] values=[50, 100, 200] len=3 next_id=None

Leaf details in physical order:
  [0] id=3491463776 keys=[5, 10, 20] values=[50, 100, 200] count=3

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (6, 60)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466176 keys=[10] children_ids=[3491463776, 3491466128]

Level 1 (nodes=2):
  Leaf id=3491463776 keys=[5, 6] values=[50, 60] len=2 next_id=3491466128
  Leaf id=3491466128 keys=[10, 20] values=[100, 200] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491463776 keys=[5, 6] values=[50, 60] count=2
  [1] id=3491466128 keys=[10, 20] values=[100, 200] count=2

Total nodes visited (approx): 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (12, 120)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 12
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466176 keys=[10] children_ids=[3491463776, 3491466128]

Level 1 (nodes=2):
  Leaf id=3491463776 keys=[5, 6] values=[50, 60] len=2 next_id=3491466128
  Leaf id=3491466128 keys=[10, 12, 20] values=[100, 120, 200] len=3 next_id=None

Leaf details in physical order:
  [0] id=3491463776 keys=[5, 6] values=[50, 60] count=2
  [1] id=3491466128 keys=[10, 12, 20] values=[100, 120, 200] count=3

Total nodes visited (approx): 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (30, 300)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 30
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466176 keys=[10, 20] children_ids=[3491463776, 3491466128, 3489868704]

Level 1 (nodes=3):
  Leaf id=3491463776 keys=[5, 6] values=[50, 60] len=2 next_id=3491466128
  Leaf id=3491466128 keys=[10, 12] values=[100, 120] len=2 next_id=3489868704
  Leaf id=3489868704 keys=[20, 30] values=[200, 300] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491463776 keys=[5, 6] values=[50, 60] count=2
  [1] id=3491466128 keys=[10, 12] values=[100, 120] count=2
  [2] id=3489868704 keys=[20, 30] values=[200, 300] count=2

Total nodes visited (approx): 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (7, 70)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466176 keys=[10, 20] children_ids=[3491463776, 3491466128, 3489868704]

Level 1 (nodes=3):
  Leaf id=3491463776 keys=[5, 6, 7] values=[50, 60, 70] len=3 next_id=3491466128
  Leaf id=3491466128 keys=[10, 12] values=[100, 120] len=2 next_id=3489868704
  Leaf id=3489868704 keys=[20, 30] values=[200, 300] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491463776 keys=[5, 6, 7] values=[50, 60, 70] count=3
  [1] id=3491466128 keys=[10, 12] values=[100, 120] count=2
  [2] id=3489868704 keys=[20, 30] values=[200, 300] count=2

Total nodes visited (approx): 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


============================================================
B+ TREE STRUCTURE
============================================================

Level 0: Node(keys=[10, 20]) 

Level 1: Leaf(keys=[5, 6, 7]) Leaf(keys=[10, 12]) Leaf(keys=[20, 30]) 

Leaf chain:
  Leaf #0 keys: [5, 6, 7], values: [50, 60, 70]
  Leaf #1 keys: [10, 12], values: [100, 120]
  Leaf #2 keys: [20, 30], values: [200, 300]

======================================================================
TEST 3: Removal and Rebalancing
======================================================================

Inserting keys: 1-10...

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491466176 keys=[1] values=[100] len=1 next_id=None

Leaf details in physical order:
  [0] id=3491466176 keys=[1] values=[100] count=1

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491466176 keys=[1, 2] values=[100, 200] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491466176 keys=[1, 2] values=[100, 200] count=2

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491466176 keys=[1, 2, 3] values=[100, 200, 300] len=3 next_id=None

Leaf details in physical order:
  [0] id=3491466176 keys=[1, 2, 3] values=[100, 200, 300] count=3

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491466176 keys=[1, 2, 3, 4] values=[100, 200, 300, 400] len=4 next_id=None

Leaf details in physical order:
  [0] id=3491466176 keys=[1, 2, 3, 4] values=[100, 200, 300, 400] count=4

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491464352 keys=[4] children_ids=[3491466176, 3491463776]

Level 1 (nodes=2):
  Leaf id=3491466176 keys=[1, 2, 3] values=[100, 200, 300] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[4, 5] values=[400, 500] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491466176 keys=[1, 2, 3] values=[100, 200, 300] count=3
  [1] id=3491463776 keys=[4, 5] values=[400, 500] count=2

Total nodes visited (approx): 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491464352 keys=[4] children_ids=[3491466176, 3491463776]

Level 1 (nodes=2):
  Leaf id=3491466176 keys=[1, 2, 3] values=[100, 200, 300] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[4, 5, 6] values=[400, 500, 600] len=3 next_id=None

Leaf details in physical order:
  [0] id=3491466176 keys=[1, 2, 3] values=[100, 200, 300] count=3
  [1] id=3491463776 keys=[4, 5, 6] values=[400, 500, 600] count=3

Total nodes visited (approx): 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491464352 keys=[4] children_ids=[3491466176, 3491463776]

Level 1 (nodes=2):
  Leaf id=3491466176 keys=[1, 2, 3] values=[100, 200, 300] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[4, 5, 6, 7] values=[400, 500, 600, 700] len=4 next_id=None

Leaf details in physical order:
  [0] id=3491466176 keys=[1, 2, 3] values=[100, 200, 300] count=3
  [1] id=3491463776 keys=[4, 5, 6, 7] values=[400, 500, 600, 700] count=4

Total nodes visited (approx): 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491464352 keys=[4, 7] children_ids=[3491466176, 3491463776, 3489868704]

Level 1 (nodes=3):
  Leaf id=3491466176 keys=[1, 2, 3] values=[100, 200, 300] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[4, 5, 6] values=[400, 500, 600] len=3 next_id=3489868704
  Leaf id=3489868704 keys=[7, 8] values=[700, 800] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491466176 keys=[1, 2, 3] values=[100, 200, 300] count=3
  [1] id=3491463776 keys=[4, 5, 6] values=[400, 500, 600] count=3
  [2] id=3489868704 keys=[7, 8] values=[700, 800] count=2

Total nodes visited (approx): 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491464352 keys=[4, 7] children_ids=[3491466176, 3491463776, 3489868704]

Level 1 (nodes=3):
  Leaf id=3491466176 keys=[1, 2, 3] values=[100, 200, 300] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[4, 5, 6] values=[400, 500, 600] len=3 next_id=3489868704
  Leaf id=3489868704 keys=[7, 8, 9] values=[700, 800, 900] len=3 next_id=None

Leaf details in physical order:
  [0] id=3491466176 keys=[1, 2, 3] values=[100, 200, 300] count=3
  [1] id=3491463776 keys=[4, 5, 6] values=[400, 500, 600] count=3
  [2] id=3489868704 keys=[7, 8, 9] values=[700, 800, 900] count=3

Total nodes visited (approx): 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491464352 keys=[4, 7] children_ids=[3491466176, 3491463776, 3489868704]

Level 1 (nodes=3):
  Leaf id=3491466176 keys=[1, 2, 3] values=[100, 200, 300] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[4, 5, 6] values=[400, 500, 600] len=3 next_id=3489868704
  Leaf id=3489868704 keys=[7, 8, 9, 10] values=[700, 800, 900, 1000] len=4 next_id=None

Leaf details in physical order:
  [0] id=3491466176 keys=[1, 2, 3] values=[100, 200, 300] count=3
  [1] id=3491463776 keys=[4, 5, 6] values=[400, 500, 600] count=3
  [2] id=3489868704 keys=[7, 8, 9, 10] values=[700, 800, 900, 1000] count=4

Total nodes visited (approx): 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


============================================================
B+ TREE STRUCTURE
============================================================

Level 0: Node(keys=[4, 7]) 

Level 1: Leaf(keys=[1, 2, 3]) Leaf(keys=[4, 5, 6]) Leaf(keys=[7, 8, 9, 10]) 

Leaf chain:
  Leaf #0 keys: [1, 2, 3], values: [100, 200, 300]
  Leaf #1 keys: [4, 5, 6], values: [400, 500, 600]
  Leaf #2 keys: [7, 8, 9, 10], values: [700, 800, 900, 1000]

Removing keys: 2, 4, 6, 8...
  Removed key 2: True

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after remove 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491464352 keys=[4, 7] children_ids=[3491466176, 3491463776, 3489868704]

Level 1 (nodes=3):
  Leaf id=3491466176 keys=[1, 3] values=[100, 300] len=2 next_id=3491463776
  Leaf id=3491463776 keys=[4, 5, 6] values=[400, 500, 600] len=3 next_id=3489868704
  Leaf id=3489868704 keys=[7, 8, 9, 10] values=[700, 800, 900, 1000] len=4 next_id=None

Leaf details in physical order:
  [0] id=3491466176 keys=[1, 3] values=[100, 300] count=2
  [1] id=3491463776 keys=[4, 5, 6] values=[400, 500, 600] count=3
  [2] id=3489868704 keys=[7, 8, 9, 10] values=[700, 800, 900, 1000] count=4

Total nodes visited (approx): 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Removed key 4: True

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after remove 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491464352 keys=[4, 7] children_ids=[3491466176, 3491463776, 3489868704]

Level 1 (nodes=3):
  Leaf id=3491466176 keys=[1, 3] values=[100, 300] len=2 next_id=3491463776
  Leaf id=3491463776 keys=[5, 6] values=[500, 600] len=2 next_id=3489868704
  Leaf id=3489868704 keys=[7, 8, 9, 10] values=[700, 800, 900, 1000] len=4 next_id=None

Leaf details in physical order:
  [0] id=3491466176 keys=[1, 3] values=[100, 300] count=2
  [1] id=3491463776 keys=[5, 6] values=[500, 600] count=2
  [2] id=3489868704 keys=[7, 8, 9, 10] values=[700, 800, 900, 1000] count=4

Total nodes visited (approx): 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Removed key 6: True

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after remove 6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491464352 keys=[4, 8] children_ids=[3491466176, 3491463776, 3489868704]

Level 1 (nodes=3):
  Leaf id=3491466176 keys=[1, 3] values=[100, 300] len=2 next_id=3491463776
  Leaf id=3491463776 keys=[5, 7] values=[500, 700] len=2 next_id=3489868704
  Leaf id=3489868704 keys=[8, 9, 10] values=[800, 900, 1000] len=3 next_id=None

Leaf details in physical order:
  [0] id=3491466176 keys=[1, 3] values=[100, 300] count=2
  [1] id=3491463776 keys=[5, 7] values=[500, 700] count=2
  [2] id=3489868704 keys=[8, 9, 10] values=[800, 900, 1000] count=3

Total nodes visited (approx): 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Removed key 8: True

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after remove 8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491464352 keys=[4, 8] children_ids=[3491466176, 3491463776, 3489868704]

Level 1 (nodes=3):
  Leaf id=3491466176 keys=[1, 3] values=[100, 300] len=2 next_id=3491463776
  Leaf id=3491463776 keys=[5, 7] values=[500, 700] len=2 next_id=3489868704
  Leaf id=3489868704 keys=[9, 10] values=[900, 1000] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491466176 keys=[1, 3] values=[100, 300] count=2
  [1] id=3491463776 keys=[5, 7] values=[500, 700] count=2
  [2] id=3489868704 keys=[9, 10] values=[900, 1000] count=2

Total nodes visited (approx): 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


============================================================
B+ TREE STRUCTURE
============================================================

Level 0: Node(keys=[4, 8]) 

Level 1: Leaf(keys=[1, 3]) Leaf(keys=[5, 7]) Leaf(keys=[9, 10]) 

Leaf chain:
  Leaf #0 keys: [1, 3], values: [100, 300]
  Leaf #1 keys: [5, 7], values: [500, 700]
  Leaf #2 keys: [9, 10], values: [900, 1000]

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
  → Inserted (15, 150)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 15
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491464352 keys=[15] values=[150] len=1 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[15] values=[150] count=1

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (7, 70)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491464352 keys=[7, 15] values=[70, 150] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[7, 15] values=[70, 150] count=2

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (23, 230)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 23
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491464352 keys=[7, 15, 23] values=[70, 150, 230] len=3 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[7, 15, 23] values=[70, 150, 230] count=3

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (4, 40)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491464352 keys=[4, 7, 15, 23] values=[40, 70, 150, 230] len=4 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[4, 7, 15, 23] values=[40, 70, 150, 230] count=4

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (11, 110)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 11
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466128 keys=[15] children_ids=[3491464352, 3491463776]

Level 1 (nodes=2):
  Leaf id=3491464352 keys=[4, 7, 11] values=[40, 70, 110] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[15, 23] values=[150, 230] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[4, 7, 11] values=[40, 70, 110] count=3
  [1] id=3491463776 keys=[15, 23] values=[150, 230] count=2

Total nodes visited (approx): 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (30, 300)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 30
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466128 keys=[15] children_ids=[3491464352, 3491463776]

Level 1 (nodes=2):
  Leaf id=3491464352 keys=[4, 7, 11] values=[40, 70, 110] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[15, 23, 30] values=[150, 230, 300] len=3 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[4, 7, 11] values=[40, 70, 110] count=3
  [1] id=3491463776 keys=[15, 23, 30] values=[150, 230, 300] count=3

Total nodes visited (approx): 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (19, 190)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 19
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466128 keys=[15] children_ids=[3491464352, 3491463776]

Level 1 (nodes=2):
  Leaf id=3491464352 keys=[4, 7, 11] values=[40, 70, 110] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[15, 19, 23, 30] values=[150, 190, 230, 300] len=4 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[4, 7, 11] values=[40, 70, 110] count=3
  [1] id=3491463776 keys=[15, 19, 23, 30] values=[150, 190, 230, 300] count=4

Total nodes visited (approx): 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (2, 20)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466128 keys=[15] children_ids=[3491464352, 3491463776]

Level 1 (nodes=2):
  Leaf id=3491464352 keys=[2, 4, 7, 11] values=[20, 40, 70, 110] len=4 next_id=3491463776
  Leaf id=3491463776 keys=[15, 19, 23, 30] values=[150, 190, 230, 300] len=4 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 4, 7, 11] values=[20, 40, 70, 110] count=4
  [1] id=3491463776 keys=[15, 19, 23, 30] values=[150, 190, 230, 300] count=4

Total nodes visited (approx): 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (45, 450)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 45
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466128 keys=[15, 30] children_ids=[3491464352, 3491463776, 3489868704]

Level 1 (nodes=3):
  Leaf id=3491464352 keys=[2, 4, 7, 11] values=[20, 40, 70, 110] len=4 next_id=3491463776
  Leaf id=3491463776 keys=[15, 19, 23] values=[150, 190, 230] len=3 next_id=3489868704
  Leaf id=3489868704 keys=[30, 45] values=[300, 450] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 4, 7, 11] values=[20, 40, 70, 110] count=4
  [1] id=3491463776 keys=[15, 19, 23] values=[150, 190, 230] count=3
  [2] id=3489868704 keys=[30, 45] values=[300, 450] count=2

Total nodes visited (approx): 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (8, 80)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466128 keys=[8, 15, 30] children_ids=[3491464352, 3489868800, 3491463776, 3489868704]

Level 1 (nodes=4):
  Leaf id=3491464352 keys=[2, 4, 7] values=[20, 40, 70] len=3 next_id=3489868800
  Leaf id=3489868800 keys=[8, 11] values=[80, 110] len=2 next_id=3491463776
  Leaf id=3491463776 keys=[15, 19, 23] values=[150, 190, 230] len=3 next_id=3489868704
  Leaf id=3489868704 keys=[30, 45] values=[300, 450] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 4, 7] values=[20, 40, 70] count=3
  [1] id=3489868800 keys=[8, 11] values=[80, 110] count=2
  [2] id=3491463776 keys=[15, 19, 23] values=[150, 190, 230] count=3
  [3] id=3489868704 keys=[30, 45] values=[300, 450] count=2

Total nodes visited (approx): 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


============================================================
B+ TREE STRUCTURE
============================================================

Level 0: Node(keys=[8, 15, 30]) 

Level 1: Leaf(keys=[2, 4, 7]) Leaf(keys=[8, 11]) Leaf(keys=[15, 19, 23]) Leaf(keys=[30, 45]) 

Leaf chain:
  Leaf #0 keys: [2, 4, 7], values: [20, 40, 70]
  Leaf #1 keys: [8, 11], values: [80, 110]
  Leaf #2 keys: [15, 19, 23], values: [150, 190, 230]
  Leaf #3 keys: [30, 45], values: [300, 450]

Inserting more keys: [33, 12, 27, 50, 6, 41, 18, 3, 36, 25]...
  → Inserted (33, 330)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 33
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466128 keys=[8, 15, 30] children_ids=[3491464352, 3489868800, 3491463776, 3489868704]

Level 1 (nodes=4):
  Leaf id=3491464352 keys=[2, 4, 7] values=[20, 40, 70] len=3 next_id=3489868800
  Leaf id=3489868800 keys=[8, 11] values=[80, 110] len=2 next_id=3491463776
  Leaf id=3491463776 keys=[15, 19, 23] values=[150, 190, 230] len=3 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 45] values=[300, 330, 450] len=3 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 4, 7] values=[20, 40, 70] count=3
  [1] id=3489868800 keys=[8, 11] values=[80, 110] count=2
  [2] id=3491463776 keys=[15, 19, 23] values=[150, 190, 230] count=3
  [3] id=3489868704 keys=[30, 33, 45] values=[300, 330, 450] count=3

Total nodes visited (approx): 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (12, 120)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 12
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466128 keys=[8, 15, 30] children_ids=[3491464352, 3489868800, 3491463776, 3489868704]

Level 1 (nodes=4):
  Leaf id=3491464352 keys=[2, 4, 7] values=[20, 40, 70] len=3 next_id=3489868800
  Leaf id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[15, 19, 23] values=[150, 190, 230] len=3 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 45] values=[300, 330, 450] len=3 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 4, 7] values=[20, 40, 70] count=3
  [1] id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] count=3
  [2] id=3491463776 keys=[15, 19, 23] values=[150, 190, 230] count=3
  [3] id=3489868704 keys=[30, 33, 45] values=[300, 330, 450] count=3

Total nodes visited (approx): 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (27, 270)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 27
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466128 keys=[8, 15, 30] children_ids=[3491464352, 3489868800, 3491463776, 3489868704]

Level 1 (nodes=4):
  Leaf id=3491464352 keys=[2, 4, 7] values=[20, 40, 70] len=3 next_id=3489868800
  Leaf id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[15, 19, 23, 27] values=[150, 190, 230, 270] len=4 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 45] values=[300, 330, 450] len=3 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 4, 7] values=[20, 40, 70] count=3
  [1] id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] count=3
  [2] id=3491463776 keys=[15, 19, 23, 27] values=[150, 190, 230, 270] count=4
  [3] id=3489868704 keys=[30, 33, 45] values=[300, 330, 450] count=3

Total nodes visited (approx): 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (50, 500)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 50
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466128 keys=[8, 15, 30] children_ids=[3491464352, 3489868800, 3491463776, 3489868704]

Level 1 (nodes=4):
  Leaf id=3491464352 keys=[2, 4, 7] values=[20, 40, 70] len=3 next_id=3489868800
  Leaf id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[15, 19, 23, 27] values=[150, 190, 230, 270] len=4 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 45, 50] values=[300, 330, 450, 500] len=4 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 4, 7] values=[20, 40, 70] count=3
  [1] id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] count=3
  [2] id=3491463776 keys=[15, 19, 23, 27] values=[150, 190, 230, 270] count=4
  [3] id=3489868704 keys=[30, 33, 45, 50] values=[300, 330, 450, 500] count=4

Total nodes visited (approx): 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (6, 60)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466128 keys=[8, 15, 30] children_ids=[3491464352, 3489868800, 3491463776, 3489868704]

Level 1 (nodes=4):
  Leaf id=3491464352 keys=[2, 4, 6, 7] values=[20, 40, 60, 70] len=4 next_id=3489868800
  Leaf id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[15, 19, 23, 27] values=[150, 190, 230, 270] len=4 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 45, 50] values=[300, 330, 450, 500] len=4 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 4, 6, 7] values=[20, 40, 60, 70] count=4
  [1] id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] count=3
  [2] id=3491463776 keys=[15, 19, 23, 27] values=[150, 190, 230, 270] count=4
  [3] id=3489868704 keys=[30, 33, 45, 50] values=[300, 330, 450, 500] count=4

Total nodes visited (approx): 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (41, 410)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 41
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491466128 keys=[8, 15, 30, 45] children_ids=[3491464352, 3489868800, 3491463776, 3489868704, 3489868848]

Level 1 (nodes=5):
  Leaf id=3491464352 keys=[2, 4, 6, 7] values=[20, 40, 60, 70] len=4 next_id=3489868800
  Leaf id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[15, 19, 23, 27] values=[150, 190, 230, 270] len=4 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 41] values=[300, 330, 410] len=3 next_id=3489868848
  Leaf id=3489868848 keys=[45, 50] values=[450, 500] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 4, 6, 7] values=[20, 40, 60, 70] count=4
  [1] id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] count=3
  [2] id=3491463776 keys=[15, 19, 23, 27] values=[150, 190, 230, 270] count=4
  [3] id=3489868704 keys=[30, 33, 41] values=[300, 330, 410] count=3
  [4] id=3489868848 keys=[45, 50] values=[450, 500] count=2

Total nodes visited (approx): 6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (18, 180)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 18
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3489868944 keys=[23] children_ids=[3491466128, 3489868896]

Level 1 (nodes=2):
  Node id=3491466128 keys=[8, 15] children_ids=[3491464352, 3489868800, 3491463776]
  Node id=3489868896 keys=[30, 45] children_ids=[3489868752, 3489868704, 3489868848]

Level 2 (nodes=6):
  Leaf id=3491464352 keys=[2, 4, 6, 7] values=[20, 40, 60, 70] len=4 next_id=3489868800
  Leaf id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[15, 18, 19] values=[150, 180, 190] len=3 next_id=3489868752
  Leaf id=3489868752 keys=[23, 27] values=[230, 270] len=2 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 41] values=[300, 330, 410] len=3 next_id=3489868848
  Leaf id=3489868848 keys=[45, 50] values=[450, 500] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 4, 6, 7] values=[20, 40, 60, 70] count=4
  [1] id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] count=3
  [2] id=3491463776 keys=[15, 18, 19] values=[150, 180, 190] count=3
  [3] id=3489868752 keys=[23, 27] values=[230, 270] count=2
  [4] id=3489868704 keys=[30, 33, 41] values=[300, 330, 410] count=3
  [5] id=3489868848 keys=[45, 50] values=[450, 500] count=2

Total nodes visited (approx): 9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (3, 30)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3489868944 keys=[23] children_ids=[3491466128, 3489868896]

Level 1 (nodes=2):
  Node id=3491466128 keys=[6, 8, 15] children_ids=[3491464352, 3489868992, 3489868800, 3491463776]
  Node id=3489868896 keys=[30, 45] children_ids=[3489868752, 3489868704, 3489868848]

Level 2 (nodes=7):
  Leaf id=3491464352 keys=[2, 3, 4] values=[20, 30, 40] len=3 next_id=3489868992
  Leaf id=3489868992 keys=[6, 7] values=[60, 70] len=2 next_id=3489868800
  Leaf id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[15, 18, 19] values=[150, 180, 190] len=3 next_id=3489868752
  Leaf id=3489868752 keys=[23, 27] values=[230, 270] len=2 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 41] values=[300, 330, 410] len=3 next_id=3489868848
  Leaf id=3489868848 keys=[45, 50] values=[450, 500] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 3, 4] values=[20, 30, 40] count=3
  [1] id=3489868992 keys=[6, 7] values=[60, 70] count=2
  [2] id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] count=3
  [3] id=3491463776 keys=[15, 18, 19] values=[150, 180, 190] count=3
  [4] id=3489868752 keys=[23, 27] values=[230, 270] count=2
  [5] id=3489868704 keys=[30, 33, 41] values=[300, 330, 410] count=3
  [6] id=3489868848 keys=[45, 50] values=[450, 500] count=2

Total nodes visited (approx): 10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (36, 360)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 36
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3489868944 keys=[23] children_ids=[3491466128, 3489868896]

Level 1 (nodes=2):
  Node id=3491466128 keys=[6, 8, 15] children_ids=[3491464352, 3489868992, 3489868800, 3491463776]
  Node id=3489868896 keys=[30, 45] children_ids=[3489868752, 3489868704, 3489868848]

Level 2 (nodes=7):
  Leaf id=3491464352 keys=[2, 3, 4] values=[20, 30, 40] len=3 next_id=3489868992
  Leaf id=3489868992 keys=[6, 7] values=[60, 70] len=2 next_id=3489868800
  Leaf id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[15, 18, 19] values=[150, 180, 190] len=3 next_id=3489868752
  Leaf id=3489868752 keys=[23, 27] values=[230, 270] len=2 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 36, 41] values=[300, 330, 360, 410] len=4 next_id=3489868848
  Leaf id=3489868848 keys=[45, 50] values=[450, 500] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 3, 4] values=[20, 30, 40] count=3
  [1] id=3489868992 keys=[6, 7] values=[60, 70] count=2
  [2] id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] count=3
  [3] id=3491463776 keys=[15, 18, 19] values=[150, 180, 190] count=3
  [4] id=3489868752 keys=[23, 27] values=[230, 270] count=2
  [5] id=3489868704 keys=[30, 33, 36, 41] values=[300, 330, 360, 410] count=4
  [6] id=3489868848 keys=[45, 50] values=[450, 500] count=2

Total nodes visited (approx): 10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  → Inserted (25, 250)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 25
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3489868944 keys=[23] children_ids=[3491466128, 3489868896]

Level 1 (nodes=2):
  Node id=3491466128 keys=[6, 8, 15] children_ids=[3491464352, 3489868992, 3489868800, 3491463776]
  Node id=3489868896 keys=[30, 45] children_ids=[3489868752, 3489868704, 3489868848]

Level 2 (nodes=7):
  Leaf id=3491464352 keys=[2, 3, 4] values=[20, 30, 40] len=3 next_id=3489868992
  Leaf id=3489868992 keys=[6, 7] values=[60, 70] len=2 next_id=3489868800
  Leaf id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[15, 18, 19] values=[150, 180, 190] len=3 next_id=3489868752
  Leaf id=3489868752 keys=[23, 25, 27] values=[230, 250, 270] len=3 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 36, 41] values=[300, 330, 360, 410] len=4 next_id=3489868848
  Leaf id=3489868848 keys=[45, 50] values=[450, 500] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 3, 4] values=[20, 30, 40] count=3
  [1] id=3489868992 keys=[6, 7] values=[60, 70] count=2
  [2] id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] count=3
  [3] id=3491463776 keys=[15, 18, 19] values=[150, 180, 190] count=3
  [4] id=3489868752 keys=[23, 25, 27] values=[230, 250, 270] count=3
  [5] id=3489868704 keys=[30, 33, 36, 41] values=[300, 330, 360, 410] count=4
  [6] id=3489868848 keys=[45, 50] values=[450, 500] count=2

Total nodes visited (approx): 10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


============================================================
B+ TREE STRUCTURE
============================================================

Level 0: Node(keys=[23]) 

Level 1: Node(keys=[6, 8, 15]) Node(keys=[30, 45]) 

Level 2: Leaf(keys=[2, 3, 4]) Leaf(keys=[6, 7]) Leaf(keys=[8, 11, 12]) Leaf(keys=[15, 18, 19]) Leaf(keys=[23, 25, 27]) Leaf(keys=[30, 33, 36, 41]) Leaf(keys=[45, 50]) 

Leaf chain:
  Leaf #0 keys: [2, 3, 4], values: [20, 30, 40]
  Leaf #1 keys: [6, 7], values: [60, 70]
  Leaf #2 keys: [8, 11, 12], values: [80, 110, 120]
  Leaf #3 keys: [15, 18, 19], values: [150, 180, 190]
  Leaf #4 keys: [23, 25, 27], values: [230, 250, 270]
  Leaf #5 keys: [30, 33, 36, 41], values: [300, 330, 360, 410]
  Leaf #6 keys: [45, 50], values: [450, 500]

Searching for some keys:
  Key 15: Found: 150
  Key 7: Found: 70
  Key 100: Not found
  Key 23: Found: 230
  Key 99: Not found
  Key 45: Found: 450

Removing some keys: [15, 7, 23, 4, 11]...

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after remove 15
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3489868944 keys=[23] children_ids=[3491466128, 3489868896]

Level 1 (nodes=2):
  Node id=3491466128 keys=[6, 8, 15] children_ids=[3491464352, 3489868992, 3489868800, 3491463776]
  Node id=3489868896 keys=[30, 45] children_ids=[3489868752, 3489868704, 3489868848]

Level 2 (nodes=7):
  Leaf id=3491464352 keys=[2, 3, 4] values=[20, 30, 40] len=3 next_id=3489868992
  Leaf id=3489868992 keys=[6, 7] values=[60, 70] len=2 next_id=3489868800
  Leaf id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[18, 19] values=[180, 190] len=2 next_id=3489868752
  Leaf id=3489868752 keys=[23, 25, 27] values=[230, 250, 270] len=3 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 36, 41] values=[300, 330, 360, 410] len=4 next_id=3489868848
  Leaf id=3489868848 keys=[45, 50] values=[450, 500] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 3, 4] values=[20, 30, 40] count=3
  [1] id=3489868992 keys=[6, 7] values=[60, 70] count=2
  [2] id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] count=3
  [3] id=3491463776 keys=[18, 19] values=[180, 190] count=2
  [4] id=3489868752 keys=[23, 25, 27] values=[230, 250, 270] count=3
  [5] id=3489868704 keys=[30, 33, 36, 41] values=[300, 330, 360, 410] count=4
  [6] id=3489868848 keys=[45, 50] values=[450, 500] count=2

Total nodes visited (approx): 10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after remove 7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3489868944 keys=[23] children_ids=[3491466128, 3489868896]

Level 1 (nodes=2):
  Node id=3491466128 keys=[4, 8, 15] children_ids=[3491464352, 3489868992, 3489868800, 3491463776]
  Node id=3489868896 keys=[30, 45] children_ids=[3489868752, 3489868704, 3489868848]

Level 2 (nodes=7):
  Leaf id=3491464352 keys=[2, 3] values=[20, 30] len=2 next_id=3489868992
  Leaf id=3489868992 keys=[4, 6] values=[40, 60] len=2 next_id=3489868800
  Leaf id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[18, 19] values=[180, 190] len=2 next_id=3489868752
  Leaf id=3489868752 keys=[23, 25, 27] values=[230, 250, 270] len=3 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 36, 41] values=[300, 330, 360, 410] len=4 next_id=3489868848
  Leaf id=3489868848 keys=[45, 50] values=[450, 500] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 3] values=[20, 30] count=2
  [1] id=3489868992 keys=[4, 6] values=[40, 60] count=2
  [2] id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] count=3
  [3] id=3491463776 keys=[18, 19] values=[180, 190] count=2
  [4] id=3489868752 keys=[23, 25, 27] values=[230, 250, 270] count=3
  [5] id=3489868704 keys=[30, 33, 36, 41] values=[300, 330, 360, 410] count=4
  [6] id=3489868848 keys=[45, 50] values=[450, 500] count=2

Total nodes visited (approx): 10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after remove 23
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3489868944 keys=[23] children_ids=[3491466128, 3489868896]

Level 1 (nodes=2):
  Node id=3491466128 keys=[4, 8, 15] children_ids=[3491464352, 3489868992, 3489868800, 3491463776]
  Node id=3489868896 keys=[30, 45] children_ids=[3489868752, 3489868704, 3489868848]

Level 2 (nodes=7):
  Leaf id=3491464352 keys=[2, 3] values=[20, 30] len=2 next_id=3489868992
  Leaf id=3489868992 keys=[4, 6] values=[40, 60] len=2 next_id=3489868800
  Leaf id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[18, 19] values=[180, 190] len=2 next_id=3489868752
  Leaf id=3489868752 keys=[25, 27] values=[250, 270] len=2 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 36, 41] values=[300, 330, 360, 410] len=4 next_id=3489868848
  Leaf id=3489868848 keys=[45, 50] values=[450, 500] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 3] values=[20, 30] count=2
  [1] id=3489868992 keys=[4, 6] values=[40, 60] count=2
  [2] id=3489868800 keys=[8, 11, 12] values=[80, 110, 120] count=3
  [3] id=3491463776 keys=[18, 19] values=[180, 190] count=2
  [4] id=3489868752 keys=[25, 27] values=[250, 270] count=2
  [5] id=3489868704 keys=[30, 33, 36, 41] values=[300, 330, 360, 410] count=4
  [6] id=3489868848 keys=[45, 50] values=[450, 500] count=2

Total nodes visited (approx): 10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after remove 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3489868944 keys=[23] children_ids=[3491466128, 3489868896]

Level 1 (nodes=2):
  Node id=3491466128 keys=[4, 11, 15] children_ids=[3491464352, 3489868992, 3489868800, 3491463776]
  Node id=3489868896 keys=[30, 45] children_ids=[3489868752, 3489868704, 3489868848]

Level 2 (nodes=7):
  Leaf id=3491464352 keys=[2, 3] values=[20, 30] len=2 next_id=3489868992
  Leaf id=3489868992 keys=[6, 8] values=[60, 80] len=2 next_id=3489868800
  Leaf id=3489868800 keys=[11, 12] values=[110, 120] len=2 next_id=3491463776
  Leaf id=3491463776 keys=[18, 19] values=[180, 190] len=2 next_id=3489868752
  Leaf id=3489868752 keys=[25, 27] values=[250, 270] len=2 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 36, 41] values=[300, 330, 360, 410] len=4 next_id=3489868848
  Leaf id=3489868848 keys=[45, 50] values=[450, 500] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 3] values=[20, 30] count=2
  [1] id=3489868992 keys=[6, 8] values=[60, 80] count=2
  [2] id=3489868800 keys=[11, 12] values=[110, 120] count=2
  [3] id=3491463776 keys=[18, 19] values=[180, 190] count=2
  [4] id=3489868752 keys=[25, 27] values=[250, 270] count=2
  [5] id=3489868704 keys=[30, 33, 36, 41] values=[300, 330, 360, 410] count=4
  [6] id=3489868848 keys=[45, 50] values=[450, 500] count=2

Total nodes visited (approx): 10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after remove 11
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3489868944 keys=[23] children_ids=[3491466128, 3489868896]

Level 1 (nodes=2):
  Node id=3491466128 keys=[4, 15] children_ids=[3491464352, 3489868992, 3491463776]
  Node id=3489868896 keys=[30, 45] children_ids=[3489868752, 3489868704, 3489868848]

Level 2 (nodes=6):
  Leaf id=3491464352 keys=[2, 3] values=[20, 30] len=2 next_id=3489868992
  Leaf id=3489868992 keys=[6, 8, 12] values=[60, 80, 120] len=3 next_id=3491463776
  Leaf id=3491463776 keys=[18, 19] values=[180, 190] len=2 next_id=3489868752
  Leaf id=3489868752 keys=[25, 27] values=[250, 270] len=2 next_id=3489868704
  Leaf id=3489868704 keys=[30, 33, 36, 41] values=[300, 330, 360, 410] len=4 next_id=3489868848
  Leaf id=3489868848 keys=[45, 50] values=[450, 500] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491464352 keys=[2, 3] values=[20, 30] count=2
  [1] id=3489868992 keys=[6, 8, 12] values=[60, 80, 120] count=3
  [2] id=3491463776 keys=[18, 19] values=[180, 190] count=2
  [3] id=3489868752 keys=[25, 27] values=[250, 270] count=2
  [4] id=3489868704 keys=[30, 33, 36, 41] values=[300, 330, 360, 410] count=4
  [5] id=3489868848 keys=[45, 50] values=[450, 500] count=2

Total nodes visited (approx): 9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


============================================================
B+ TREE STRUCTURE
============================================================

Level 0: Node(keys=[23]) 

Level 1: Node(keys=[4, 15]) Node(keys=[30, 45]) 

Level 2: Leaf(keys=[2, 3]) Leaf(keys=[6, 8, 12]) Leaf(keys=[18, 19]) Leaf(keys=[25, 27]) Leaf(keys=[30, 33, 36, 41]) Leaf(keys=[45, 50]) 

Leaf chain:
  Leaf #0 keys: [2, 3], values: [20, 30]
  Leaf #1 keys: [6, 8, 12], values: [60, 80, 120]
  Leaf #2 keys: [18, 19], values: [180, 190]
  Leaf #3 keys: [25, 27], values: [250, 270]
  Leaf #4 keys: [30, 33, 36, 41], values: [300, 330, 360, 410]
  Leaf #5 keys: [45, 50], values: [450, 500]

======================================================================
TEST 5: Updating Values
======================================================================

Inserting keys 1-5...

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491463728 keys=[1] values=[100] len=1 next_id=None

Leaf details in physical order:
  [0] id=3491463728 keys=[1] values=[100] count=1

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491463728 keys=[1, 2] values=[100, 200] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491463728 keys=[1, 2] values=[100, 200] count=2

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491463728 keys=[1, 2, 3] values=[100, 200, 300] len=3 next_id=None

Leaf details in physical order:
  [0] id=3491463728 keys=[1, 2, 3] values=[100, 200, 300] count=3

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Leaf id=3491463728 keys=[1, 2, 3, 4] values=[100, 200, 300, 400] len=4 next_id=None

Leaf details in physical order:
  [0] id=3491463728 keys=[1, 2, 3, 4] values=[100, 200, 300, 400] count=4

Total nodes visited (approx): 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VERBOSE SNAPSHOT: after insert 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Level 0 (nodes=1):
  Node id=3491463776 keys=[4] children_ids=[3491463728, 3491466128]

Level 1 (nodes=2):
  Leaf id=3491463728 keys=[1, 2, 3] values=[100, 200, 300] len=3 next_id=3491466128
  Leaf id=3491466128 keys=[4, 5] values=[400, 500] len=2 next_id=None

Leaf details in physical order:
  [0] id=3491463728 keys=[1, 2, 3] values=[100, 200, 300] count=3
  [1] id=3491466128 keys=[4, 5] values=[400, 500] count=2

Total nodes visited (approx): 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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

============================================================
B+ TREE STRUCTURE
============================================================

Level 0: Node(keys=[4]) 

Level 1: Leaf(keys=[1, 2, 3]) Leaf(keys=[4, 5]) 

Leaf chain:
  Leaf #0 keys: [1, 2, 3], values: [100, 200, 999]
  Leaf #1 keys: [4, 5], values: [400, 500]

######################################################################
# ALL TESTS COMPLETED
######################################################################

