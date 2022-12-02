import numpy as np
import os
import timeit
from typing import Union, Callable


class AdventOfCodeSolution:
    def __init__(self, day: int):
        self.__location__: str = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.main(day)

    def main(self, day: int) -> Union[str, int]:
        match day:
            case 1:
                self.run_day(self.day_one)
            case 2:
                self.run_day(self.day_two)
            case other:
                raise NotImplementedError(
                    'This day has not been implemented yet.')

    def run_day(self, day_solution: Callable) -> None:
        start_time = timeit.default_timer()
        day_solution()
        delta = timeit.default_timer() - start_time
        print(f'\nRan in: {delta}s\n\n')

    def day_one(self) -> str:
        # Part 1
        with open(os.path.join(self.__location__, 'day01/input.txt'), 'r') as raw_input:
            input_data: str = raw_input.read()

        input_array: np.array = np.array([np.sum(np.array(line, dtype=object)) for line in list(
            map(lambda each: list(map(int, each.split('\n'))), input_data.split('\n\n')))], dtype=object)

        max_idx: int = np.argmax(input_array)

        print(
            f'Elf number {max_idx} is carrying the most calories, with {input_array[max_idx]} calories.')

        # Part 2

        total_calories = np.sum(np.sort(input_array)[-3:])

        print(
            f'The three elves with the most calories, together, have {total_calories} calories.')

    def day_two(self) -> str:
        # Part 1
        with open(os.path.join(self.__location__, 'day02/input.txt'), 'r') as raw_input:
            raw_input_data: list = raw_input.read().splitlines()

        input_data = np.array([np.array(line.split(), dtype=object) for line in raw_input_data], dtype=object)
        
        def calculate_rps_outcome(input: Union[np.array, list]) -> int:
            total_points = 0

            # [X | A]: Rock
            # [Y | B]: Paper
            # [Z | C]: Scissors
            player_sign = input[1]
            opponent_sign = input[0]

            match player_sign:
                case 'X': # Rock
                    total_points += 1
                    match opponent_sign:
                        case 'A': # Rock with Rock, draw
                            total_points += 3
                        case 'B': # Rock with Paper, lose
                            total_points += 0
                        case 'C': # Rock with Scissors, win
                            total_points += 6

                case 'Y': # Paper
                    total_points += 2
                    match opponent_sign:
                        case 'A': # Paper with Rock, win
                            total_points += 6
                        case 'B': # Paper with Paper, draw
                            total_points += 3
                        case 'C': # Paper with Scissors, lose
                            total_points += 0

                case 'Z': # Scissors
                    total_points += 3
                    match opponent_sign:
                        case 'A': # Scissors with Rock, lose
                            total_points += 0
                        case 'B': # Scissors with Paper, win
                            total_points += 6
                        case 'C': # Scissors with Scissors, draw
                            total_points += 3

            return total_points

        answer1 = np.sum(np.array([calculate_rps_outcome(game) for game in input_data], dtype=object))

        print(f'My total score, if everything goes exactly according to the strategy guide, is {answer1}')

        def calculate_rps_outcome_winlose(input: Union[np.array, list]) -> int:
            total_points = 0

            # [X | A]: Rock +1
            # [Y | B]: Paper +2
            # [Z | C]: Scissors +3
            player_sign = input[1]
            opponent_sign = input[0]

            match opponent_sign:
                case 'A': # Rock
                    match player_sign:
                        case 'X': # Lose, Scissors
                            total_points += 0
                            total_points += 3
                        case 'Y': # Draw, Rock
                            total_points += 3
                            total_points += 1
                        case 'Z': # Win, Paper
                            total_points += 6
                            total_points += 2

                case 'B': # Paper
                    match player_sign:
                        case 'X': # Lose, Rock
                            total_points += 0
                            total_points += 1
                        case 'Y': # Draw, Paper
                            total_points += 3
                            total_points += 2
                        case 'Z': # Win, Scissors
                            total_points += 6
                            total_points += 3

                case 'C': # Scissors
                    match player_sign:
                        case 'X': # Lose, Paper
                            total_points += 0
                            total_points += 2
                        case 'Y': # Draw, Scissors
                            total_points += 3
                            total_points += 3
                        case 'Z': # Win, Rock
                            total_points += 6
                            total_points += 1
                

            return total_points

        answer2 = np.sum(np.array([calculate_rps_outcome_winlose(game) for game in input_data], dtype=object))

        print(f'My total score, if everything goes exactly according to the strategy guide and understanding the elf, is {answer2}')

if __name__ == '__main__':
    day_input = int(input('Which day do you want to run? '))
    AdventOfCodeSolution(day_input)
