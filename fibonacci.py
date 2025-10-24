def get_positive_int():
    while True:
        try:
          n = int(input("How many terms? "))
           if n > 0:
            return n
            else:
              print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def print_sequence(seq):
    print("Fibonacci sequence:", ", ".join(str(x) for x in seq))

def main():
    n = get_positive_int()
    seq = generate_fibonacci(n)
    print_sequence(seq)

if __name__ == "__main__":
    main()
