import unittest
from simpy import Environment
from IdeaPolarizationSim.processes import Network, Person, NewsItem


class TestClassObjects(unittest.TestCase):
    env = Environment()

    def test_network(self):
        nodes = []
        edge_weights = {}

        person_1 = Person(self.env, 1, 1, [])
        person_2 = Person(self.env, 2, 0.9, [])
        person_3 = Person(self.env, 3, 0.6, [])
        person_4 = Person(self.env, 4, -0.2, [])
        person_5 = Person(self.env, 5, -0.65, [])
        person_6 = Person(self.env, 6, -1, [])

        person_1.add_connections([person_2, person_3])
        edge_weights['1-2'] = 0.8
        edge_weights['1-3'] = 0.9
        person_2.add_connections([person_1, person_3, person_5])
        edge_weights['2-3'] = 0.7
        edge_weights['2-5'] = 0.2
        person_3.add_connections([person_1, person_2, person_4])
        edge_weights['3-4'] = 0.3
        person_4.add_connections([person_3, person_5, person_6])
        edge_weights['4-5'] = 0.5
        edge_weights['4-6'] = 0.7
        person_5.add_connections([person_2, person_4, person_6])
        edge_weights['5-6'] = 0.8
        person_6.add_connections([person_4, person_5])

        nodes = [person_1, person_2, person_3, person_4, person_5, person_6]

        network = Network(self.env, nodes, edge_weights)
        self.assertIn(person_1, network.nodes)
        self.assertIn(person_5, network.nodes)
        self.assertEqual(network.edge_weights['1-2'], 0.8)
        self.assertEqual(network.edge_weights['3-4'], 0.3)

    def test_valid_person(self):
        test_person = Person(self.env, 1, 0.75, [])
        self.assertIsInstance(test_person.env, Environment)
        self.assertIsInstance(test_person.node, int)
        self.assertIsInstance(test_person.opinion, float)

    def test_invalid_person(self):
        self.assertRaises(TypeError, Person(self.env, 'name', -1.0, []))
        self.assertRaises(TypeError, Person(self.env, 2, 'something else', []))

    def test_valid_news_item(self):
        test_news_item = NewsItem(self.env, .5, [])
        self.assertIsInstance(test_news_item.env, Environment)
        self.assertIsInstance(test_news_item.opinion_score, float)

    def test_invalid_news_item(self):
        self.assertRaises(TypeError, NewsItem(self.env, 'good', ['apple', 'banana']))


if __name__ == '__main__':
    unittest.main()
