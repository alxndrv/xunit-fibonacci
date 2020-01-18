import sys


def get_fibonacci_seq(start, N):
    results = []
    count = 0

    prevValue = 0
    value = 1

    while count < N:
        # tmp = prevValue + value
        prevValue, value = value, prevValue + value

        if value > start:
            count += 1
            results.append(value)

    return results


def write_sequence_to_file(seq, filename="fibonacci.txt"):
    with open(filename, "w") as f:
        for i in seq:
            f.write(str(i) + "\n")
        f.close()


def fibonacci(argv):
    # Arguments should be:
    # - Starting number
    # - Length of elements to output (default to 10)
    if len(argv) < 1:
        print("Missing one or more arguments")
        print("Usage: main.py <start> [<count>]")

        return

    start = int(argv[0])
    N = int(argv[1]) if len(argv) > 1 else 10

    results = get_fibonacci_seq(start, N)
    write_sequence_to_file(results)

    print(results)


if __name__ == '__main__':
    fibonacci(sys.argv[1:])
