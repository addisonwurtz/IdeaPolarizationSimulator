from IdeaPolarizationSim.graph_builder import GraphBuilder
from IdeaPolarizationSim.simulation import Simulation
from IdeaPolarizationSim.simulation_classes import NewsItem, SocialNetwork, GraphData

if __name__ == "__main__":
    update_rate = 0.2
    time = 0
    graph_size = 1000
    max_time = 10000

    graph = GraphData([], {}, update_rate)
    graphBuilder = GraphBuilder(graph, '0.edges')
    graphBuilder.build_graph(graph_size)

    news_items = graphBuilder.create_news_items()
    # news_items = toy_graph.news_items

    social_network = SocialNetwork(graph, news_items, update_rate)

    my_simulation = Simulation(social_network, max_time)

    # animation = Animation(my_simulation)
    # animation.on_execute()

    # Skip animation, just generate images
    while my_simulation.current_news_item is not None and my_simulation.time <= my_simulation.max_time:
        time = my_simulation.update_simulation()


