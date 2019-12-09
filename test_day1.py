from day1 import RocketObject
import unittest


class TestRocketObject(unittest.TestCase):
    def test_RocketObject_fuelType(self):
        # rocketObj = RocketObject('100756')
        self.assertRaisesRegexp(
            RuntimeError, 'Need an integer input', RocketObject, '100756')
        self.assertRaises

    def test_RocketObject_fuelA(self):
        rocketObj = RocketObject(100756)
        self.assertEqual(rocketObj.Fuel, 33583)

    def test_RocketObject_fuelB(self):
        rocketObj = RocketObject(100756)
        self.assertEqual(rocketObj.RecursiveFuel, 50346)


if __name__ == '__main__':
    unittest.main()
