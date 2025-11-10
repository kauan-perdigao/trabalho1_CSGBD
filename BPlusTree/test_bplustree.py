import unittest
from BPlusTree.BPlusTree import BPlusTree


class TestBPlusTree(unittest.TestCase):
    def test_insert_search_remove(self):
        tree = BPlusTree(order=4)
        keys = [5, 1, 8, 3, 7, 2, 9, 4, 6]
        for k in keys:
            tree.insert(k, k * 100)

        for k in keys:
            self.assertEqual(tree.search(k), k * 100)

        self.assertIsNone(tree.search(999))

        for rem in [3, 4, 5]:
            self.assertTrue(tree.remove(rem))
            self.assertIsNone(tree.search(rem))

        self.assertFalse(tree.remove(3))


if __name__ == "__main__":
    unittest.main()
