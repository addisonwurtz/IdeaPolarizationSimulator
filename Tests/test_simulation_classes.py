import unittest
from unittest.mock import Mock, patch
from IdeaPolarizationSim.simulation_classes import NewsItem, User, Graph, SocialNetwork, UserNotInfectiousError


class TestSocialNetwork(unittest.TestCase):
    def test_probability_of_infection(self):
        from IdeaPolarizationSim import toy_graph
        news_item = NewsItem(1, 0.8, [])
        social_network = SocialNetwork(toy_graph.graph, news_item, 0.1)

        self.assertEqual(0.89, social_network.probability_of_infection(toy_graph.user_1, toy_graph.user_3, news_item))

    def test_share_news_item(self):
        from IdeaPolarizationSim import toy_graph
        news_item = NewsItem(1, 0.8, [toy_graph.user_4])
        social_network = SocialNetwork(toy_graph.graph, news_item, 0.1)

        with patch('IdeaPolarizationSim.simulation_classes.SocialNetwork.probability_of_infection') \
                as mock_probability_of_infection:
            mock_probability_of_infection.return_value = 1
            social_network.share_news_item(toy_graph.user_4, news_item)

            for connection in toy_graph.user_4.connections:
                self.assertIn(connection, news_item.inoculated_users)
                self.assertIn(connection, news_item.infectious_users)

            self.assertNotIn(toy_graph.user_4, news_item.infectious_users)
            self.assertIn(toy_graph.user_4, news_item.inoculated_users)

    def test_share_news_item_raises_error_for_user_not_in_infectious_list(self):
        from IdeaPolarizationSim import toy_graph
        news_item = NewsItem(1, 0.8, [])
        user = Mock()
        social_network = SocialNetwork(toy_graph.graph, news_item, 0.1)

        with self.assertRaises(UserNotInfectiousError):
            social_network.share_news_item(user, news_item)


class TestGraph(unittest.TestCase):
    def test_graph(self):
        from IdeaPolarizationSim import toy_graph

        test_graph = Graph(toy_graph.nodes, toy_graph.edge_weights, 0.1)
        self.assertIn(toy_graph.user_1, test_graph.nodes)
        self.assertIn(toy_graph.user_5, test_graph.nodes)
        self.assertEqual(test_graph.edge_weights['1-2'], 0.8)
        self.assertEqual(test_graph.edge_weights['3-4'], 0.3)
        self.assertEqual(test_graph.update_rate, 0.1)

    def test_increase_connection_strength(self):
        user1 = User(1, 0.75, [])
        user2 = User(2, -0.5, [user1])
        user1.add_connections([user2])
        edge_weight = {'1-2': 0.5}
        test_graph = Graph([user1, user2], edge_weight, update_rate=0.1)

        test_graph.increase_connection_strength(user1, user2)
        self.assertEqual(0.6, test_graph.edge_weights['1-2'])

    def test_decrease_connection_strength(self):
        user1 = User(1, 0.75, [])
        user2 = User(2, -0.5, [user1])
        user1.add_connections([user2])
        edge_weight = {'1-2': 0.5}
        test_graph = Graph([user1, user2], edge_weight, update_rate=0.1)

        test_graph.decrease_connection_strength(user1, user2)
        self.assertEqual(0.4, test_graph.edge_weights['1-2'])

    def test_get_edge_string(self):
        user1 = User(1, 0.2, [])
        user2 = User(2, -0.4, [])

        self.assertEqual('1-2', Graph.get_edge_string(user1, user2))
        self.assertEqual('1-2', Graph.get_edge_string(user2, user1))

    def test_get_edge_string_raises_value_error_when_nodes_are_the_same(self):
        user = Mock()
        with self.assertRaises(ValueError):
            Graph.get_edge_string(user, user)

    def test_get_edge_weight_for_valid_edge(self):
        user1 = User(1, 0.2, [])
        user2 = User(2, -0.4, [])
        edge_weight = {'1-2': 0.65}

        test_graph = Graph([user1, user2], edge_weight)

        self.assertEqual(0.65, test_graph.get_edge_weight(user1, user2))
        self.assertEqual(0.65, test_graph.get_edge_weight(user2, user1))

    def test_get_edge_weight_catches_value_error_when_args_Are_the_same_node(self):
        user = Mock()
        test_graph = Graph(user, {})
        with self.assertRaises(ValueError):
            test_graph.get_edge_weight(user, user)

    def test_get_edge_weight_on_edge_not_in_graph(self):
        user1 = Mock()
        user2 = Mock()
        test_graph = Graph(user1, {})
        with self.assertRaises(KeyError):
            test_graph.get_edge_weight(user1, user2)


