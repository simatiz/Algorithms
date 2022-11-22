import networkx as nx


class Graph:
    def __init__(self):
        self.x = 0

    @staticmethod
    def get_available_color(neighbours, vertex_colors, num_colors, old_color):
        # Отримати перший доступний колір, якого немає у сусідів
        available_colors = [color for color in range(num_colors)]

        for neighbor in neighbours:
            color = vertex_colors[neighbor]
            if color in available_colors:
                available_colors.remove(color)

        if old_color in available_colors:
            available_colors.remove(old_color)

        if len(available_colors) != 0:
            return available_colors[0]

        return -1

    @staticmethod
    def remove_duplicate_edges(lst):
        # Видаляти повтори, наприклад 1-3, 3-1, або 1-1
        new_list = []
        for key, val in lst:
            if key != val:
                if [key, val] and [val, key] not in new_list:
                    new_list.append([key, val])

        return new_list

    @staticmethod
    def draw_graph(graph, vertex_colors):
        # Намалювати граф
        pos = nx.spring_layout(graph)
        colors = ['red', 'blue', 'yellow', 'purple', 'orange', 'black', 'green', 'grey', 'purple', 'pink', 'brown']
        values = [colors[vertex_colors[node]] for node in graph.nodes()]

        nx.draw(graph, pos, with_labels=True, node_color=values, edge_color='black', width=1, alpha=0.7)
