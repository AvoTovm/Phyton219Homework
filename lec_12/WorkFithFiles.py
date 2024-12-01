import random
import time

def create_file(filename):
    with open(filename, 'w') as f:
        for _ in range(100):
            line = ' '.join(str(random.randint(1, 100)) for _ in range(20))
            f.write(line + '\n')


def process_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    int_arrays = [list(map(int, line.split())) for line in lines]
    return int_arrays

def filter_and_write_back(filename, int_arrays):
    with open(filename, 'w') as f:
        for arr in int_arrays:
            filtered = list(filter(lambda x: x > 40, arr))
            f.write(' '.join(map(str, filtered)) + '\n')

def read_file_as_generator(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper


@decorator
def full_pipeline():
    filename = 'random_numbers.txt'
    create_file(filename)
    int_arrays = process_lines(filename)
    filter_and_write_back(filename, int_arrays)

    print("\nReading file as generator:")
    for line in read_file_as_generator(filename):
        print(line)


full_pipeline()