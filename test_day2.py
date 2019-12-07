from day2 import IntcodeListObject
import unittest


class TestIntcodeListObject(unittest.TestCase):
    def test_IntcodeListObject_A(self):
        dataList = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        resultList = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        intcodeObj = IntcodeListObject(dataList)
        self.assertEqual(intcodeObj.Run(), resultList)

    def test_IntcodeListObject_B(self):
        dataList = [1,1,1,4,99,5,6,0,99]
        resultList = [30,1,1,4,2,5,6,0,99]
        intcodeObj = IntcodeListObject(dataList)
        self.assertEqual(intcodeObj.Run(), resultList)

if __name__ == '__main__':
    unittest.main()
