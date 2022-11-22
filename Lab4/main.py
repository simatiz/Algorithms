from input_file import *
from algorithm import *


def main():
    fill = InputFile(file='files/input.txt')
    fill.create()

    algorithms = Algorithm()
    algorithms.bees()


if __name__ == "__main__":
    main()
