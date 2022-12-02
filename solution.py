import numpy as np
import os
import timeit
from typing import Union


class AdventOfCodeSolution:
    def __init__(self, day: int):
        self.__location__: str = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.main(day)

    def main(self, day: int) -> Union[str, int]:
        match day:
            case 1:
                self.day_one()
            case 2:
                self.day_two()
            case other:
                raise NotImplementedError('This day has not been implemented yet.')

    def day_one(self):
        with open(os.path.join(self.__location__, 'day01/input.txt'), 'r') as raw_input:
            input_data: str = raw_input.read()

        input_array: np.array = np.array([np.sum(np.array(line, dtype=object)) for line in list(
            map(lambda each: list(map(int, each.split('\n'))), input_data.split('\n\n')))], dtype=object)

        max_idx: int = np.argmax(input_array)

        print(f'Elf number {max_idx} is carrying the most calories, with {input_array[max_idx]} calories.')

    def day_two(self):
        with open(os.path.join(self.__location__, 'day02/input.txt'), 'r') as raw_input:
            input_data: str = raw_input.read()

        input_array: np.array = np.array([np.sum(np.array(line, dtype=object)) for line in list(
            map(lambda each: list(map(int, each.split('\n'))), input_data.split('\n\n')))], dtype=object)

        total_calories = np.sum(np.sort(input_array)[-3:])
        
        print(f'The three elves with the most calories, together, have {total_calories} calories.')

if __name__ == '__main__':
    while True:
        day_input = int(input('Which day do you want to run? '))
        start_time = timeit.default_timer()
        AdventOfCodeSolution(day_input)
        delta = timeit.default_timer() - start_time
        print(f'\nRan in: {delta}s\n\n')
