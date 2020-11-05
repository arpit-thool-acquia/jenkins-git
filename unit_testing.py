import unittest
from map import Car
from road import Road, Urban, Rural


class CarTest(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_urban(self):
        urban = Urban("urban", 900)
        self.assertEqual(self.car.mapping(urban)["totalDistanceTravelled"], 1000)

    def test_rural(self):
        rural = Rural("rural", 900)
        self.assertEqual(self.car.mapping(rural)["totalDistanceTravelled"], 1050)


    def test_largeinput_urban(self):
        urban = Urban("urban", 463808250)
        self.assertIsNotNone(self.car.mapping(urban)["totalDistanceTravelled"])


    def test_largeinput_rural(self):
        rural = Rural("rural", 900539000)
        self.assertIsNotNone(self.car.mapping(rural)["totalDistanceTravelled"])
    
    # def test_negative_urban(self):
    #     rural = Rural("rural", -10)
    #     self.assertEqual(self.car.mapping(rural)["totalDistanceTravelled"], 0)

    # def test_negative_rural(self):
    #     urban = Urban("urban", -50)
    #     self.assertEqual(self.car.mapping(urban)["totalDistanceTravelled"], 0)

if __name__ == '__main__':
    unittest.main()