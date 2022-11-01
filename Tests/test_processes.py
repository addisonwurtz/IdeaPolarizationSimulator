import unittest
import simpy
from IdeaPolarizationSim.processes import Person
from IdeaPolarizationSim.run_simulation import env


class TestClassObjects(unittest.TestCase):
    env = simpy.Environment

    def test_valid_person(self):
        my_person = Person(env, 1, 0.75)
        self.assertIsInstance(my_person.env, simpy.Environment)
        self.assertIsInstance(my_person.node, int)
        self.assertIsInstance(my_person.opinion, float)

    def test_invalid_person(self):
        self.assertRaises(TypeError, Person(env, 'Addison', -1.0))
        self.assertRaises(TypeError, Person(env, 2, 'independent'))

    def test_valid_news_item(self):
        pass


if __name__ == '__main__':
    unittest.main()