class TestUser(unittest.TestCase):
    def test_valid_user(self):
        test_user = User(1, 0.75, [])
        self.assertIsInstance(test_user.user_id, int)
        self.assertIsInstance(test_user.opinion_score, float)

    def test_invalid_user(self):
        self.assertRaises(TypeError, User('name', -1.0, []))
        self.assertRaises(TypeError, User(2, 'something else', []))

    def test_get_connections(self):
        connection1 = User(2, 0.5, [])
        connection2 = User(3, 1, [])
        connections = [connection1, connection2]
        test_user = User(1, 0.75, connections)

        self.assertEqual(test_user.get_connections(), connections)

    def test_add_connections_with_list(self):
        test_user = User(1, 0.75, [])
        connection1 = User(2, 0.5, [])
        connection2 = User(3, 1, [])
        connection3 = User(4, 0.15, [])
        connections = [connection1, connection2, connection3]

        test_user.add_connections(connections)

        self.assertIn(connection1, test_user.connections)
        self.assertIn(connection2, test_user.connections)
        self.assertIn(connection3, test_user.connections)

    def test_add_connections_by_adding_single_new_connection_to_existing_list(self):
        connection1 = User(2, 0.5, [])
        connection2 = User(3, 1, [])
        connection3 = User(4, 0.15, [])
        connections = [connection1, connection2, connection3]
        test_user = User(1, 0.75, connections)

        new_connection = User(5, 0.9, [])
        test_user.add_connections([new_connection])

        self.assertIn(new_connection, test_user.connections)

    def test_update_opinion_to_increase_opinion_score(self):
        opinion_update_rate = 0.1
        news_item_opinions_score = 1.0
        test_user = User(1, 0.75, [], opinion_update_rate)
        test_user.update_opinion(news_item_opinions_score)

        self.assertEqual(test_user.opinion_score, 0.75 + opinion_update_rate * news_item_opinions_score)

    def test_update_opinion_to_decrease_opinion_score(self):
        opinion_update_rate = 0.1
        news_item_opinions_score = -1.0
        test_user = User(1, 0.75, [], opinion_update_rate)
        test_user.update_opinion(news_item_opinions_score)

        self.assertEqual(test_user.opinion_score, 0.75 - opinion_update_rate * news_item_opinions_score)


class TestNewsItem(unittest.TestCase):
    def test_valid_news_item(self):
        test_news_item = NewsItem(1, 0.5, [])
        self.assertIsInstance(test_news_item.opinion_score, float)

    def test_invalid_news_item(self):
        self.assertRaises(TypeError, NewsItem(1, 'good', ['apple', 'banana']))

    def test_infect_user_updates_infectious_and_inoculated_lists(self):
        user = User(1, 0.5, [])
        news_item = NewsItem(1, 0.3, [])

        news_item.infect_user(user)

        self.assertIs(user, news_item.infectious_users[0])
        self.assertIn(user, news_item.infectious_users)
        self.assertIn(user, news_item.inoculated_users)

    def test_infect_user_does_not_add_duplicates_to_infectious_and_inoculated_lists(self):
        user = User(1, 0.5, [])
        news_item = NewsItem(1, 0.3, [])

        news_item.infect_user(user)
        news_item.infect_user(user)

        self.assertEqual(1, news_item.infectious_users.count(user))
        self.assertEqual(1, news_item.inoculated_users.count(user))

    def test_infect_user_does_not_add_user_that_is_inoculated_but_not_infectious(self):
        user = User(1, 0.5, [])
        news_item = NewsItem(1, 0.3, [])

        news_item.infect_user(user)
        news_item.remove_user_from_infectious_list(user)
        news_item.infect_user(user)

        self.assertNotIn(user, news_item.infectious_users)
        self.assertIn(user, news_item.inoculated_users)

    def test_remove_user_from_infectious_list_removes_user(self):
        user = User(1, 0.5, [])
        news_item = NewsItem(1, 0.3, [])

        news_item.infect_user(user)
        news_item.remove_user_from_infectious_list(user)

        self.assertNotIn(user, news_item.infectious_users)
        self.assertIn(user, news_item.inoculated_users)


if __name__ == '__main__':
    unittest.main()
