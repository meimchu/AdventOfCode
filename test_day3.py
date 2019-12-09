from day3 import MoveMachine
import unittest


class TestMoveMachineObject(unittest.TestCase):
    def test_MoveMachineObject_A(self):
        dataList = [["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]]
        machine = MoveMachine()
        for data in dataList:
            wire = machine.AddWire()
            machine.MoveWireByData(wire, data)
        self.assertEqual(machine.GetShortestDistanceToStart(), 6)
        self.assertEqual(machine.GetShortestDistanceFromStepsToStart(), 30)

    def test_MoveMachineObject_B(self):
        dataList = [["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"], [
            "U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]]
        machine = MoveMachine()
        for data in dataList:
            wire = machine.AddWire()
            machine.MoveWireByData(wire, data)
        self.assertEqual(machine.GetShortestDistanceToStart(), 159)
        self.assertEqual(machine.GetShortestDistanceFromStepsToStart(), 610)

    def test_MoveMachineObject_C(self):
        dataList = [["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"], [
            "U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]]
        machine = MoveMachine()
        for data in dataList:
            wire = machine.AddWire()
            machine.MoveWireByData(wire, data)
        self.assertEqual(machine.GetShortestDistanceToStart(), 135)
        self.assertEqual(machine.GetShortestDistanceFromStepsToStart(), 410)


if __name__ == '__main__':
    unittest.main()
