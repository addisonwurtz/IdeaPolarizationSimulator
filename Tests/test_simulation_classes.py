import unittest
from IdeaPolarizationSim.simulation_classes import Graph, User, NewsItem
from IdeaPolarizationSim.toy_graph import *

class TestGraph(unittest.TestCase):
    def test_graph(self):

        graph = Graph(nodes, edge_weights, 0.1)
        self.assertIn(user_1, graph.nodes)
        self.assertIn(user_5, graph.nodes)
        self.assertEqual(graph.edge_weights['1-2'], 0.8)
        self.assertEqual(graph.edge_weights['3-4'], 0.3)
        self.assertEqual(graph.update_rate, 0.1)


class TestUser(unittest.TestCase):
    def test_valid_user(self):
        test_user = User(1, 0.75, [])
        self.assertIsInstance(test_user.user_id, int)
        self.assertIsInstance(test_user.opinion_score, float)

    def test_invalid_user(self):
        self.assertRaises(TypeError, User('name', -1.0, []))
        self.assertRaises(TypeError, User(2, 'something else', []))


class TestNewsItem(unittest.TestCase):
    def test_valid_news_item(self):
        test_news_item = NewsItem(.5, [])
        self.assertIsInstance(test_news_item.opinion_score, float)

    def test_invalid_news_item(self):
        self.assertRaises(TypeError, NewsItem('good', ['apple', 'banana']))


if __name__ == '__main__':
    unittest.main()
