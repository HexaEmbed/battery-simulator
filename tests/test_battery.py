import unittest
from backend.battery import Battery

class TestBattery(unittest.TestCase):
    def test_discharge(self):
        b = Battery(100)
        b.discharge(20)
        self.assertEqual(b.level, 80)

    def test_charge(self):
        b = Battery(100)
        b.discharge(50)
        b.charge(30)
        self.assertEqual(b.level, 80)

if __name__ == "__main__":
    unittest.main()
