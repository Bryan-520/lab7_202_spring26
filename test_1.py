import unittest

from lab7_1 import MinHeap, insert, extract, heapify_up, heapify_down


class TestMinHeap(unittest.TestCase):
    def test_insert(self):
        my_heap = MinHeap([])
        self.assertEqual(insert(my_heap, 10), MinHeap([10]))

    def test_insert_multiple(self):
        my_heap = MinHeap([10])
        self.assertEqual(insert(my_heap, 5), MinHeap([5, 10]))

    def test_extract(self):
        my_heap = MinHeap([5, 10])
        self.assertEqual(extract(my_heap), (5, MinHeap([10])))

    def test_extract_twice(self):
        my_heap = MinHeap([5, 10, 15])
        val1, heap1 = extract(my_heap)

        self.assertEqual(extract(heap1), (10, MinHeap([15])))

    def test_heapify_up(self):
        heap = [5, 10, 8, 20, 15, 9, 1]
        result = heapify_up(heap, 6)
        self.assertEqual(result, [1, 10, 5, 20, 15, 9, 8])

    def test_heapify_down(self):
        heap = [9, 3, 5]
        result = heapify_down(heap, 0)
        self.assertEqual(result, [3, 9, 5])


if __name__ == "__main__":
    unittest.main()
