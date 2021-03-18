import numpy as np
import sys


yes = ['y', 'yes', 'Y', 'Yes']
line = '============================================================'
def tui():

    print(chr(27) + "[2J")
    print(line)
    print('=   Authors: ')
    print('=   - Karolina Jablonska, 295813')
    print('=   - Wojciech Marosek, 295818')
    print(line)
    print('=   EARIN | Exercise 2 | Genetic algorithm')
    print(line)

    try:
        """
        Read function parameters: matrix A, vector b, and scalar c | f(x) = x^T * A * x + b^t * x + c
        """
        in_text = input('=   Please input vector B (i.e.: 1,2,3) : ')
        vector_b = format_input(in_text, ',')
        vector_len = len(vector_b)
        vector_b = np.asarray(vector_b).astype(np.float)

        vector_temp = []

        print('=   Please input symmetric matrix with dimension {n}x{n}'.format(n=vector_len) + ': ')
        for x in range(0, vector_len):
            in_text = input('=   Please input {n}th row of matrix A (i.e.: 1,2,3) : '.format(n=x))
            vector_temp.append(format_input(in_text, ','))

        matrix_a = np.asarray(vector_temp).astype(np.float)

    #    if not (is_symmetric(matrix_a) and is_positive_definite(matrix_a)):
    #        raise ValueError

        scalar_c = int(input('=   Please input scalar C (integer) : '))
        if not isinstance(scalar_c, int):
            raise ValueError

        print_variables(matrix_a, vector_b, scalar_c)
        print(line)

        """
        Read dimensionality, the range of searched integers, population size, crossover probability, mutation probability, number (N) of iteration
        """

        print('=   Please define dimensionality')
        dimension = int(input('=   in example: "2" - integer: '))

        print('=   Please define population_size')
        population_size = int(input('=   in example: "50" - integer: '))

        print('=   Please define range of searched integers')
        range_search = input('=   in example: "1, 2": ')
        range_search = format_input(range_search, ',')

        print(len(range_search))
        if not (len(range_search) == 2):
            raise ValueError
        else:
            new_population = np.random.uniform(range_search[0], range_search[1], size=population_size)

        print('=   Please define crossover probability')
        cross_probability = float(input('=   in example: "0.9" - float: '))

        print('=   Please define mutation probability')
        mutation_probability = float(input('=   in example: "0.05" - float: '))

        no_iter = int(input('=   Please specify number of iteration: '))
        if not no_iter <= 100:
            raise ValueError

#        run_method(matrix_a, vector_b, scalar_c, start_point)
#        print(line)


#        ans = 'y'
#        while ans in yes:
#            ans = input('=   Would you like run another method (y | n):')
#            if ans in yes:
#                run_method(matrix_a, vector_b, scalar_c, start_point)
#                print(line)

    except ValueError:
        error = 'Defined input variables are incorrect! Please define valid one!'
        print_error(error)
    except np.linalg.LinAlgError:
        error = 'Defined matrix is not a positive-definite! Please input valid one!'
        print_error(error)

#    ans = input('=   Would you like input new variables (y | n):')
#    if ans in yes:
#        tui()
#    else:
#        sys.exit()

"""
Converts string to the array. Responsible for fetching input data in correct format.
input: text - string, delimiter - char
output: array of delimited strings
"""


def format_input(text, delimiter):
    text = text.replace(' ', '')
    text = text.split(delimiter)
    return text


"""
Printing a error message and asking user next execution of program
input: error - String
output: n/a
"""


def print_error(error):
    yes = ['y', 'yes', 'Y', 'Yes']

    print('=\n=   ' + error)
    ans = input('=   Would you like input new variables (y | n):')
    if ans in yes:
        tui()
    else:
        sys.exit()


"""
Printing a input variable for the task
input: matrix, vector, scalar
output: n/a
"""


def print_variables(matrix, vector, scalar):
    print(line)
    print('=   Defined variables:')
    print('=   Matrix:\n')
    print(matrix)
    print('\n=   Vector:\n')
    print(vector)
    print('\n=   Scalar: ' + str(scalar))


if __name__ == "__main__":
    tui()