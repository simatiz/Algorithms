import numpy as np


class InputFile:
    # Створити довільний вхідний файл для графа
    def __init__(self, n=200, min_pow=1, max_pow=30, file='files/input.txt'):
        # n - кількість вершин у графі, min_pow - мінімальний степінь вершини
        # max_pow - максимальний степінь вершини, file - назва вихідного файлу
        self.n = n
        self.min_pow = min_pow
        self.max_pow = max_pow
        self.file = file

    def create(self):
        # Створити вхідний файл
        # Створити випадковий список зв'язків з використанням обмежень
        lst = []
        for i in range(self.n):
            num_of_edges = np.random.randint(1, self.max_pow + 1)
            all_vertexes = np.arange(self.n)
            np.random.shuffle(all_vertexes)
            neighbours = all_vertexes[:num_of_edges]

            for neighbor in neighbours:
                lst.append([i, neighbor])

        # Зберегти матрицю у файл
        with open(self.file, 'w') as f:
            f.write(str(self.n) + "\n")
            for key, value in lst:
                f.write(str(key) + " " + str(value) + "\n")
