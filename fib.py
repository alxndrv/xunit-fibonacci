import sys


def get_fibonacci_seq(start, N=10):
    results = []
    count = 0

    prevValue = 0
    value = 1

    if start == 0:
        results.append(1)

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


# Generates the requested fibonacci sequence, writes it to a file and returns it as a list
def fibonacci(argv):
    # Arguments should be:
    # - Starting number
    # - Length of elements to output (default to 10)
    if len(argv) < 1:
        raise RuntimeError("""
        Missing one or more arguments
        Usage: fib.py <start> [<count>]
        """)

    start = int(argv[0])
    N = int(argv[1]) if len(argv) > 1 else 10

    results = get_fibonacci_seq(start, N)
    write_sequence_to_file(results)

    print(results)
    return results


if __name__ == '__main__':
    fibonacci(sys.argv[1:])
