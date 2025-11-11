# Saída ExtensibleHash

```bash
######################################################################
# EXTENSIBLE HASH - DEMONSTRATION AND TESTS
# Author: Gabriel Viana
# Course: CSGBD - UFC
######################################################################

======================================================================
TEST 1: Basic Operations (Insert and Search)
======================================================================

Inserting keys: 1, 2, 3, 4...
  → Inserido no Bucket #123875199160624 (índice 1, local_depth=1)
  → Inserido no Bucket #123875197415744 (índice 0, local_depth=1)
  → Inserido no Bucket #123875199160624 (índice 1, local_depth=1)
  → Inserido no Bucket #123875197415744 (índice 0, local_depth=1)

============================================================
Extensible Hash Structure
============================================================
Global Depth: 1
Directory Size: 2
Bucket Size: 2
============================================================

Directory Mapping:
Index      Binary          Bucket ID    Local Depth     Entries
--------------------------------------------------------------------------------
0          0               123875197415744 1               {2: 200, 4: 400} *
1          1               123875199160624 1               {1: 100, 3: 300} *

============================================================
Unique Buckets: 2
============================================================


Detailed Bucket Contents:
============================================================

Bucket #0 (ID: 123875197415744)
  Local Depth: 1
  Capacity: 2/2
  Entries: {2: 200, 4: 400}
  Directory Indices: 0(0)

Bucket #1 (ID: 123875199160624)
  Local Depth: 1
  Capacity: 2/2
  Entries: {1: 100, 3: 300}
  Directory Indices: 1(1)

============================================================


Searching for keys:
  → Encontrado no Bucket #123875199160624 (índice 1, local_depth=1)
  Key 1: 100
  → Encontrado no Bucket #123875197415744 (índice 0, local_depth=1)
  Key 2: 200
  → Encontrado no Bucket #123875199160624 (índice 1, local_depth=1)
  Key 3: 300
  → Encontrado no Bucket #123875197415744 (índice 0, local_depth=1)
  Key 4: 400
  Key 5: Not found

======================================================================
TEST 2: Bucket Split and Directory Doubling
======================================================================

Inserting keys to trigger splits: 0, 2, 4, 6, 8, 10...

--- Inserting key 0 ---
  → Inserido no Bucket #123875197415168 (índice 0, local_depth=1)

============================================================
Extensible Hash Structure
============================================================
Global Depth: 1
Directory Size: 2
Bucket Size: 2
============================================================

Directory Mapping:
Index      Binary          Bucket ID    Local Depth     Entries
--------------------------------------------------------------------------------
0          0               123875197415168 1               {0: 0} *
1          1               123875197418192 1               {} *

============================================================
Unique Buckets: 2
============================================================


Detailed Bucket Contents:
============================================================

Bucket #0 (ID: 123875197415168)
  Local Depth: 1
  Capacity: 1/2
  Entries: {0: 0}
  Directory Indices: 0(0)

Bucket #1 (ID: 123875197418192)
  Local Depth: 1
  Capacity: 0/2
  Entries: Empty
  Directory Indices: 1(1)

============================================================


--- Inserting key 2 ---
  → Inserido no Bucket #123875197415168 (índice 0, local_depth=1)

============================================================
Extensible Hash Structure
============================================================
Global Depth: 1
Directory Size: 2
Bucket Size: 2
============================================================

Directory Mapping:
Index      Binary          Bucket ID    Local Depth     Entries
--------------------------------------------------------------------------------
0          0               123875197415168 1               {0: 0, 2: 20} *
1          1               123875197418192 1               {} *

============================================================
Unique Buckets: 2
============================================================


Detailed Bucket Contents:
============================================================

Bucket #0 (ID: 123875197415168)
  Local Depth: 1
  Capacity: 2/2
  Entries: {0: 0, 2: 20}
  Directory Indices: 0(0)

Bucket #1 (ID: 123875197418192)
  Local Depth: 1
  Capacity: 0/2
  Entries: Empty
  Directory Indices: 1(1)

============================================================


--- Inserting key 4 ---
  ⚠ Bucket #123875197415168 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 2
  → Inserido no Bucket #123875197418144 (índice 0, local_depth=2)

============================================================
Extensible Hash Structure
============================================================
Global Depth: 2
Directory Size: 4
Bucket Size: 2
============================================================

Directory Mapping:
Index      Binary          Bucket ID    Local Depth     Entries
--------------------------------------------------------------------------------
0          00              123875197418144 2               {0: 0, 4: 40} *
1          01              123875197418192 1               {} *
2          10              123875197418432 2               {2: 20} *
3          11              123875197418192 1               {}

============================================================
Unique Buckets: 3
============================================================


Detailed Bucket Contents:
============================================================

Bucket #0 (ID: 123875197418144)
  Local Depth: 2
  Capacity: 2/2
  Entries: {0: 0, 4: 40}
  Directory Indices: 0(00)

Bucket #1 (ID: 123875197418192)
  Local Depth: 1
  Capacity: 0/2
  Entries: Empty
  Directory Indices: 1(01), 3(11)

Bucket #2 (ID: 123875197418432)
  Local Depth: 2
  Capacity: 1/2
  Entries: {2: 20}
  Directory Indices: 2(10)

============================================================


--- Inserting key 6 ---
  → Inserido no Bucket #123875197418432 (índice 2, local_depth=2)

============================================================
Extensible Hash Structure
============================================================
Global Depth: 2
Directory Size: 4
Bucket Size: 2
============================================================

Directory Mapping:
Index      Binary          Bucket ID    Local Depth     Entries
--------------------------------------------------------------------------------
0          00              123875197418144 2               {0: 0, 4: 40} *
1          01              123875197418192 1               {} *
2          10              123875197418432 2               {2: 20, 6: 60} *
3          11              123875197418192 1               {}

============================================================
Unique Buckets: 3
============================================================


Detailed Bucket Contents:
============================================================

Bucket #0 (ID: 123875197418144)
  Local Depth: 2
  Capacity: 2/2
  Entries: {0: 0, 4: 40}
  Directory Indices: 0(00)

Bucket #1 (ID: 123875197418192)
  Local Depth: 1
  Capacity: 0/2
  Entries: Empty
  Directory Indices: 1(01), 3(11)

Bucket #2 (ID: 123875197418432)
  Local Depth: 2
  Capacity: 2/2
  Entries: {2: 20, 6: 60}
  Directory Indices: 2(10)

============================================================


--- Inserting key 8 ---
  ⚠ Bucket #123875197418144 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 3
  → Inserido no Bucket #123875197418528 (índice 0, local_depth=3)

============================================================
Extensible Hash Structure
============================================================
Global Depth: 3
Directory Size: 8
Bucket Size: 2
============================================================

Directory Mapping:
Index      Binary          Bucket ID    Local Depth     Entries
--------------------------------------------------------------------------------
0          000             123875197418528 3               {0: 0, 8: 80} *
1          001             123875197418192 1               {} *
2          010             123875197418432 2               {2: 20, 6: 60} *
3          011             123875197418192 1               {}
4          100             123875197418240 3               {4: 40} *
5          101             123875197418192 1               {}
6          110             123875197418432 2               {2: 20, 6: 60}
7          111             123875197418192 1               {}

============================================================
Unique Buckets: 4
============================================================


Detailed Bucket Contents:
============================================================

Bucket #0 (ID: 123875197418528)
  Local Depth: 3
  Capacity: 2/2
  Entries: {0: 0, 8: 80}
  Directory Indices: 0(000)

Bucket #1 (ID: 123875197418192)
  Local Depth: 1
  Capacity: 0/2
  Entries: Empty
  Directory Indices: 1(001), 3(011), 5(101), 7(111)

Bucket #2 (ID: 123875197418432)
  Local Depth: 2
  Capacity: 2/2
  Entries: {2: 20, 6: 60}
  Directory Indices: 2(010), 6(110)

Bucket #3 (ID: 123875197418240)
  Local Depth: 3
  Capacity: 1/2
  Entries: {4: 40}
  Directory Indices: 4(100)

============================================================


--- Inserting key 10 ---
  ⚠ Bucket #123875197418432 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 3
  → Inserido no Bucket #123875197418336 (índice 2, local_depth=3)

============================================================
Extensible Hash Structure
============================================================
Global Depth: 3
Directory Size: 8
Bucket Size: 2
============================================================

Directory Mapping:
Index      Binary          Bucket ID    Local Depth     Entries
--------------------------------------------------------------------------------
0          000             123875197418528 3               {0: 0, 8: 80} *
1          001             123875197418192 1               {} *
2          010             123875197418336 3               {2: 20, 10: 100} *
3          011             123875197418192 1               {}
4          100             123875197418240 3               {4: 40} *
5          101             123875197418192 1               {}
6          110             123875197415168 3               {6: 60} *
7          111             123875197418192 1               {}

============================================================
Unique Buckets: 5
============================================================


Detailed Bucket Contents:
============================================================

Bucket #0 (ID: 123875197418528)
  Local Depth: 3
  Capacity: 2/2
  Entries: {0: 0, 8: 80}
  Directory Indices: 0(000)

Bucket #1 (ID: 123875197418192)
  Local Depth: 1
  Capacity: 0/2
  Entries: Empty
  Directory Indices: 1(001), 3(011), 5(101), 7(111)

Bucket #2 (ID: 123875197418336)
  Local Depth: 3
  Capacity: 2/2
  Entries: {2: 20, 10: 100}
  Directory Indices: 2(010)

Bucket #3 (ID: 123875197418240)
  Local Depth: 3
  Capacity: 1/2
  Entries: {4: 40}
  Directory Indices: 4(100)

Bucket #4 (ID: 123875197415168)
  Local Depth: 3
  Capacity: 1/2
  Entries: {6: 60}
  Directory Indices: 6(110)

============================================================


======================================================================
TEST 3: Removal and Bucket Merging
======================================================================

Inserting keys: 1-10...
  → Inserido no Bucket #123875197418192 (índice 1, local_depth=1)
  → Inserido no Bucket #123875197415744 (índice 0, local_depth=1)
  → Inserido no Bucket #123875197418192 (índice 1, local_depth=1)
  → Inserido no Bucket #123875197415744 (índice 0, local_depth=1)
  → Inserido no Bucket #123875197418192 (índice 1, local_depth=1)
  → Inserido no Bucket #123875197415744 (índice 0, local_depth=1)
  ⚠ Bucket #123875197418192 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 2
  → Inserido no Bucket #123875197418240 (índice 3, local_depth=2)
  ⚠ Bucket #123875197415744 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 2
  → Inserido no Bucket #123875197418192 (índice 0, local_depth=2)
  → Inserido no Bucket #123875197418528 (índice 1, local_depth=2)
  → Inserido no Bucket #123875197418096 (índice 2, local_depth=2)

============================================================
Extensible Hash Structure
============================================================
Global Depth: 2
Directory Size: 4
Bucket Size: 3
============================================================

Directory Mapping:
Index      Binary          Bucket ID    Local Depth     Entries
--------------------------------------------------------------------------------
0          00              123875197418192 2               {4: 400, 8: 800} *
1          01              123875197418528 2               {1: 100, 5: 500, 9: 900} *
2          10              123875197418096 2               {2: 200, 6: 600, 10: 1000} *
3          11              123875197418240 2               {3: 300, 7: 700} *

============================================================
Unique Buckets: 4
============================================================


Detailed Bucket Contents:
============================================================

Bucket #0 (ID: 123875197418192)
  Local Depth: 2
  Capacity: 2/3
  Entries: {4: 400, 8: 800}
  Directory Indices: 0(00)

Bucket #1 (ID: 123875197418528)
  Local Depth: 2
  Capacity: 3/3
  Entries: {1: 100, 5: 500, 9: 900}
  Directory Indices: 1(01)

Bucket #2 (ID: 123875197418096)
  Local Depth: 2
  Capacity: 3/3
  Entries: {2: 200, 6: 600, 10: 1000}
  Directory Indices: 2(10)

Bucket #3 (ID: 123875197418240)
  Local Depth: 2
  Capacity: 2/3
  Entries: {3: 300, 7: 700}
  Directory Indices: 3(11)

============================================================


Removing keys: 2, 4, 6, 8...
  → Removido do Bucket #123875197418096 (índice 2, local_depth=2)
  Removed key 2: True
  → Removido do Bucket #123875197418192 (índice 0, local_depth=2)
  ✓ Merge realizado. Buckets consolidados.
  Removed key 4: True
  → Removido do Bucket #123875197415168 (índice 2, local_depth=1)
  Removed key 6: True
  → Removido do Bucket #123875197415168 (índice 0, local_depth=1)
  Removed key 8: True

============================================================
Extensible Hash Structure
============================================================
Global Depth: 2
Directory Size: 4
Bucket Size: 3
============================================================

Directory Mapping:
Index      Binary          Bucket ID    Local Depth     Entries
--------------------------------------------------------------------------------
0          00              123875197415168 1               {10: 1000} *
1          01              123875197418528 2               {1: 100, 5: 500, 9: 900} *
2          10              123875197415168 1               {10: 1000}
3          11              123875197418240 2               {3: 300, 7: 700} *

============================================================
Unique Buckets: 3
============================================================


Detailed Bucket Contents:
============================================================

Bucket #0 (ID: 123875197415168)
  Local Depth: 1
  Capacity: 1/3
  Entries: {10: 1000}
  Directory Indices: 0(00), 2(10)

Bucket #1 (ID: 123875197418528)
  Local Depth: 2
  Capacity: 3/3
  Entries: {1: 100, 5: 500, 9: 900}
  Directory Indices: 1(01)

Bucket #2 (ID: 123875197418240)
  Local Depth: 2
  Capacity: 2/3
  Entries: {3: 300, 7: 700}
  Directory Indices: 3(11)

============================================================


Searching after removal:
  → Encontrado no Bucket #123875197418528 (índice 1, local_depth=2)
  Key 1: 100
  Key 2: Not found
  → Encontrado no Bucket #123875197418240 (índice 3, local_depth=2)
  Key 3: 300
  Key 4: Not found
  → Encontrado no Bucket #123875197418528 (índice 1, local_depth=2)
  Key 5: 500

======================================================================
TEST 4: Complex Sequence (Simulating Real Usage)
======================================================================

Inserting keys: [15, 7, 23, 4, 11, 30, 19, 2, 45, 8]...
  → Inserido no Bucket #123875197418240 (índice 1, local_depth=1)
  → Inserido no Bucket #123875197418240 (índice 1, local_depth=1)
  ⚠ Bucket #123875197418240 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 2
  ⚠ Bucket #123875197418720 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 3
  ⚠ Bucket #123875197418432 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 4
  → Inserido no Bucket #123875197418096 (índice 7, local_depth=4)
  → Inserido no Bucket #123875197415168 (índice 4, local_depth=1)
  → Inserido no Bucket #123875197418192 (índice 11, local_depth=3)
  → Inserido no Bucket #123875197415168 (índice 14, local_depth=1)
  → Inserido no Bucket #123875197418192 (índice 3, local_depth=3)
  ⚠ Bucket #123875197415168 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 4
  → Inserido no Bucket #123875197418432 (índice 2, local_depth=2)
  → Inserido no Bucket #123875197418336 (índice 13, local_depth=2)
  → Inserido no Bucket #123875197418240 (índice 8, local_depth=2)

============================================================
Extensible Hash Structure
============================================================
Global Depth: 4
Directory Size: 16
Bucket Size: 2
============================================================

Directory Mapping:
Index      Binary          Bucket ID    Local Depth     Entries
--------------------------------------------------------------------------------
0          0000            123875197418240 2               {4: 40, 8: 80} *
1          0001            123875197418336 2               {45: 450} *
2          0010            123875197418432 2               {30: 300, 2: 20} *
3          0011            123875197418192 3               {11: 110, 19: 190} *
4          0100            123875197418240 2               {4: 40, 8: 80}
5          0101            123875197418336 2               {45: 450}
6          0110            123875197418432 2               {30: 300, 2: 20}
7          0111            123875197418096 4               {7: 70, 23: 230} *
8          1000            123875197418240 2               {4: 40, 8: 80}
9          1001            123875197418336 2               {45: 450}
10         1010            123875197418432 2               {30: 300, 2: 20}
11         1011            123875197418192 3               {11: 110, 19: 190}
12         1100            123875197418240 2               {4: 40, 8: 80}
13         1101            123875197418336 2               {45: 450}
14         1110            123875197418432 2               {30: 300, 2: 20}
15         1111            123875197418480 4               {15: 150} *

============================================================
Unique Buckets: 6
============================================================


Detailed Bucket Contents:
============================================================

Bucket #0 (ID: 123875197418240)
  Local Depth: 2
  Capacity: 2/2
  Entries: {4: 40, 8: 80}
  Directory Indices: 0(0000), 4(0100), 8(1000), 12(1100)

Bucket #1 (ID: 123875197418336)
  Local Depth: 2
  Capacity: 1/2
  Entries: {45: 450}
  Directory Indices: 1(0001), 5(0101), 9(1001), 13(1101)

Bucket #2 (ID: 123875197418432)
  Local Depth: 2
  Capacity: 2/2
  Entries: {30: 300, 2: 20}
  Directory Indices: 2(0010), 6(0110), 10(1010), 14(1110)

Bucket #3 (ID: 123875197418192)
  Local Depth: 3
  Capacity: 2/2
  Entries: {11: 110, 19: 190}
  Directory Indices: 3(0011), 11(1011)

Bucket #4 (ID: 123875197418096)
  Local Depth: 4
  Capacity: 2/2
  Entries: {7: 70, 23: 230}
  Directory Indices: 7(0111)

Bucket #5 (ID: 123875197418480)
  Local Depth: 4
  Capacity: 1/2
  Entries: {15: 150}
  Directory Indices: 15(1111)

============================================================


Inserting more keys: [33, 12, 27, 50, 6, 41, 18, 3, 36, 25]...
  → Inserido no Bucket #123875197418336 (índice 1, local_depth=2)
  ⚠ Bucket #123875197418240 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 4
  → Inserido no Bucket #123875197415744 (índice 12, local_depth=3)
  ⚠ Bucket #123875197418192 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 4
  → Inserido no Bucket #123875197418576 (índice 11, local_depth=4)
  ⚠ Bucket #123875197418432 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 4
  → Inserido no Bucket #123875197418192 (índice 2, local_depth=3)
  → Inserido no Bucket #123875197415168 (índice 6, local_depth=3)
  ⚠ Bucket #123875197418336 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 4
  → Inserido no Bucket #123875197418432 (índice 9, local_depth=3)
  ⚠ Bucket #123875197418192 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 4
  ⚠ Bucket #123875197418336 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 5
  → Inserido no Bucket #123875197419248 (índice 18, local_depth=5)
  → Inserido no Bucket #123875197418240 (índice 3, local_depth=4)
  ⚠ Bucket #123875197415744 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 5
  → Inserido no Bucket #123875197418192 (índice 4, local_depth=4)
  ⚠ Bucket #123875197418432 está cheio. Iniciando split...
  ✓ Split concluído. Global depth agora é 5
  → Inserido no Bucket #123875197419344 (índice 25, local_depth=4)

============================================================
Extensible Hash Structure
============================================================
Global Depth: 5
Directory Size: 32
Bucket Size: 2
============================================================

Directory Mapping:
Index      Binary          Bucket ID    Local Depth     Entries
--------------------------------------------------------------------------------
0          00000           123875197418528 3               {8: 80} *
1          00001           123875197415744 4               {33: 330} *
2          00010           123875197419200 5               {2: 20} *
3          00011           123875197418240 4               {19: 190, 3: 30} *
4          00100           123875197418192 4               {4: 40, 36: 360} *
5          00101           123875197418960 3               {45: 450} *
6          00110           123875197415168 3               {30: 300, 6: 60} *
7          00111           123875197418096 4               {7: 70, 23: 230} *
8          01000           123875197418528 3               {8: 80}
9          01001           123875197419344 4               {41: 410, 25: 250} *
10         01010           123875197419008 4               {} *
11         01011           123875197418576 4               {11: 110, 27: 270} *
12         01100           123875197418336 4               {12: 120} *
13         01101           123875197418960 3               {45: 450}
14         01110           123875197415168 3               {30: 300, 6: 60}
15         01111           123875197418480 4               {15: 150} *
16         10000           123875197418528 3               {8: 80}
17         10001           123875197415744 4               {33: 330}
18         10010           123875197419248 5               {50: 500, 18: 180} *
19         10011           123875197418240 4               {19: 190, 3: 30}
20         10100           123875197418192 4               {4: 40, 36: 360}
21         10101           123875197418960 3               {45: 450}
22         10110           123875197415168 3               {30: 300, 6: 60}
23         10111           123875197418096 4               {7: 70, 23: 230}
24         11000           123875197418528 3               {8: 80}
25         11001           123875197419344 4               {41: 410, 25: 250}
26         11010           123875197419008 4               {}
27         11011           123875197418576 4               {11: 110, 27: 270}
28         11100           123875197418336 4               {12: 120}
29         11101           123875197418960 3               {45: 450}
30         11110           123875197415168 3               {30: 300, 6: 60}
31         11111           123875197418480 4               {15: 150}

============================================================
Unique Buckets: 14
============================================================


Detailed Bucket Contents:
============================================================

Bucket #0 (ID: 123875197418528)
  Local Depth: 3
  Capacity: 1/2
  Entries: {8: 80}
  Directory Indices: 0(00000), 8(01000), 16(10000), 24(11000)

Bucket #1 (ID: 123875197415744)
  Local Depth: 4
  Capacity: 1/2
  Entries: {33: 330}
  Directory Indices: 1(00001), 17(10001)

Bucket #2 (ID: 123875197419200)
  Local Depth: 5
  Capacity: 1/2
  Entries: {2: 20}
  Directory Indices: 2(00010)

Bucket #3 (ID: 123875197418240)
  Local Depth: 4
  Capacity: 2/2
  Entries: {19: 190, 3: 30}
  Directory Indices: 3(00011), 19(10011)

Bucket #4 (ID: 123875197418192)
  Local Depth: 4
  Capacity: 2/2
  Entries: {4: 40, 36: 360}
  Directory Indices: 4(00100), 20(10100)

Bucket #5 (ID: 123875197418960)
  Local Depth: 3
  Capacity: 1/2
  Entries: {45: 450}
  Directory Indices: 5(00101), 13(01101), 21(10101), 29(11101)

Bucket #6 (ID: 123875197415168)
  Local Depth: 3
  Capacity: 2/2
  Entries: {30: 300, 6: 60}
  Directory Indices: 6(00110), 14(01110), 22(10110), 30(11110)

Bucket #7 (ID: 123875197418096)
  Local Depth: 4
  Capacity: 2/2
  Entries: {7: 70, 23: 230}
  Directory Indices: 7(00111), 23(10111)

Bucket #8 (ID: 123875197419344)
  Local Depth: 4
  Capacity: 2/2
  Entries: {41: 410, 25: 250}
  Directory Indices: 9(01001), 25(11001)

Bucket #9 (ID: 123875197419008)
  Local Depth: 4
  Capacity: 0/2
  Entries: Empty
  Directory Indices: 10(01010), 26(11010)

Bucket #10 (ID: 123875197418576)
  Local Depth: 4
  Capacity: 2/2
  Entries: {11: 110, 27: 270}
  Directory Indices: 11(01011), 27(11011)

Bucket #11 (ID: 123875197418336)
  Local Depth: 4
  Capacity: 1/2
  Entries: {12: 120}
  Directory Indices: 12(01100), 28(11100)

Bucket #12 (ID: 123875197418480)
  Local Depth: 4
  Capacity: 1/2
  Entries: {15: 150}
  Directory Indices: 15(01111), 31(11111)

Bucket #13 (ID: 123875197419248)
  Local Depth: 5
  Capacity: 2/2
  Entries: {50: 500, 18: 180}
  Directory Indices: 18(10010)

============================================================


Searching for some keys:
  → Encontrado no Bucket #123875197418480 (índice 15, local_depth=4)
  Key 15: Found: 150
  → Encontrado no Bucket #123875197418096 (índice 7, local_depth=4)
  Key 7: Found: 70
  Key 100: Not found
  → Encontrado no Bucket #123875197418096 (índice 23, local_depth=4)
  Key 23: Found: 230
  Key 99: Not found
  → Encontrado no Bucket #123875197418960 (índice 13, local_depth=3)
  Key 45: Found: 450

Removing keys: [15, 7, 23, 4, 11]...
  → Removido do Bucket #123875197418480 (índice 15, local_depth=4)
  ✓ Merge realizado. Buckets consolidados.
  → Removido do Bucket #123875197418432 (índice 7, local_depth=3)
  → Removido do Bucket #123875197418432 (índice 23, local_depth=3)
  → Removido do Bucket #123875197418192 (índice 4, local_depth=4)
  ✓ Merge realizado. Buckets consolidados.
  → Removido do Bucket #123875197418576 (índice 11, local_depth=4)

============================================================
Extensible Hash Structure
============================================================
Global Depth: 5
Directory Size: 32
Bucket Size: 2
============================================================

Directory Mapping:
Index      Binary          Bucket ID    Local Depth     Entries
--------------------------------------------------------------------------------
0          00000           123875197418528 3               {8: 80} *
1          00001           123875197415744 4               {33: 330} *
2          00010           123875197419200 5               {2: 20} *
3          00011           123875197418240 4               {19: 190, 3: 30} *
4          00100           123875197418480 3               {36: 360, 12: 120} *
5          00101           123875197418960 3               {45: 450} *
6          00110           123875197415168 3               {30: 300, 6: 60} *
7          00111           123875197418432 3               {} *
8          01000           123875197418528 3               {8: 80}
9          01001           123875197419344 4               {41: 410, 25: 250} *
10         01010           123875197419008 4               {} *
11         01011           123875197418576 4               {27: 270} *
12         01100           123875197418480 3               {36: 360, 12: 120}
13         01101           123875197418960 3               {45: 450}
14         01110           123875197415168 3               {30: 300, 6: 60}
15         01111           123875197418432 3               {}
16         10000           123875197418528 3               {8: 80}
17         10001           123875197415744 4               {33: 330}
18         10010           123875197419248 5               {50: 500, 18: 180} *
19         10011           123875197418240 4               {19: 190, 3: 30}
20         10100           123875197418480 3               {36: 360, 12: 120}
21         10101           123875197418960 3               {45: 450}
22         10110           123875197415168 3               {30: 300, 6: 60}
23         10111           123875197418432 3               {}
24         11000           123875197418528 3               {8: 80}
25         11001           123875197419344 4               {41: 410, 25: 250}
26         11010           123875197419008 4               {}
27         11011           123875197418576 4               {27: 270}
28         11100           123875197418480 3               {36: 360, 12: 120}
29         11101           123875197418960 3               {45: 450}
30         11110           123875197415168 3               {30: 300, 6: 60}
31         11111           123875197418432 3               {}

============================================================
Unique Buckets: 12
============================================================


Detailed Bucket Contents:
============================================================

Bucket #0 (ID: 123875197418528)
  Local Depth: 3
  Capacity: 1/2
  Entries: {8: 80}
  Directory Indices: 0(00000), 8(01000), 16(10000), 24(11000)

Bucket #1 (ID: 123875197415744)
  Local Depth: 4
  Capacity: 1/2
  Entries: {33: 330}
  Directory Indices: 1(00001), 17(10001)

Bucket #2 (ID: 123875197419200)
  Local Depth: 5
  Capacity: 1/2
  Entries: {2: 20}
  Directory Indices: 2(00010)

Bucket #3 (ID: 123875197418240)
  Local Depth: 4
  Capacity: 2/2
  Entries: {19: 190, 3: 30}
  Directory Indices: 3(00011), 19(10011)

Bucket #4 (ID: 123875197418480)
  Local Depth: 3
  Capacity: 2/2
  Entries: {36: 360, 12: 120}
  Directory Indices: 4(00100), 12(01100), 20(10100), 28(11100)

Bucket #5 (ID: 123875197418960)
  Local Depth: 3
  Capacity: 1/2
  Entries: {45: 450}
  Directory Indices: 5(00101), 13(01101), 21(10101), 29(11101)

Bucket #6 (ID: 123875197415168)
  Local Depth: 3
  Capacity: 2/2
  Entries: {30: 300, 6: 60}
  Directory Indices: 6(00110), 14(01110), 22(10110), 30(11110)

Bucket #7 (ID: 123875197418432)
  Local Depth: 3
  Capacity: 0/2
  Entries: Empty
  Directory Indices: 7(00111), 15(01111), 23(10111), 31(11111)

Bucket #8 (ID: 123875197419344)
  Local Depth: 4
  Capacity: 2/2
  Entries: {41: 410, 25: 250}
  Directory Indices: 9(01001), 25(11001)

Bucket #9 (ID: 123875197419008)
  Local Depth: 4
  Capacity: 0/2
  Entries: Empty
  Directory Indices: 10(01010), 26(11010)

Bucket #10 (ID: 123875197418576)
  Local Depth: 4
  Capacity: 1/2
  Entries: {27: 270}
  Directory Indices: 11(01011), 27(11011)

Bucket #11 (ID: 123875197419248)
  Local Depth: 5
  Capacity: 2/2
  Entries: {50: 500, 18: 180}
  Directory Indices: 18(10010)

============================================================


======================================================================
TEST 5: Updating Values
======================================================================

Inserting keys 1-5...
  → Inserido no Bucket #123875197415744 (índice 1, local_depth=1)
  → Inserido no Bucket #123875197418624 (índice 0, local_depth=1)
  → Inserido no Bucket #123875197415744 (índice 1, local_depth=1)
  → Inserido no Bucket #123875197418624 (índice 0, local_depth=1)
  → Inserido no Bucket #123875197415744 (índice 1, local_depth=1)

Before update:
  → Encontrado no Bucket #123875197415744 (índice 1, local_depth=1)
  Key 1: 100
  → Encontrado no Bucket #123875197418624 (índice 0, local_depth=1)
  Key 2: 200
  → Encontrado no Bucket #123875197415744 (índice 1, local_depth=1)
  Key 3: 300
  → Encontrado no Bucket #123875197418624 (índice 0, local_depth=1)
  Key 4: 400
  → Encontrado no Bucket #123875197415744 (índice 1, local_depth=1)
  Key 5: 500

Updating key 3 to new value 999...
  → Inserido no Bucket #123875197415744 (índice 1, local_depth=1)

After update:
  → Encontrado no Bucket #123875197415744 (índice 1, local_depth=1)
  Key 1: 100
  → Encontrado no Bucket #123875197418624 (índice 0, local_depth=1)
  Key 2: 200
  → Encontrado no Bucket #123875197415744 (índice 1, local_depth=1)
  Key 3: 999
  → Encontrado no Bucket #123875197418624 (índice 0, local_depth=1)
  Key 4: 400
  → Encontrado no Bucket #123875197415744 (índice 1, local_depth=1)
  Key 5: 500

============================================================
Extensible Hash Structure
============================================================
Global Depth: 1
Directory Size: 2
Bucket Size: 3
============================================================

Directory Mapping:
Index      Binary          Bucket ID    Local Depth     Entries
--------------------------------------------------------------------------------
0          0               123875197418624 1               {2: 200, 4: 400} *
1          1               123875197415744 1               {1: 100, 3: 999, 5: 500} *

============================================================
Unique Buckets: 2
============================================================


Detailed Bucket Contents:
============================================================

Bucket #0 (ID: 123875197418624)
  Local Depth: 1
  Capacity: 2/3
  Entries: {2: 200, 4: 400}
  Directory Indices: 0(0)

Bucket #1 (ID: 123875197415744)
  Local Depth: 1
  Capacity: 3/3
  Entries: {1: 100, 3: 999, 5: 500}
  Directory Indices: 1(1)

============================================================


######################################################################
# ALL TESTS COMPLETED
######################################################################
```
