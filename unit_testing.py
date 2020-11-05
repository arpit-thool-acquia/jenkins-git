import unittest
from map import Car
from road import Road, Urban, Rural


class CarTest(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_urban(self):
        urban = Urban("urban", 900)
        self.assertEqual(self.car.mapping(urban)["totalDistanceTravelled"], 1000)

    def test_urban1(self):
        urban = Urban("urban", 150)
        self.assertEqual(self.car.mapping(urban)["totalDistanceTravelled"], 200)

    def test_urban2(self):
        urban = Urban("urban", 4000)
        self.assertEqual(self.car.mapping(urban)["totalDistanceTravelled"], 4300)

    def test_urban3(self):
        urban = Urban("urban", 40)
        self.assertEqual(self.car.mapping(urban)["totalDistanceTravelled"], 80)

    def test_urban4(self):
        urban = Urban("urban", 650)
        self.assertEqual(self.car.mapping(urban)["totalDistanceTravelled"], 730)

    def test_rural(self):
        rural = Rural("rural", 900)
        self.assertEqual(self.car.mapping(rural)["totalDistanceTravelled"], 1040)

    def test_rural1(self):
        rural = Rural("rural", 150)
        self.assertEqual(self.car.mapping(rural)["totalDistanceTravelled"], 260)

    def test_rural2(self):
        rural = Rural("rural", 4000)
        self.assertEqual(self.car.mapping(rural)["totalDistanceTravelled"], 4300)

    def test_rural3(self):
        rural = Rural("rural", 40)
        self.assertEqual(self.car.mapping(rural)["totalDistanceTravelled"], 140)

    def test_rural4(self):
        rural = Rural("rural", 650)
        self.assertEqual(self.car.mapping(rural)["totalDistanceTravelled"], 780)

    
    def test_refuel_urban1(self):
        urban = Urban("urban", 1200)
        self.assertEqual(self.car.mapping(urban)["totalRefuels"], 8)

    def test_refuel_urban2(self):
        urban = Urban("urban", 5321)
        self.assertEqual(self.car.mapping(urban)["totalRefuels"], 35)

    def test_refuel_rural1(self):
        rural = Rural("rural", 1200)
        self.assertEqual(self.car.mapping(rural)["totalRefuels"], 6)

    def test_refuel_rural2(self):
        rural = Rural("rural", 5321)
        self.assertEqual(self.car.mapping(rural)["totalRefuels"], 26)

    def test_largeinput_urban(self):
        urban = Urban("urban", 463808250)
        self.assertIsNotNone(self.car.mapping(urban)["totalDistanceTravelled"])


    def test_largeinput_rural(self):
        rural = Rural("rural", 900539000)
        self.assertIsNotNone(self.car.mapping(rural)["totalDistanceTravelled"])
    

if __name__ == '__main__':
    unittest.main()