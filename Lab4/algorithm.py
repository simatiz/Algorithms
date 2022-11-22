from graph import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Algorithm:
    def __init__(self, file="files/input.txt"):
        # Зчитати дані для побудови графа з файлу
        with open(file, 'r') as f:
            lst = f.readlines()
            n = int(lst[0])
            lst = lst[1:]
            lst = [list(map(int, elem.split())) for elem in lst]

        self.n = n
        self.lst = lst

    def get_neighbours(self, vertex):
        # Отримати список сусідів для вершини
        result = []
        for key, val in self.lst:
            if key == vertex:
                result.append(val)

        return result

    def all_neighbours_not_in_same_color(self, vertex, vertex_colors, current_color):
        # Перевірити, чи всі сусіди мають інші кольори, від вершини
        neighbours = self.get_neighbours(vertex)
        neighbours_not_in_same_color = [vertex_colors[neighbor] != current_color for neighbor in neighbours]

        if sum(neighbours_not_in_same_color) == len(neighbours_not_in_same_color):
            return True

        return False

    def max_power_vertex(self):
        # Знайти у графі вершину з максимальною кількістю ребер
        elements = [row[0] for row in self.lst]
        max_val = max(set(elements), key=elements.count)

        return max_val

    def try_to_reduce_num_of_colors(self, vertex, vertex_colors, num_colors):
        # Спробувати зменшити кількість кольорів для кожного сусіда поточної вершини
        neighbours = self.get_neighbours(vertex)

        for neighbor in neighbours:
            temp_colors = vertex_colors.copy()
            # Поміняти колір із сусідом
            temp_colors[vertex], temp_colors[neighbor] = \
                temp_colors[neighbor], temp_colors[vertex]
            # Перевірити, чи можна виконати обмін
            if self.all_neighbours_not_in_same_color(
                   neighbor, temp_colors, temp_colors[neighbor]
               ):
                # Спробувати зменшити кількість кольорів
                new_color = Graph.get_available_color(
                    self.get_neighbours(neighbor),
                    temp_colors,
                    num_colors,
                    vertex_colors[neighbor]
                )
                # Якщо будь-який альтернативний колір підходить, то перефарбувати
                if new_color != -1:
                    temp_colors[neighbor] = new_color
                    vertex_colors = temp_colors.copy()

        return vertex_colors

    # Отримати вхідні дані з файлу та створити неорієнтований граф
    def create_graph(self):
        graph = nx.Graph()
        lst = Graph.remove_duplicate_edges(self.lst)

        for row in lst:
            graph.add_edge(row[0], row[1])

        return graph

    def show_graph(self, vertex_colors):
        # Показати граф
        print("Vertex colors:", vertex_colors)
        print("Number of colors:", len(set(vertex_colors)))
        graph = self.create_graph()

        Graph.draw_graph(graph, vertex_colors)
        plt.show()

    def greedy(self):
        current_color = 0
        # Список кольорів для кожної вершини. Примітка: -1 означає відсутність кольору
        vertex_colors = [-1 for _ in range(self.n)]

        while sum([val == -1 for val in vertex_colors]) != 0:
            for vertex in range(self.n):
                if vertex_colors[vertex] == -1:
                    if self.all_neighbours_not_in_same_color(
                           vertex, vertex_colors, current_color
                       ):
                        vertex_colors[vertex] = current_color
            current_color += 1

        return vertex_colors, current_color

    def bees(self):
        # Застосувати жадібний алгоритм
        vertex_colors, num_colors = self.greedy()

        # Намалювати розфарбований граф, створений за допомогою жадібного алгоритму
        self.show_graph(vertex_colors)

        # Знайти вершину з максимальним степенем (стартова вершина)
        vertex = self.max_power_vertex()
        # Список вершин для обробки
        nxt = [vertex]

        counter = 0
        parent = -1
        randomness = 1
        mutation = randomness

        while len(nxt) < 40:
            vertex = nxt[counter]
            neighbours = self.get_neighbours(vertex)
            for neighbor in neighbours:
                if neighbor != parent:
                    nxt.append(neighbor)
                if mutation == 0:
                    nxt.append(np.random.randint(0, self.n+1))
                    mutation = randomness
            parent = vertex
            counter += 1
            mutation -= 1

        for vertex in nxt:
            vertex_colors = self.try_to_reduce_num_of_colors(vertex, vertex_colors, num_colors)

        # Намалювати розфарбований граф, створений за допомогою класичного бджолиного алгоритму
        self.show_graph(vertex_colors)
