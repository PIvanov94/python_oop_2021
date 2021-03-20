def fibonacci():
    start_num, next_num = 0, 1
    while True:
        yield start_num
        fibonacci_num = start_num + next_num
        start_num, next_num = next_num, fibonacci_num